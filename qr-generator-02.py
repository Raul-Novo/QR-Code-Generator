# Importing necessary libraries
from PIL import Image, ImageDraw  # Library for creating and manipulating images
import random  # Library to generate random numbers

def generate_simple_qr(url):
    # Create a basic grid for the QR code (10x10 for simplicity)
    size = 10  # Size of the QR code grid
    grid = [[0 for _ in range(size)] for _ in range(size)]  # Initialize a 10x10 grid

    # Fill the grid with random black (1) or white (0) pixels based on the URL length
    for i in range(size):
        for j in range(size):
            grid[i][j] = 1 if (i + j + len(url)) % 2 == 0 else 0  # Simple pattern

    # Create an image from the grid
    img_size = size * 10  # Each grid box will be 10x10 pixels
    img = Image.new('1', (img_size, img_size), 1)  # Create a white image
    draw = ImageDraw.Draw(img)  # Prepare to draw on the image

    # Draw the grid
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 1:  # If the grid cell is 1, draw a black square
                draw.rectangle([j * 10, i * 10, (j + 1) * 10, (i + 1) * 10], fill=0)

    # Save the image
    img.save('simple_qr.png')  # Save as simple_qr.png
    print("Simplified QR code generated and saved as 'simple_qr.png'")

if __name__ == "__main__":
    # Ask user for a URL
    url = input("Enter the URL to generate a simple QR code: ")
    generate_simple_qr(url)  # Generate a simple QR code for the provided URL
