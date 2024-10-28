from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
background_path = "image.png"
logo_path = "logo.png"
output_path = Path(background_path).with_name("watermarked_image.jpg")

background = Image.open(background_path)
watermark = Image.new("RGBA", background.size)

draw = ImageDraw.Draw(watermark)

font_size = 40
font = ImageFont.load_default()
text = "MRRRRRR"

bbox = draw.textbbox((0, 0), text, font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

text_position = ((background.width - text_width) - 20, background.height - text_height - 20)
draw.text(text_position, text, font=font, fill=(255, 255, 255, 128))

logo = Image.open(logo_path).convert("RGBA")
logo = logo.resize((300, 300))

logo_position = ((background.width - logo.width) -20, text_position[1] - logo.height - 10)
watermark.paste(logo, logo_position, logo)

watermarked_image = Image.alpha_composite(background.convert("RGBA"), watermark)
watermarked_image.convert("RGB").save(output_path, "JPEG")
watermarked_image.show()
