from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img =  Image.open("poster.png")
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("font/DroidSansMono.ttf", 30)

# box start point 'X' axis = 747
# box end point   = 1284
# box max character count = 25
# boxes middle 'Y' axis point = 670 , 807, 946, 1084, 1224
name = "MD Tanzim Khan Shanto"
print(len(name))
#draw.text((741, 670), " "*((25-len(name))//2)+name, (0, 0, 0), font=font)
draw.text((747, 670), "a"*30, (255,0,0), font=font)
#img.save(f"Generated Poster/{name}.png")
img.show()