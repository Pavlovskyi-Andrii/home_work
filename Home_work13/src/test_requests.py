import requests
import sys


BASE_URL = "http://localhost:5000/users"

def log_result(message, file_path='results.txt'):
    """Логирование результатов в консоль и файл"""
    print(message)
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(message + '\n')

def test_rest_api():
    
    open('results.txt', 'w').close()

    # 1. Retrieve all existing students (GET)
    log_result("\n1. Отримання всіх існуючих користувачів:")
    response = requests.get(BASE_URL)
    log_result(f"Статус: {response.status_code}")
    log_result(f"Пользователи: {response.json()}")

    # 2. Create three students (POST)
    students = [
        {"name": "name111", "surname": "surname111", "age": "age111"},
        {"name": "name222", "surname": "surname222", "age": "age222"},
        {"name": "name333", "surname": "surname333", "age": "age333"}
    ]

    created_students = []
    log_result("\n2. Створення трьох користувачів:")
    for student in students:
        response = requests.post(BASE_URL, json=student)
        log_result(f"Створено користувач: {response.json()}")
        created_students.append(response.json())

    # 3. Retrieve information about all existing students (GET)
    log_result("\n3. Отримання всіх користувачів після створення:")
    response = requests.get(BASE_URL)
    log_result(f"Статус: {response.status_code}")
    log_result(f"Користувачі: {response.json()}")

    # 4. Update the age of the second student (PATCH)
    second_student_id = created_students[1]['id']
    log_result(f"Статус: {response.status_code}")
    log_result(f"\n4. Оновлення віку другого користувача(ID: {second_student_id}):")
    patch_data = {"age": "31"}
    response = requests.patch(f"{BASE_URL}/{second_student_id}", json=patch_data)
    log_result(f"Оновлений користувач: {response.json()}")

    # 5. Retrieve information about the second student (GET)
    log_result(f"Статус: {response.status_code}")
    log_result(f"\n5. Отримання інформації про другого користувача(ID: {second_student_id}):")
    response = requests.get(f"{BASE_URL}/{second_student_id}")
    log_result(f"Користувач: {response.json()}")

    # 6. Update the first name, last name and the age of the third student (PUT)
    third_student_id = created_students[2]['id']
    log_result(f"\n6. Повне оновлення третього користувача(ID: {third_student_id}):")
    put_data = {"name": "Suichael", "surname": "Brown", "age": "50"}
    response = requests.put(f"{BASE_URL}/{third_student_id}", json=put_data)
    log_result(f"Оновлений користувач: {response.json()}")
    log_result(f"Статус: {response.status_code}")

    # 7. Retrieve information about the third student (GET)
    log_result(f"\n7. Отримання інформації про третього користувача(ID: {third_student_id}):")
    response = requests.get(f"{BASE_URL}/{third_student_id}")
    log_result(f"Користувач: {response.json()}")

    # 8. Retrieve all existing students (GET)
    log_result("\n8. Отримання всіх користувачів:")
    response = requests.get(BASE_URL)
    log_result(f"Статус: {response.status_code}")
    log_result(f"Пользователи: {response.json()}")

    # 9. Delete the first user (DELETE)
    first_student_id = created_students[0]['id']
    log_result(f"\n9. Видалення першого користувача(ID: {first_student_id}):")
    response = requests.delete(f"{BASE_URL}/{first_student_id}")
    log_result(f"Результат видалення:{response.json()}")

    # 10. Retrieve all existing students (GET)
    log_result("\n10. Отримання всіх користувачів після видалення:")
    response = requests.get(BASE_URL)
    log_result(f"Статус: {response.status_code}")
    log_result(f"Користувачі: {response.json()}")

if __name__ == "__main__":
    test_rest_api()