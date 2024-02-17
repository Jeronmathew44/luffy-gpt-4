# Copyright 2023 Qewertyy, MIT License

from pyrogram import Client, filters, types as t
from Utils import getText,ChatCompletion,getMedia,geminiVision

@Client.on_message(filters.command(["gpt","bard","llama","mistral","palm","gemini"]))
async def chatbots(_: Client,m: t.Message):
    prompt = getText(m)
    media = getMedia(m)
    if media is not None:
        return await askAboutImage(_,m,[media],prompt)
    if prompt is None:
        return await m.reply_text("Give An input !! ")
        await s.delete()
    text = m.text.split(" ", 1)[1]
    model = m.command[0].lower()
    output = await ChatCompletion(prompt,model)
    if model == "bard":
        output, images = output
        if len(images) == 0:
            return await m.reply_text(text=f"ʜᴇʏ {m.from_user.mention}\n ǫᴜᴇʀʏ ɪs:- {text}\n\nResults:\n\n{output}")
            await s.delete()
        media = []
        for i in images:
            media.append(t.InputMediaPhoto(i))
        media[0] = t.InputMediaPhoto(images[0],caption=output)
        await _.send_media_group(
            m.chat.id,
            media,
            reply_to_message_id=m.id
            )
        return
    s = await m.reply_sticker("CAACAgQAAxkBAAELHDhlmn1cxY6clm6BgZoURPY-xywq4gACbg8AAuHqsVDaMQeY6CcRojQE")
    ai_response = output['parts'][0]['text'] if model=="gemini" else output
    await m.reply_text(text=f"ʜᴇʏ {m.from_user.mention}\n ǫᴜᴇʀʏ ɪs:- {text}\n\nResults:\n\n{ai_response}")
    await s.delete()

async def askAboutImage(_:Client,m:t.Message,mediaFiles: list,prompt:str):
    images = []
    for media in mediaFiles:
        image = await _.download_media(media.file_id,file_name=f'./downloads/{m.from_user.id}_ask.jpg')
        images.append(image)
    output = await geminiVision(prompt if prompt else "whats this?","geminiVision",images)
    await m.reply_text(output)
