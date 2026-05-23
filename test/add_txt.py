from PIL import Image, ImageDraw, ImageFont
import os, traceback

def add_text_to_img():
    config = load_settings()
    image_path = config.get("input_path", "")
    print(f"불러온 설정값: {config}")
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)


    if not config:
        print("ERR, 설정 값이 없는뎁쇼?")
        input("\n프로그램이 종료되었습니다. 엔터를 누르면 창이 닫힙니다...")
        return

    draw.text(xy=(80.4, 79.4), text=config.get("chr_name", ""), font = font_0(36), fill = (255, 255, 255))
    draw.text(xy=(80.4, 160.8), text=config.get("title", ""), font = font_0(100.2), fill = (255, 255, 255), spacing = 25)
    draw.text(xy=(80.4, 415), text=config.get("bible", ""), font = font_1(72), fill = (255, 255, 255))
    draw.text(xy=(80.4, 523.2), text=config.get("preacher", ""), font = font_1(72), fill = (255, 255, 255))

    output_path = config.get("output_path", "")
    img.save(output_path)
    
    img.show()
    print("DONE!!")

def font_0(font_size):
    font_path = "../fonts/BMHANNA_11yrs_ttf.ttf"
    font_tag = ImageFont.truetype(font_path, font_size)
    return font_tag

def font_1(font_size):
    font_path = "../fonts/BMHANNAAir_ttf.ttf"
    font_tag = ImageFont.truetype(font_path, font_size)
    return font_tag

def load_settings():
    file_path = "../setting.txt"
    settings = {}
    if not os.path.exists(file_path): 
        print(f"ERR: {file_path} 파일 찾을 수 없음")
        input("\n프로그램이 종료되었습니다. 엔터를 누르면 창이 닫힙니다...")
        return settings

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#") or "=" not in line:
                continue

            key, val = line.split("=", 1)
            val = val.replace("\\n", "\n")
            settings[key.strip()] = val.strip()

    return settings

print("[백석새소망교회 썸네일 자동 제조기]")
add_text_to_img()
input("\n프로그램이 종료되었습니다. 엔터를 누르면 창이 닫힙니다...")