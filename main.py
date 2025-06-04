import qrcode
from PIL import Image

def generate_qr_code(data, filename="qr_code.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    return filename

if __name__ == "__main__":
    print("Генератор QR-кодов")
    input_data = input("Введите текст или ссылку для кодирования в QR-код: ")
    output_filename = input("Введите имя файла для сохранения QR-кода (например, my_qr.png) или нажмите Enter для 'qr_code.png': ")

    if not output_filename:
        output_filename = "qr_code.png"
    elif not output_filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        output_filename += ".png"

    saved_file = generate_qr_code(input_data, output_filename)
    print(f"QR-код успешно создан и сохранен как '{saved_file}'")
