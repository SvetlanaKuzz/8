from PIL import Image, ImageDraw, ImageFont
import random

cards = {
    "день рождения": "др.jpg",
    "новый год": "нг.jpg",
    "8 марта": "8марта.jpg",
    "23 февраля": "23.jpg"
}
a = input("К какому празднику Вам нужна открытка?: ")
if a.lower() in cards:
    card_name = cards[a.lower()]
    card_im = Image.open(card_name)
else:
    print("Не найдено открытки к данному празднику")
#запоминаем размер открытки
w, h = card_im.size
name = input("Кого вы хотите поздравить?: ")
#рандом цвета
b = random.randint(0, 256)
c = random.randint(0, 256)
d = random.randint(0, 256)
#рандом расположения (сверху или снизу открытки)
y = [0, 1800]
y1 = random.choice(y)
#рандом шрифта
v = ["arial.ttf", "ariblk.ttf"]
v1 = random.choice(v)
font = ImageFont.truetype(f"{v1}", 80)
txt = ImageDraw.Draw(card_im)
name_text = f"{name}, поздравляю!"
#определение ширины и высоты области для текста
_, _, w1, h1 = txt.textbbox((0, y1), name_text, font=font)
#центрирование текста
txt.text(((w - w1) / 2, y1), name_text, (b, c, d), font=font)
card_im.show()
card_im.save("card1.png")