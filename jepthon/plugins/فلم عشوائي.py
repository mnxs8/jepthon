#Jepthon ©
#By Reda 
from imdb import Cinemagoer
import requests
from html_telegraph_poster.upload_images import upload_image
from random import randint
from jepthon import jmthon
import asyncio
from ..core.managers import edit_delete, edit_or_reply
ia = Cinemagoer()

@jmthon.ar_cmd(pattern="فلم")
async def rfilm(event):
    await event.edit("يرجى الانتضار جاري البحث على فلم...")
    for _ in range(100):
        movieID = randint(1,250)
        movieT = ia.get_top250_movies()

        movie = movieT[movieID]
        year = movie.get('year')
        rating = movie.get('rating', "لا يوجد")
        movien = movie.get('title')
        await jmthon.send_message(event.chat_id, str(movie.get('cover url')))
        moviep = movie.get('full-size cover url')
        if moviep is not None:
            moviep = upload_image(str(moviep)) 
        if moviep is None:
            moviep = f"https://telegra.ph/file/15480332b663adae49205.jpg"
        moviet = f"الاسم: {movien}\nالسنة: {year}\nالتقييم: {rating}"
        await event.delete()
        await jmthon.send_file(
                event.chat_id,
                moviep,
                caption=moviet,
                )
        break
