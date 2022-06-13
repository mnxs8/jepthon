"""
By Jepthon Team © 
Reda
"""
import os
from datetime import datetime
import speech_recognition as sr
from pydub import AudioSegment

from jepthon import jmthon
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import media_type

plugin_category = "utils"


@jmthon.ar_cmd(pattern="احجي(?:\s|$)([\s\S]*)",
               command=("احجي", plugin_category),
              )
async def _(event):
    "تحويل الكلام الى نص."
    
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    lan = input_str
    if not lan:
         return await edit_delete(event, "يجب ان تضع اختصار اللغة المطلوبة")
    

    if not os.path.isdir(Config.TEMP_DIR):
        os.makedirs(Config.TEMP_DIR)
    mediatype = media_type(reply)
    if not reply:
        return await edit_delete(
            event,
            "`قم بالرد على رسالة او مقطع صوتي لتحويله الى نص.`",
        )
    
    
    if mediatype is None:
         await edit_delete(event, "`**الملف الذي قمت بالرد عليه ليس بصمة صوتية**`")

    jepevent = await edit_or_reply(event, "`يجري تنزيل الملف...`")
    oggfi = await event.client.download_media(reply, Config.TEMP_DIR)
    await jepevent.edit("`يجري تحويل الكلام الى نص....`")
    r = sr.Recognizer()
 
    ogg = oggfi.removesuffix('.ogg')
   
    AudioSegment.from_file(oggfi).export(f"{ogg}.wav", format="wav")
    user_audio_file = sr.AudioFile(f"{ogg}.wav")
    with user_audio_file as source:
         audio = r.record(source)

    
    
    text = r.recognize_google(audio, language=str(lan))
    
    end = datetime.now()
    ms = (end - start).seconds
    
    string_to_show = "**النص : **`{}`".format(text)
    await jepevent.edit(string_to_show)
    
    os.remove(oggfi)
    os.remove(f"{ogg}.wav")
