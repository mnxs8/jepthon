
import os
import asyncio
from datetime import datetime

from jepthon import CMD_HELP, jmthon
from . import hmention, reply_id
from ..sql_helper.globals import gvarstatus
plugin_category = "tools"


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
    jmthon_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    JEP_TXT = gvarstatus("ALIVE_TEXT") or "**[ 𝗜 𝗝𝘂𝘀𝘁 𝗔𝘀𝗸𝗲𝗱 𝗙𝗼𝗿 𝗦𝗼𝗺𝗲 𝗣𝗲𝗮𝗰𝗲 🎀 ](t.me/Jepthon)**"
    PING_PIC = gvarstatus("PING_PIC") or Config.P_PIC
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✇ ◅"
    caption = jmthon_caption.format(
        PING_TEXT=PING_TEXT,
        EMOJI=EMOJI,
        ping=ms,
    )
    if PING_PIC:
        RR7 = [x for x in PING_PIC.split()]
        PIC = random.choice(RR7)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                event,
                f"**الميـديا خـطأ **\nغـير الرابـط بأستـخدام الأمـر  \n `.اضف_فار ALIVE_PIC رابط صورتك`\n\n**لا يمـكن الحـصول عـلى صـورة من الـرابـط :-** `{PIC}`",
            )
    else:
        await edit_or_reply(
            event,
            caption,
        )

temp = """{PING_TEXT}
**{EMOJI} البنك ↜ :** `{ping}`"""
#======================================================================================================================================
CMD_HELP.update(
    {
        "البنك":".بنك\nجرب الامر بنفسك" 
        }
        )
