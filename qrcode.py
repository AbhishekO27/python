import qrcode
from PIL import Image
import qrcode.constants

qr= qrcode.QRcode( version= 1 , error.correction = qrcode.constants.ERROR_CORRECT_H, box_size=10,border=4)

qr.add_data("")
qr.make(fit=True)

img = qr.make_image(fill_color="blue",back_color="white")

img.save("geeks for geeks")

# comminting some changes 
