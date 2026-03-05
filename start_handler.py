from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode

# URL твоего мини-приложения
WEBAPP_URL = "https://vavilonpenis.github.io/название-репозитория"  # замени на свой URL

def get_start_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🛍 Открыть Маркет",
                web_app={"url": WEBAPP_URL},
                icon_custom_emoji_id="6032644646587338669"  # 🎁 Подарок
            )
        ],
        [
            InlineKeyboardButton(
                text="💎 NFT Коллекция",
                web_app={"url": WEBAPP_URL + "?tab=profile"},
                icon_custom_emoji_id="5904462880941545555"  # 🪙 Деньги
            ),
            InlineKeyboardButton(
                text="⭐ Stars",
                web_app={"url": WEBAPP_URL + "?tab=stars"},
                icon_custom_emoji_id="5870930636742595124"  # 📊 График
            )
        ],
        [
            InlineKeyboardButton(
                text="💬 Поддержка",
                url="https://t.me/AstralGiftsSup",
                icon_custom_emoji_id="5870753782874246579"  # ✍ Писать
            )
        ]
    ])


START_TEXT = """<b><tg-emoji emoji-id="5873147866364514353">🏘</tg-emoji> Добро пожаловать, {first_name}!</b>

<tg-emoji emoji-id="5870657884844462243">❌</tg-emoji> <b>Важно:</b> Мини-приложение может не работать без VPN. Для стабильного доступа используйте VPN-соединение.

Это официальный бот <b>AstralGifts</b> — маркетплейс Telegram подарков.

Здесь ты можешь:
<tg-emoji emoji-id="5904462880941545555">🪙</tg-emoji> Покупать и продавать NFT‑подарки и Stars
<tg-emoji emoji-id="6032644646587338669">🎁</tg-emoji> Получать и отправлять подарки пользователям
<tg-emoji emoji-id="5884479287171485878">📦</tg-emoji> Управлять своей коллекцией в удобном интерфейсе

<tg-emoji emoji-id="6037249452824072506">🔒</tg-emoji> <b>Безопасность и скорость:</b>
Все сделки проходят в блокчейне <b>TON</b> — надёжно и моментально.

<tg-emoji emoji-id="5769126056262898415">👛</tg-emoji> Подключи TON кошелёк и начни торговать прямо сейчас!

<tg-emoji emoji-id="5893057118545646106">📰</tg-emoji> Нажми кнопку ниже, чтобы открыть Маркет:"""


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        START_TEXT.format(first_name=message.from_user.first_name),
        parse_mode=ParseMode.HTML,
        reply_markup=get_start_keyboard()
    )
