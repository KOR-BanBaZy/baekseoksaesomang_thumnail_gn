from PIL import Image, ImageDraw, ImageFont

chr_name = "백석새소망교회 주일예배"
title = "주님을 향한\n우리의 열심"
bible = "로마서 땡땡 땡땡절"
pastor = "김보현 담임목사"

def add_text_to_img():
    image_path = "img_0_non_txt.jpg"
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    draw.text(xy=(80.4, 79.4), text = chr_name, font = font_0(36), fill = (255, 255, 255))
    draw.text(xy=(80.4, 160.8), text = title, font = font_0(100.2), fill = (255, 255, 255))
    draw.text(xy=(80.4, 415), text = bible, font = font_1(72), fill = (255, 255, 255))
    draw.text(xy=(80.4, 523.2), text = pastor, font = font_1(72), fill = (255, 255, 255))

    # output_path = "result_img.jpg"
    
    img.show()
    print("done")

def font_0(font_size):
    font_path = "fonts/BMHANNA_11yrs_ttf.ttf"
    font_tag = ImageFont.truetype(font_path, font_size)
    return font_tag

def font_1(font_size):
    font_path = "fonts/BMHANNAAir_ttf.ttf"
    font_tag = ImageFont.truetype(font_path, font_size)
    return font_tag

add_text_to_img()