Перші 2 пункта завдання я вже зробив . перевір чи все вірно , і давай ідти далі :
1. Creating a simple application

●      Use Python programming language to create a simple web application with MySQL database

●      Create a Dockerfile to build a container image of your application.

Note: You can use this application. Link: 

https://gitlab.com/dan-it/groups/devops_soft/-/tree/main/forStep4?ref_type=heads

2. Setting up a Kubernetes Cluster

●      MiniKube:

○      Install MiniKube on your local machine to create a single-node Kubernetes cluster.

○      Start the cluster using minikube start.

●      Kubernetes Configuration Files:

○      Create YAML files to define your application's deployment, service, and other resources.

3. Deploying the Application

●      Use kubectl to apply your YAML files to the Kubernetes cluster.

●      Check the status of your deployment and service using kubectl get pods and kubectl get services.

4. Integrating with GitLab

●      Configure GitLab CI/CD to automatically build, test, and deploy your application to Kubernetes.

●      Create a GitLab CI/CD pipeline using a .gitlab-ci.yml file.

5. Persistent Volumes

●      Create a persistent volume claim (PVC) to request storage for your application.

●      Create a persistent volume (PV) to provision storage for the PVC.

●      Mount the PV to your application's pod.



файли чи скріншоти які будуть потрібні для перевірки цого проекту (домашнього завдання) я їх буду робити сам : папка screens в ній будуть лежати скріни виконнаня коду , Скріни перевірки статусу итд.

1. Код власноствореної апки на Пайтоні, яка працює з базою даних MySQL (або взяти готову за посиланням, й переробити в разі необхідності). Апка повинна бути з тестами.

2. Код Dockerfile для імеджа з апкою

3. Код власного кластера (MiniKube або Kind)

4. Код всіх необхідних маніфестів

5. Скріни підняття кластера й аплая маніфестів (як що вручну, перед пайплайном)

6. Скріни перевірки статусу

7. Скрін ~/.kube/config, де вказані IP адреса кластера

8. Скріни підняття власного GitLab CE (встановити на віртуалку, або підняти в Docker)

9. Скріни підключення GitLab Docker runner

10. Скрін змінних GitLab проекту (Settings - CI/CD - Variables)

11. Скріни змінних оточення (які передаютьсяв апку (DB_HOST)

12. Код пайплайну(.gitlab-ci.yml)

13. Код PVC й PV

14. Скріни підключення PV

15. Скріни роботи пайплайну

16. Скріни роботи апки (При пуші в репозиторій повинен запуститись пайплайн

17. Скріни подів (2 з апкою й одна з MySQL)

18. Скріни бази даних, яка залищається на хості, після видалення кластера (опціонально)
Не изменяй файлы в папке tests ,  templates, src\static а также файлы app.py 