import requests
import datetime
import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=os.environ.get('BOT_TOKEN'))
dp = Dispatcher(bot)
open_weather_token = os.environ.get('OPEN_WEATHER_TOKEN')

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Проивет! Напиши мне название города и я пришлю сводку погоды!")

@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
    "Clear": "Ясно \U00002600",
    "Clouds": "Облачно \U00002601",
    "Rain": "Дождь \U0001F327",
    "Drizzle": "Дождь \U0001F326",
    "Thunderstorm": "Гроза \U000026C8",
    "Snow": "Снег \U0001F328",
    "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&APPID={open_weather_token}&units=metric&lang=ru"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там"
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        await message.reply(
              f"Погода в городе: {city}\nТемпература: {cur_weather}С° {wd}\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\n"
              f"Восход солнца: {sunrise_timestamp}\nЗакат  солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
              f"Хорошего дня")


    except Exception as ex:
        await message.reply(ex)




if __name__ == '__main__':
    executor.start_polling(dp)