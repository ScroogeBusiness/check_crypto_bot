from pyrogram import Client, filters
import re

print('[+] Bot Checks Crawler by @coder_pyua')
app = Client("check_bot", api_id=12735088, api_hash="367fbd3d9ce186f160eca00c8a1aa3b8")


@app.on_message(filters.text)
async def check_handler(client, message):
    if 'CryptoBot' in message.text:
        checks_id = re.findall(r"t\.me/CryptoBot\?start=(.*)", message.text)

        for check_id in checks_id:
            print(f'[+] Словили чек: {check_id}')
            await app.send_message("CryptoBot", f"/start {check_id}")
    elif message.via_bot != None and message.via_bot.username == 'CryptoBot':
        if 'Получить ' in message.reply_markup.inline_keyboard[0][0].text or 'Receive ' in message.reply_markup.inline_keyboard[0][0].text:
            check_id = message.reply_markup.inline_keyboard[0][0].url.split('=')[1]
            print(f'[+] Словили чек: {check_id}')
            await app.send_message("CryptoBot", f"/start {check_id}")

    elif 'tonRocketBot' in message.text:
        checks_id = re.findall(r"t\.me/tonRocketBot\?start=(.*)", message.text)

        for check_id in checks_id:
            print(f'[+] Словили чек: {check_id}')
            await app.send_message("tonRocketBot", f"/start {check_id}")
    elif message.via_bot != None and message.via_bot.username == 'tonRocketBot':
        if 'Получить ' in message.reply_markup.inline_keyboard[0][0].text or 'Receive ' in message.reply_markup.inline_keyboard[0][0].text:
            check_id = message.reply_markup.inline_keyboard[0][0].url.split('=')[1]
            print(f'[+] Словили чек: {check_id}')
            await app.send_message("tonRocketBot", f"/start {check_id}")

    elif 'wallet' in message.text:
        checks_id = re.findall(r"t\.me/wallet\?start=(.*)", message.text)

        for check_id in checks_id:
            print(f'[+] Словили чек: {check_id}')
            await app.send_message("wallet", f"/start {check_id}")
    elif message.via_bot != None and message.via_bot.username == 'wallet':
        if 'Получить: ' in message.reply_markup.inline_keyboard[0][0].text or 'Receive: ' in message.reply_markup.inline_keyboard[0][0].text:
            check_id = message.reply_markup.inline_keyboard[0][0].url.split('=')[1]
            print(f'[+] Словили чек: {check_id}')
            await app.send_message("wallet", f"/start {check_id}")

# To Do
# @app.on_message(filters.private & filters.text)
# async def cryptobot_handler(client, message):
#     if message.from_user.username == 'CryptoBot':
#         if 'Вы получили' in message.text:
#             print(message.text)

app.run()