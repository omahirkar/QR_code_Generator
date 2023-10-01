#QR code generator
import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,  # QR code version (adjust as needed)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code
        border=4,  # Border size (adjust as needed)
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    data = input("Enter the data for the QR code: ")
    filename = input("Enter the filename for the QR code image (e.g., qr_code.png): ")

    generate_qr_code(data, filename)
    print(f"QR code saved as {filename}")
