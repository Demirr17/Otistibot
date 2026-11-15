import discord
import pyttsx3
import requests
from discord.ext import commands
intents=discord.Intents.default()
intents.message_content=True
bot=commands.Bot(command_prefix="?",intents=intents)
@bot.command()
async def start(ctx):
    await ctx.send("Merhaba Bot başlatılıyor,komutlara bakmak için ?list yazın!")
def get_weather(city):
    url=f"https://wttr.in/{city}?format=%C+%t"
    response=requests.get(url)
    if response.status_code==200:
        return response.text.strip()
    else:
        return"Hava durumu bilgilerine ulaşılamadı,lütfen tekrar deneyiniz."
def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
@bot.command()
async def weather(ctx,*,city):
    weather_info=get_weather(city)
    await ctx.send(weather_info)
    speak(weather_info)
bot.run("Token buraya")
