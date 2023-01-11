import qrcode
import image
qr=qrcode.QRCode(
    version =20,
    box_size= 12,
    border = 1,

)
data="https://www.youtube.com/watch?v=dQw4w9WgXcQ"

qr.add_data(data)
img = qr.make_image(back_color="aqua")
img.save("QR.png")