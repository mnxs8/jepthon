import os

import subprocess

from datetime import datetime

import speech_recognition as sr




from gtts import gTTS


from pydub import AudioSegment

from jepthon import jmthon


from ..helpers import media_type

from ..core.managers import edit_delete, edit_or_reply

from . import deEmojify, reply_id







@jmthon.ar_cmd(pattern="تكلم(?:\s|$)([\s\S]*)")

async def _(event):

    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str

    elif "|" in input_str:
        lan, text = input_str.split("|")

    else:

        await edit_or_reply(event, "- هذا نص غير صحيح")
        return
        text = text.strip()
        lan = lan.strip()

    jepthonevent = await edit_or_reply(event, "⌔∮ جـار التسجيل انتـظر قليلا")


    if not os.path.isdir("./temp/"):

        os.makedirs("./temp/")

    required_file_name = "./temp/" + "voice.ogg"

    try:

        tts = gTTS(text, lang=lan)
        tts.save(required_file_name)
        command_to_execute = [
            "ffmpeg",
            "-i",
             required_file_name,
             "-map",
             "0:a",
             "-codec:a",
             "libopus",
             "-b:a",
             "100k",
             "-vbr",
             "on",
             required_file_name + ".opus"
        ]
        
        try:

            t_response = subprocess.check_output(

                command_to_execute, stderr=subprocess.STDOUT

            )

        except (subprocess.CalledProcessError, NameError, FileNotFoundError) as exc:

            await jepthonevent.edit(str(exc))

        else:

            os.remove(required_file_name)

            required_file_name = required_file_name + ".opus"

        end = datetime.now()

        ms = (end - start).seconds

        await event.client.send_file(

            event.chat_id,

            required_file_name,

            reply_to=event.message.reply_to_msg_id,

            allow_cache=False,

            voice_note=True,

        )

        os.remove(required_file_name)

        await edit_delete(

            jepthonevent,

            "تحويل النص {} الى مقطع صوتي في {} ثواني ".format(text[0:20], ms),

        )

    except Exception as e:

        await edit_or_reply(jepthonevent, f"خطأ:\n{e}")

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
    
    string_to_show = text
    await jepevent.edit(string_to_show)
    
    os.remove(oggfi)
    os.remove(f"{ogg}.wav")
