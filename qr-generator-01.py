# Importing necessary libraries
import qrcode  # Library to create QR codes
import sys  # Library for system-specific parameters and functions

def generate_qr_code(url):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in pixels
        border=4,  # Width of the border (minimum is 4)
    )
    qr.add_data(url)  # Add the URL data to the QR code
    qr.make(fit=True)  # Generate the QR code

    # Create an image from the QR code instance
    img = qr.make_image(fill='black', back_color='white')  # Colors of the QR code

    # Save the image to a file
    img.save('qr_code.png')  # Save as qr_code.png
    print("QR code generated and saved as 'qr_code.png'")

if __name__ == "__main__":
    # Ask user for a URL
    url = input("Enter the URL to generate QR code: ")
    generate_qr_code(url)  # Generate QR code for the provided URL
