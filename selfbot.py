import selfcord, random, asyncio, base64, string
from colorama import Fore as F

try:
    dft = F.RESET
    err = F.RED
    wrn = F.YELLOW
    scs = F.GREEN
    dec = F.LIGHTBLUE_EX
    otr = F.CYAN
except:
    print("Make sure you have colorama installed!\n")
    exit()

try:
    with open("setup.txt") as f:
        tkn = f.readline()
        prfx = f.readline()
except:
    print(f"{err}UNABLE TO LOCATE 'setup.txt' FILE\n{dft}")
    exit()

class client(selfcord.Client):
    async def on_ready(self):
        print(f"{dec}\n▼ User: {self.user}")
        await bot.change_presence(activity=selfcord.Activity(type=selfcord.ActivityType.playing, name="with JSB"))

    async def on_message(self, message):
        if message.author != self.user:
            return
        msg = message.content
        ctx = message.channel
        nrd_on = False
        if nrd_on == True and message.author == nrd_trgt:
            await message.add_reaction(emoji="🤓")
        async def remove(itm):
            try:
                await itm.delete()
                print(f"{scs}► It has also been deleted!")
            except:
                print(f"{wrn}► Unable to delete it though.")

        if msg.startswith(f"{prfx}help"):
            await message.reply("Too lazy lol")
        
        if msg.startswith(f"{prfx}info"):
            cmdI = msg.split(" ")
            if len(cmdI) > 1:
                if len(cmdI[1]) > 17:
                    try:
                        if cmdI[1].startswith("<@"):
                            a = cmdI[1].replace("<@", "")
                            trgtID = int(a.replace(">", ""))
                        else:
                            trgtID = int(cmdI[1])
                        trgt = await bot.fetch_user(trgtID)
                        print(f"{dft}\nTarget: {trgt}")
                        trgt_dsply = trgt.display_name
                        trgt_crtnDte = trgt.created_at
                        trgt_dteCrtd = str(trgt_crtnDte).split(" ")
                        trgt_flgs = trgt.public_flags.all()
                        if str(trgt_flgs) != "[]":
                            bdgs = 0
                            for flg in trgt_flgs:
                                if bdgs > 0:
                                    trgt_bdgs = trgt_bdgs + ", " + (str(flg).replace("UserFlags.", "").replace("_", " ").title())
                                else:
                                    trgt_bdgs = str(flg).replace("UserFlags.", "").replace("_", " ").title()
                                bdgs += 1
                        else:
                            trgt_bdgs = "No badges to display."
                        print(f"{scs}Info successfully fetched!")
                        await ctx.send(f"""## Basic Account Information
▸ **📄 Username:**
{trgt_dsply} | {trgt} ({trgtID})
▸ **🛠️ Creation Date:**
{trgt_dteCrtd[0]} (YEAR-MN-DY) | {trgt_dteCrtd[1]}
▸ **🏅 Badges:**
{trgt_bdgs}""")
                        await message.delete()
                    except:
                        await message.reply("An exception has been raised.")
                else:
                    await message.reply("Invalid user has been given.")
            else:
                await message.reply("Please put in a target.")

        elif msg.startswith(f"{prfx}avatar"):
            cmdA = msg.split(" ")
            if len(cmdA) > 1:
                try:
                    if cmdA[1].startswith("<@"):
                        a = cmdA[1].replace("<@", "")
                        trgtID = int(a.replace(">", ""))
                    else:
                        trgtID = int(cmdA[1])
                    trgt = await bot.fetch_user(trgtID)
                    print(f"{dft}\nTarget: {trgt}")
                    trgt_pfp = trgt.avatar
                    await message.delete()
                    await ctx.send(trgt_pfp)
                    print(f"{scs}► Message has been sent!")
                    await message.delete()
                except:
                    await message.reply("An exception occurred.")
            else:
                await message.reply("Please enter in a target.")

        elif msg.startswith(f"{prfx}ghost"):
            cmdG = msg.split(" ", 2)
            if len(cmdG) > 2:
                try:
                    amt = int(cmdG[1])
                    msgs = 0
                    print(f"{dft}\nAmount: {amt} | Message: {cmdG[2]}")
                    await message.delete()
                    while msgs < amt:
                        ghst = await ctx.send(cmdG[2])
                        msgs += 1
                        print(f"{scs}► Message has been sent!")
                        loop = asyncio.get_event_loop()
                        loop.create_task(remove(ghst))
                except:
                    await message.reply("An exception was raised.")
            else:
                await message.reply("Please enter all required arguments.")
        
        elif msg.startswith(f"{prfx}nerd"):
            cmdN = msg.split(" ")
            if len(cmdN) > 1:
                try:
                    await message.delete()
                    if cmdN[1].startswith("<@"):
                        a = cmdN[1].replace("<@", "")
                        nrd_trgtID = a.replace(">", "")
                    else:
                        nrd_trgtID = cmdN[1]
                    nrd_trgt = await bot.fetch_user(nrd_trgtID)
                    print(f"{dft}\nTarget: {nrd_trgt}")
                    if nrd_on == False:
                        nrd_on = True
                        print(f"{scs}► Auto nerd react enabled!")
                    else:
                        nrd_on = False
                        print(f"{wrn}► Auto nerd react disabled.")
                except:
                    await message.reply("An exception has happened.")
            else:
                await message.reply("Please enter in a target.")
            

bot = client()
try:
    bot.run(tkn)
except:
    print(f"{err}INVALID TOKEN GIVEN\n")