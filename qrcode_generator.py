import qrcode
import image

qr = qrcode.QRcode(
        version = 15,   # higher the number, qr code generated is bigger and more complicated
        box_size = 10,  # size of the box in which qr code is generated
        border = 5      # white space around the qr code on all 4 sides in the box
     )
data = input("Enter text/link to generate QR code")

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", back_color = "white")
img.save('demo.png')    # give full path for specific location
