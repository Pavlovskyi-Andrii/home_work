import requests
import sys

# URL вашего локального сервера
BASE_URL = "http://localhost:5000/users"

def log_result(message, file_path='results.txt'):
    """Логирование результатов в консоль и файл"""
    print(message)
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(message + '\n')

def test_rest_api():
    # Открываем файл результатов в режиме перезаписи
    open('results.txt', 'w').close()

    # 1. Retrieve all existing students (GET)
    log_result("\n1. Получение всех существующих пользователей:")
    response = requests.get(BASE_URL)
    log_result(f"Статус: {response.status_code}")
    log_result(f"Пользователи: {response.json()}")

    # 2. Create three students (POST)
    students = [
        {"name": "John", "surname": "Doe", "age": "25"},
        {"name": "Jane", "surname": "Smith", "age": "30"},
        {"name": "Mike", "surname": "Johnson", "age": "35"}
    ]

    created_students = []
    log_result("\n2. Создание трех пользователей:")
    for student in students:
        response = requests.post(BASE_URL, json=student)
        log_result(f"Создан пользователь: {response.json()}")
        created_students.append(response.json())

    # 3. Retrieve information about all existing students (GET)
    log_result("\n3. Получение всех пользователей после создания:")
    response = requests.get(BASE_URL)
    log_result(f"Статус: {response.status_code}")
    log_result(f"Пользователи: {response.json()}")

    # 4. Update the age of the second student (PATCH)
    second_student_id = created_students[1]['id']
    log_result(f"\n4. Обновление возраста второго пользователя (ID: {second_student_id}):")
    patch_data = {"age": "31"}
    response = requests.patch(f"{BASE_URL}/{second_student_id}", json=patch_data)
    log_result(f"Обновленный пользователь: {response.json()}")

    # 5. Retrieve information about the second student (GET)
    log_result(f"\n5. Получение информации о втором пользователе (ID: {second_student_id}):")
    response = requests.get(f"{BASE_URL}/{second_student_id}")
    log_result(f"Пользователь: {response.json()}")

    # 6. Update the first name, last name and the age of the third student (PUT)
    third_student_id = created_students[2]['id']
    log_result(f"\n6. Полное обновление третьего пользователя (ID: {third_student_id}):")
    put_data = {"name": "Michael", "surname": "Brown", "age": "40"}
    response = requests.put(f"{BASE_URL}/{third_student_id}", json=put_data)
    log_result(f"Обновленный пользователь: {response.json()}")

    # 7. Retrieve information about the third student (GET)
    log_result(f"\n7. Получение информации о третьем пользователе (ID: {third_student_id}):")
    response = requests.get(f"{BASE_URL}/{third_student_id}")
    log_result(f"Пользователь: {response.json()}")

    # 8. Retrieve all existing students (GET)
    log_result("\n8. Получение всех пользователей:")
    response = requests.get(BASE_URL)
    log_result(f"Статус: {response.status_code}")
    log_result(f"Пользователи: {response.json()}")

    # 9. Delete the first user (DELETE)
    first_student_id = created_students[0]['id']
    log_result(f"\n9. Удаление первого пользователя (ID: {first_student_id}):")
    response = requests.delete(f"{BASE_URL}/{first_student_id}")
    log_result(f"Результат удаления: {response.json()}")

    # 10. Retrieve all existing students (GET)
    log_result("\n10. Получение всех пользователей после удаления:")
    response = requests.get(BASE_URL)
    log_result(f"Статус: {response.status_code}")
    log_result(f"Пользователи: {response.json()}")

if __name__ == "__main__":
    test_rest_api()