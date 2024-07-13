from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

filial = "Filial 📍"
start = "Start ✅"
admin = "Admin 👨🏻‍💻"
newpost = "NewsPost"


def start_btn():
    rmk = ReplyKeyboardBuilder()
    design = [
        KeyboardButton(text=filial),
        KeyboardButton(text=start),
        KeyboardButton(text=admin),
        KeyboardButton(text=newpost)
    ]
    rmk.add(*design)
    rmk.adjust(2 , 1)
    return rmk.as_markup(resize_keyboard=True)

women = "Woman 🧍‍♀️"
men = "Men 🧍‍♂️"
back = "🔙 back"


def men_women():
    rmk = ReplyKeyboardBuilder()
    design = [
        KeyboardButton(text=women),
        KeyboardButton(text=men),
        KeyboardButton(text=back)
    ]
    rmk.add(*design)
    rmk.adjust(2 , 1)
    return rmk.as_markup(resize_keyboard=True)


oy1 = "1-oy"
oy2 = "2-oy"
oy3 = "3-oy"
oy4 = "4-oy"


def month_men():
    rmk = ReplyKeyboardBuilder()
    design = [
        KeyboardButton(text=oy1),
        KeyboardButton(text=oy2),
        KeyboardButton(text=oy3),
        KeyboardButton(text=oy4),
        KeyboardButton(text=back)
    ]
    rmk.add(*design)
    rmk.adjust(2 , repeat=True)
    return rmk.as_markup(resize_keyboard=True)


def month_women():
    rmk = ReplyKeyboardBuilder()
    design = [
        KeyboardButton(text=oy1),
        KeyboardButton(text=oy2),
        KeyboardButton(text=oy3),
        KeyboardButton(text=oy4),
        KeyboardButton(text=back)
    ]
    rmk.add(*design)
    rmk.adjust(2 , repeat=True)
    return rmk.as_markup(resize_keyboard=True)


dushanba = "dushanba"
seshanba = "seshanba"
chorshanba = "chorshanba"
juma = "juma"
shanba = "shanba"
yakshanba = "yakshanba"


def hafta_kn():
    rmk = ReplyKeyboardBuilder()
    design = [
        KeyboardButton(text=dushanba),
        KeyboardButton(text=seshanba),
        KeyboardButton(text=chorshanba),
        KeyboardButton(text=juma),
        KeyboardButton(text=shanba),
        KeyboardButton(text=yakshanba)
    ]
    rmk.add(*design)
    rmk.adjust(3 , repeat=True)
    return rmk.as_markup(resize_keyboard=True)