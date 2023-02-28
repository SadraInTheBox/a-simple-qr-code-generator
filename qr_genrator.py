import qrcode as qr

qr = qr.QRCode(
	version=1,
    error_correction=qr.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

def TextPut():
	text = ""
	print("type your text")
	while True:
		txt = str(input())
		if txt.lower() == "end":
			break
		else:
			text += txt
	return text

qr.add_data(TextPut())

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

path = input("type a path > ")

img.save(path)

print(f"QR code genrated!\n./{path} saved!")