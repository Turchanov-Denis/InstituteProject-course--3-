from PIL import Image, ImageDraw, ImageFont

def create_card(number):
    card_size = (100, 100)
    border_color = (0, 0, 255)
    text_color = (255, 0, 0)
    border_thickness = 5

    card = Image.new("RGB", card_size, "white")
    draw = ImageDraw.Draw(card)

    draw.rectangle(
        [border_thickness // 2, border_thickness // 2, 
         card_size[0] - border_thickness // 2, card_size[1] - border_thickness // 2],
        outline=border_color, width=border_thickness
    )

    font = ImageFont.load_default()
    text = str(number)
    bbox = draw.textbbox((0, 0), text, font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    text_position = ((card_size[0] - text_width) // 2, (card_size[1] - text_height) // 2)
    draw.text(text_position, text, fill=text_color, font=font)

    return card

for i in range(1, 4):
    card_image = create_card(i)
    card_image.show()
    card_image.save(f"card_{i}.png", "PNG")
