import qrcode
from PIL import Image

data = "https://www.youtube.com"

img = qrcode.make(data)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

qr_img = qr.make_image(fill="black", back_color="red")
qr_img.save("qrcode.png")
qr_img.show()