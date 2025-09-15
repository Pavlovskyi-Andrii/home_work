const express = require('express');
const winston = require('winston');
const FluentLogger = require('fluent-logger');


// Настройка Winston для локального логирования
const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  transports: [
    new winston.transports.Console()
  ]
});

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware для парсинга JSON
app.use(express.json());

// Middleware для логирования запросов
app.use((req, res, next) => {
  const logData = {
    method: req.method,
    url: req.url,
    ip: req.ip,
    timestamp: new Date().toISOString(),
    userAgent: req.get('User-Agent')
  };
  
  logger.info('HTTP Request', logData);
  
  // Отправляем лог в Fluentd
  fluentLogger.emit('access', logData);
  
  next();
});

// Основные маршруты
app.get('/', (req, res) => {
  res.json({
    message: 'Node.js App is running!',
    timestamp: new Date().toISOString(),
    uptime: process.uptime()
  });
});

app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    memory: process.memoryUsage()
  });
});

// Маршрут для тестирования логирования
app.post('/log', (req, res) => {
  const logLevel = req.body.level || 'info';
  const message = req.body.message || 'Test log message';
  const data = req.body.data || {};
  
  const logEntry = {
    level: logLevel,
    message: message,
    data: data,
    timestamp: new Date().toISOString(),
    source: 'nodejs-app'
  };
  
  logger.log(logLevel, message, data);
  fluentLogger.emit('application', logEntry);
  
  res.json({ 
    success: true, 
    logged: logEntry 
  });
});

// Обработка ошибок
app.use((err, req, res, next) => {
  const errorLog = {
    error: err.message,
    stack: err.stack,
    url: req.url,
    method: req.method,
    timestamp: new Date().toISOString()
  };
  
  logger.error('Application Error', errorLog);
  fluentLogger.emit('error', errorLog);
  
  res.status(500).json({ 
    error: 'Internal Server Error',
    timestamp: new Date().toISOString()
  });
});

// Запуск сервера
app.listen(PORT, '0.0.0.0', () => {
  const startupLog = {
    message: `Server started on port ${PORT}`,
    port: PORT,
    timestamp: new Date().toISOString(),
    nodeVersion: process.version
  };
  
  logger.info('Server Startup', startupLog);
  fluentLogger.emit('startup', startupLog);
});

// Graceful shutdown
process.on('SIGTERM', () => {
  logger.info('Received SIGTERM, shutting down gracefully');
  fluentLogger.emit('shutdown', { 
    message: 'Application shutting down',
    timestamp: new Date().toISOString() 
  });
  process.exit(0);
});

process.on('SIGINT', () => {
  logger.info('Received SIGINT, shutting down gracefully');
  fluentLogger.emit('shutdown', { 
    message: 'Application shutting down',
    timestamp: new Date().toISOString() 
  });
  process.exit(0);
});
