# Very simple Telegram Bot #

This is very simple bot I've made to try out Python, aiogram and docker

## Running ##

You can use followinmg command to start this container.
You will need to provide your telegram bot token, and [OpenWeather](https://openweathermap.org) token

```console
docker run \
  --env BOT_TOKEN='telegram_token' \
  --env OPEN_WEATHER_TOKEN='open_weather_token' \
  esungurov/tbot:latest
```