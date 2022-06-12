
import os
import asyncio
from datetime import datetime

from jepthon import CMD_HELP, jmthon
from . import hmention, reply_id
from ..sql_helper.globals import gvarstatus
plugin_category = "tools"

JEP_TXT = gvarstatus("ALIVE_TEXT") or "**[ 𝗜 𝗝𝘂𝘀𝘁 𝗔𝘀𝗸𝗲𝗱 𝗙𝗼𝗿 𝗦𝗼𝗺𝗲 𝗣𝗲𝗮𝗰𝗲 🎀 ](t.me/Jepthon)**"
PING_PIC = gvarstatus("PING_PIC") or Config.P_PIC


@jmthon.ar_cmd(
    pattern="بنك$",
    command=("بنك", plugin_category),
    info={
        "header": "امر تجربه البوت اذا يشتغل ارسل  .بنك فقط",
        "option": "امر بنك المتطور كتابة  @RR7PP",
        "usage": ["{tr}البنك", ],
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    start = datetime.now()
    cat = await edit_or_reply(event, "<b><i>   البــــنك...  </b></i>", "html")
    end = datetime.now()
    await cat.delete()
    ms = (end - start).microseconds / 1000
    if PING_PIC:
        caption = f"<b><i>{JEP_TXT}<i><b>\n<code>┏━━━━━━━┓\n┃ ✦ {ms}\n┃ ✦ <b>{hmention}</b>\n┗━━━━━━━┛"
        await event.client.send_file(
            event.chat_id,
            PING_PIC,
            caption=caption,
            parse_mode="html",
            reply_to=reply_to_id,
            link_preview=False,
            allow_cache=True,
        )
    else:
        await event.edit_or_reply(event, "<code>يجـب اضـافة متـغير `PING_PIC`  اولا  f<code>", "html")

#======================================================================================================================================
CMD_HELP.update(
    {
        "البنك":".بنك\nجرب الامر بنفسك" 
        }
        )
