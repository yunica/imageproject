from PIL import Image, ImageDraw, ImageFont

image = Image.open("certi3.jpg")
draw = ImageDraw.Draw(image)

# O bien /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif.ttf.
#841.89 595.28 a4
# 65/325
font = ImageFont.truetype("arial.ttf", 28)
draw.text((65, 295), "JUNIOR GROVER FLORES MARTINEZ ", font=font, fill="black")
image.save("salida.jpg")
