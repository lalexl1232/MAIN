import socket
from PIL import Image, ImageFilter
import io

def render_image(image_data):
    print("Entering render_image")
    image = Image.open(io.BytesIO(image_data))
    rendered_image = image.filter(ImageFilter.GaussianBlur(10))
    buffer = io.BytesIO()
    rendered_image.save(buffer, format='PNG')
    return buffer.getvalue(), rendered_image

def connect_to_server(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Получаем изображение от сервера
    image_data = b''
    while True:
        print("Receiving data...")
        chunk = client_socket.recv(512)
        if b'EOF' in chunk:
            image_data += chunk.replace(b'EOF', b'')
            print("No more data received.")
            break
        image_data += chunk

    print("Data received, length:", len(image_data))

    render_data, rendered_image = render_image(image_data)

    client_socket.sendall(render_data)
    client_socket.sendall(b'EOF')
    client_socket.close()

    rendered_image.show()
    print("Rendered image displayed.")


connect_to_server('127.0.0.1', 9999)
