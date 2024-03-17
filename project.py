# Importing Required Modules
import pyqrcode

url=input("enter url to generate qr code: ")
qr_code=pyqrcode.create(url)
qr_code.svg('qr_code1.svg',scale=5)

print("QrCode generated")
