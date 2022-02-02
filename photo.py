import sys

from PIL import Image, ImageDraw, ImageFont
CHILD_W = CHILD_H =16
font_path ='C:\\Users\Chauncy ye\PycharmProjects\pythonProject\.font\song.ttc'
txt="我的心是可可的"
font = ImageFont.truetype(font_path, CHILD_W)

if __name__ =='__main__':
    print(sys.argv)
    imgSrc = Image.open("hanpi.jpg")
    w,h =imgSrc.size
    print(txt)
    imgChild = Image.new('RGB', (CHILD_W, CHILD_H))
    imgDst = Image.new("RGB", (CHILD_W*w, CHILD_H*h))


    textW,textH =font.getsize("米")
    print(textW,textH)
    offsetX = (CHILD_W - textW) >>2
    offsetY = (CHILD_H-textH)>>2

    charIndex =3
    draw = ImageDraw.Draw(imgChild)
    for y in range(h):
        for x in range(w):
            draw.rectangle((0, 0, CHILD_W, CHILD_H),fill= "gray")
            draw.text((offsetX, offsetY),txt[charIndex],font =font, fill= imgSrc.getpixel((x,y)))
            imgDst.paste(imgChild,(x*CHILD_W,y*CHILD_H))

            charIndex +=1
            if charIndex == len(txt):
                charIndex = -1

    imgDst.save("laohanpi2.jpg")
    print("ok")
