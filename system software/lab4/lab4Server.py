import socket
from PIL import Image
import io
import sqlite3 as sql


# Настройка первой базы данных для хранения путей исходных изображений
def setup_database():
    con = sql.connect('data.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS images (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(255)
                );''')
    con.commit()
    cur.close()
    con.close()


def insert_db():
    con = sql.connect('data.db')
    cur = con.cursor()
    cur.execute('''INSERT INTO images (name) VALUES
                    ('/Users/lalexl/Documents/spo_afon/lab1/image_to_render1.png'),
                    ('/Users/lalexl/Documents/spo_afon/lab1/image_to_render2.png'),
                    ('/Users/lalexl/Documents/spo_afon/lab1/image_to_render3.png'),
                    ('/Users/lalexl/Documents/spo_afon/lab1/image_to_render4.png'),
                    ('/Users/lalexl/Documents/spo_afon/lab1/image_to_render5.png'),
                    ('/Users/lalexl/Documents/spo_afon/lab1/image_to_render6.png'),
                    ('/Users/lalexl/Documents/spo_afon/lab1/image_to_render7.png');   
                ''')
    con.commit()
    cur.close()
    con.close()


def get_random_image_path():
    con = sql.connect('data.db')
    cur = con.cursor()
    cur.execute('SELECT name FROM images ORDER BY RANDOM() LIMIT 1;')
    image_path = cur.fetchone()[0]
    cur.close()
    con.close()
    return image_path


# Настройка второй базы данных для хранения путей отрендеренных изображений
def setup_rendered_database():
    con = sql.connect('rendered_data.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS rendered_images (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(255)
                );''')
    con.commit()
    cur.close()
    con.close()


def save_rendered_image_to_db(image_path):
    con = sql.connect('rendered_data.db')
    cur = con.cursor()
    cur.execute('INSERT INTO rendered_images (name) VALUES (?);', (image_path,))
    con.commit()
    cur.close()
    con.close()


def create_image():
    image_path = get_random_image_path()
    image = Image.open(image_path)
    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    print(f"Image {image_path} created and saved to buffer.")
    return buffer.getvalue()


def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        print("Waiting for a connection...")
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        # Отправляем изображение клиенту
        image_data = create_image()
        print(f"Sending image data of size {len(image_data)} bytes to client.")
        client_socket.sendall(image_data)
        client_socket.sendall(b'EOF')  # Отправляем метку окончания передачи данных
        print("Image data sent to client.")

        # Получаем обработанное изображение от клиента
        render_data = b''
        while True:
            print("Receiving rendered data from client...")
            chunk = client_socket.recv(512)
            if b'EOF' in chunk:
                render_data += chunk.replace(b'EOF', b'')  # Убираем метку окончания
                print("No more data from client.")
                break
            render_data += chunk
            print(f"Received chunk of size {len(chunk)} bytes from client.")

        # Обрабатываем полученное изображение (например, сохраняем его)
        print("Processing received rendered image...")
        received_image = Image.open(io.BytesIO(render_data))
        rendered_image_path = "received_image.png"
        received_image.save(rendered_image_path)
        print("Received rendered image saved.")

        # Сохраняем путь к отрендеренному изображению в базу данных
        save_rendered_image_to_db('/Users/lalexl/Documents/spo_afon/lab1/' + rendered_image_path)
        print("Rendered image path saved to database.")

        client_socket.close()
        print("Client connection closed.")


setup_database()
insert_db()
setup_rendered_database()
start_server('127.0.0.1', 9999)
