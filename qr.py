import qrcode
# from PIL import Image

# data = "https://127.0.0.1:8000"

# qr = qrcode.QRCode()


image = qrcode.make("https://127.0.0.1:8000")
image.save("qr.png")

