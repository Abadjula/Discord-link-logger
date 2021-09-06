import discord
from colorama import Fore
import os
import shutil

def clear():
    if os.name == "nt":
        os.system("cls")
        os.system("title Discord Link Logger")
        os.system("mode 75, 25")
    else:
        os.system("clear")

clear()
width = shutil.get_terminal_size().columns

try:
    MessagePassId = int(input(f"[{Fore.RESET}{Fore.GREEN}MESSAGE PASS ROLE ID{Fore.RESET}] {Fore.LIGHTCYAN_EX}"))
    forbidden = [".gg/", "discord.com/invite/"]

    client = discord.Client()

    @client.event
    async def on_message(message):

        msg = message.content
        guild = message.guild
        author = message.author

        MessagePass = discord.utils.get(guild.roles, id=MessagePassId)

        for Item in forbidden:
            if MessagePass in author.roles:
                pass
            else:
                if Item in msg:
                    await message.delete()
                    print(f"{Fore.RESET}[{Fore.GREEN}{author.id}{Fore.RESET}] {Fore.LIGHTCYAN_EX}{author} Sent a Discord link")

    @client.event
    async def on_ready():
        clear()
        print(f"{Fore.RESET}{Fore.GREEN}Connected!".center(width))

    client.run("ODQxMDE1MDk4MTkzMjE1NTM4.YJgmWA.0NWJs8kd243AItqkauva06mOBIU")
except Exception as error:
    clear()
    print(f"{Fore.RESET}{Fore.LIGHTCYAN_EX}[{Fore.RESET}{Fore.RED}ERROR{Fore.RESET}{Fore.LIGHTCYAN_EX}] {Fore.RESET}{Fore.RED}{error} ")
    input(f"{Fore.RESET}\nPress Enter to Exit. . .")
