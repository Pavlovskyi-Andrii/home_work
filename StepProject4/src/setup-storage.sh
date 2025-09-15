#!/bin/bash
# setup-storage.sh - Подготовка директорий для Persistent Volumes

echo "🔧 Setting up storage directories for Kubernetes Persistent Volumes..."

# Для Minikube нужно создать директории внутри Minikube VM
if command -v minikube &> /dev/null; then
    echo "📁 Creating directories in Minikube..."
    
    # Создаем директории в Minikube
    minikube ssh "sudo mkdir -p /data/mysql && sudo chmod 777 /data/mysql"
    minikube ssh "sudo mkdir -p /data/app && sudo chmod 777 /data/app"
    
    echo "✅ Directories created in Minikube:"
    minikube ssh "ls -la /data/"
    
    # Монтируем локальные директории (опционально)
    echo "📂 You can also mount local directories:"
    echo "minikube mount /local/path:/data/mysql"
    
else
    echo "📁 Creating local directories (for Docker Desktop or local cluster)..."
    
    # Для локального кластера
    sudo mkdir -p /data/mysql /data/app
    sudo chmod 755 /data/mysql /data/app
    
    echo "✅ Local directories created:"
    ls -la /data/
fi

echo "🎯 Storage setup completed!"
echo ""
echo "📝 Next steps:"
echo "1. Apply PV manifests: kubectl apply -f k8s/mysql-pv.yaml -f k8s/app-pv.yaml"
echo "2. Check PV status: kubectl get pv"
echo "3. Deploy applications with PVC"