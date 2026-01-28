import pyqrcode

url = input("Enter your url to generate qr code :")
name = input("File name : ")

qr_code = pyqrcode.create(url)
qr_code.svg(f"{name}.svg", scale=8)
