from PIL import Image, ImageDraw, ImageFont

image = Image.open("certi.jpg")
draw = ImageDraw.Draw(image)

# O bien /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif.ttf.

font = ImageFont.truetype("arial.ttf", 28)
draw.text((550, 390), "JUNIOR GROVER FLORES MARTINEZ ", font=font, fill="black")
image.save("salida.jpg")
