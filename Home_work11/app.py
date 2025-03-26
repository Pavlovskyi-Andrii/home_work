from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)
CSV_FILE = "users.csv"

# Инициализация CSV файла
def init_csv_file():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "name", "surname", "age"])

# Чтение пользователей из CSV
def read_users():
    init_csv_file()
    users = []
    with open(CSV_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        users = list(reader)
    return users

# Запись пользователей в CSV
def write_users(users):
    init_csv_file()
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'name', 'surname', 'age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)

# Генерация нового уникального ID
def generate_new_id(users):
    if not users:
        return '1'
    # Находим максимальный существующий ID и увеличиваем его
    max_id = max(int(user['id']) for user in users)
    return str(max_id + 1)

@app.route("/")
def home():
    return "Hello, Flask!"

# --- Получить всех пользователей ---
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(read_users())

# --- Получить пользователя по ID ---
@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    users = read_users()
    user = next((u for u in users if u["id"] == id), None)
    return jsonify(user) if user else ("User not found", 404)

# --- Добавить нового пользователя ---
@app.route("/users", methods=["POST"])
def create_user():
    users = read_users()
    data = request.json

    # Проверка наличия обязательных полей
    if not all(key in data for key in ["name", "surname", "age"]):
        return jsonify({"error": "Missing name, surname, or age"}), 400

    # Генерация нового уникального ID
    new_id = generate_new_id(users)

    new_user = {
        "id": new_id,
        "name": data["name"],
        "surname": data["surname"],
        "age": data["age"]
    }

    users.append(new_user)
    write_users(users)
    return jsonify(new_user), 201

# --- Обновить пользователя (PUT) ---
@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    users = read_users()
    data = request.json

    for user in users:
        if user["id"] == id:
            # Обновляем все поля
            user.update({
                "name": data.get("name", user["name"]),
                "surname": data.get("surname", user["surname"]),
                "age": data.get("age", user["age"])
            })
            write_users(users)
            return jsonify(user)

    return jsonify({"error": "User not found"}), 404

# --- Частичное обновление (PATCH) ---
@app.route("/users/<id>", methods=["PATCH"])
def patch_user(id):
    users = read_users()
    data = request.json

    for user in users:
        if user["id"] == id:
            # Обновляем только указанные поля
            for key, value in data.items():
                if value is not None:
                    user[key] = value
            write_users(users)
            return jsonify(user)

    return jsonify({"error": "User not found"}), 404

# --- Удалить пользователя ---
@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    users = read_users()
    
    # Находим пользователя для удаления
    user_to_delete = next((u for u in users if u["id"] == id), None)
    
    if not user_to_delete:
        return jsonify({"error": "User not found"}), 404

    # Удаляем пользователя
    users = [u for u in users if u["id"] != id]
    
    # Перезаписываем файл без удаленного пользователя
    write_users(users)
    return jsonify({"message": "User deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)



# from flask import Flask, request, jsonify
# import csv
# import os

# app = Flask(__name__)
# CSV_FILE = "users.csv"

# # Если файла нет, создаём его с заголовками
# if not os.path.exists(CSV_FILE):
#     with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(["id", "name", "surname", "age"])

# # Чтение пользователей из CSV
# def read_users():
#     users = []
#     if os.path.exists(CSV_FILE):
#         with open(CSV_FILE, newline="", encoding="utf-8") as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 users.append(row)
#     return users

# # Запись пользователей в CSV
# def write_users(users):
#     # Use the fieldnames that match the actual keys in your user dictionaries
#     fieldnames = ['id', 'name', 'surname', 'age']
    
#     with open(CSV_FILE, 'a', newline='', encoding='utf-8') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(users)


# @app.route("/")
# def home():
#     return "Hello, Flask!"

# # --- Получить всех пользователей ---
# @app.route("/users", methods=["GET"])
# def get_users():
#     return jsonify(read_users())

# # --- Получить пользователя по ID ---
# @app.route("/users/<id>", methods=["GET"])
# def get_user(id):
#     users = read_users()
#     user = next((u for u in users if u["id"] == id), None)
#     return jsonify(user) if user else ("User not found", 404)

# # --- Добавить нового пользователя ---
# @app.route("/users", methods=["POST"])
# def create_user():
#     users = read_users()
#     data = request.json  # Используем request.json, а не requests.json

#     if "name" not in data or "surname" not in data or "age" not in data:
#         return jsonify({"error": "Missing name, surname, or age"}), 400

#     new_user = {
#         "id": str(len(users) + 1),
#         "name": data["name"],
#         "surname": data["surname"],
#         "age": data["age"]
#     }

#     users.append(new_user)
#     write_users(users)
#     return jsonify(new_user), 201

# # --- Обновить пользователя (PUT) ---
# @app.route("/users/<id>", methods=["PUT"])
# def update_user(id):
#     users = read_users()
#     data = request.json

#     for user in users:
#         if user["id"] == id:
#             user.update(data)
#             write_users(users)
#             return jsonify(user)

#     return jsonify({"error": "User not found"}), 404

# # --- Частичное обновление (PATCH) ---
# @app.route("/users/<id>", methods=["PATCH"])
# def patch_user(id):
#     users = read_users()
#     data = request.json

#     for user in users:
#         if user["id"] == id:
#             user.update({k: v for k, v in data.items() if v})
#             write_users(users)
#             return jsonify(user)

#     return jsonify({"error": "User not found"}), 404

# # --- Удалить пользователя ---
# @app.route("/users/<id>", methods=["DELETE"])
# def delete_user(id):
#     users = read_users()
#     new_users = [u for u in users if u["id"] != id]

#     if len(users) == len(new_users):
#         return jsonify({"error": "User not found"}), 404

#     write_users(new_users)
#     return jsonify({"message": "User deleted"}), 200

# if __name__ == "__main__":
#     app.run(debug=True)
