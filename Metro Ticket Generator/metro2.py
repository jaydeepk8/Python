import qrcode
import PIL.Image

# Generate the QR code
qr_code = qrcode.make("This is a QR code")

# Create a PIL image object from the QR code
qr_image = PIL.Image.open(qr_code.to_image())

# Display the image
qr_image.show()

# Display the output
print("The output is: This is a QR code")
