import os
import telebot
from dotenv import load_dotenv
from goldhand import *

load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")


# tradingView data
tw = Tw()

ticker = "BTC-USD"
t = GoldHand(ticker)
fig = t.plotly_last_year(tw.get_plotly_title(ticker))

# Címek és Emoji hozzáadása
fig.update_layout(
    xaxis_title="Date 🗓️",
    yaxis_title="Price (USD) 💵",
    template="plotly_white",  # sötét háttér, változtathatod
    width=1000,  # szélesség beállítása
    height=600,  # magasság beállítása
)

# A grafikon mentése PNG formátumban
fig.write_image("static_plot.png")



bot = telebot.TeleBot(BOT_TOKEN)

bot.send_photo(CHAT_ID, photo=open('static_plot.png', 'rb'))

