from xxlimited import foo

from PIL import Image, ImageDraw, ImageFont

def add_text_to_img():
    image_path = "img_0_non_txt.jpg"
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # 폰트 설정 필요
    font_path = "fonts/BMHANNA_11yrs_ttf.ttf"
    
    font_title_tag = ImageFont.truetype(font_path, 36)

    # 교회 이름
    draw.text(xy=(80.4, 79.4), text = "백석새소망교회 주일예배", font = font_title_tag, fill = (255, 255, 255))

    # output_path = "result_img.jpg"
    
    img.show()
    print("done")

add_text_to_img()