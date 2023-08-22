
# JOHANs SELFBOT | Version 1.1 | Developed by J0HAN

import discord, asyncio, random, time, base64, string
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

def convert(tme):
    pos = ["s","m","h","d"]

    dct = {"s" : 1, "m" : 60, "h" : 3600, "d": 3600*24}

    unt = tme[-1]

    if unt not in pos:
        return -1
    try:
        val = int(tme[:-1])
    except:
        return -2

    return val * dct[unt]

class client(discord.Client):
    async def on_ready(self):
        print(f"{dec}\n▼ User: {bot.user}")

    async def on_message(self, message):
        if message.author != bot.user:
            return
        
        msg = message.content
        ctx = message.channel

        async def delete(itm):
            await itm.delete()

        async def info1(trgt):
            print(f"{dft}\nUser Info — Target: {trgt}")
            crtn = str(trgt.created_at).split(" ")
            flgs = trgt.public_flags.all()
            if str(flgs) != "[]":
                bdgs = 0
                for flg in flgs:
                    if bdgs > 0:
                        bdg = bdg + ", " + (str(flg).replace("UserFlags.", "").replace("_", " ").title())
                    else:
                        bdg = str(flg).replace("UserFlags.", "").replace("_", " ").title()
                        bdgs += 1
            else:
                bdg = "No badges to display."
            print(f"{scs}► Info successfully fetched!")
            await ctx.send(f"""```USER INFO
▸ Username
{trgt.display_name} | @{trgt} ({trgt.id})
▸ Creation Date
{crtn[0]} (YEAR-MN-DY)
▸ Other
Bot: {str(trgt.bot)} | System: {str(trgt.system)}
▸ Badges
{bdg}```""")
        async def info2(trgt):
            print(f"{dft}\nServer Info — Target: {trgt}")
            await ctx.send(f"""```SERVER INFO
▸ Name
{trgt.name} ({trgt.id})
```""")

        async def avatar(trgt):
            print(f"{dft}\nAvatar — Target: {trgt}")
            await ctx.send(trgt.avatar)
            print(f"{scs}► Avatar has been fetched!")

        async def grab(trgtID):
            print(f"{dft}\nGrab — Target: {trgtID}")
            a = str(trgtID).encode("ascii")
            b = base64.b64encode(a)
            c = b.decode("ascii")
            x = c.replace("==", "")
            y = "".join(random.choices(string.ascii_letters, k=5))
            z = "".join(random.choices(string.ascii_letters, k=38))
            ftkn = x + "." + y + "." + z
            try:
                tmp = await message.reply("```Connecting over TCP handshake...```")
                await asyncio.sleep(1.5) # Set to 0 for instant
                await tmp.delete()
                tmp = await message.reply("```Connection established, scraping through LAN network...```")
                await asyncio.sleep(2) # Set to 0 for instant
                await tmp.delete()
                await message.reply(f"```Found & fetched target token: {ftkn}```")
                print(f"{scs}► Token successfully fetched and sent!")
            except:
                print(f"{wrn}► Unable to send grab message(s).")

        async def spam(amt, mde, ntce):
            print(f"{dft}\nSpam — Amount: {amt} | Mode: {mde} | Message: {ntce}")
            msgs = 0
            strt = time.time()
            while msgs < amt:
                try:
                    await ctx.send(ntce)
                    if mde == 2:
                        msgs += 1
                        print(f"{scs}► Delayed spam has been sent! ({msgs}/{amt})")
                        await asyncio.sleep(0.1)
                    else:
                        msgs += 1
                        print(f"{scs}► Spam has been sent! ({msgs}/{amt})")
                except:
                    print(f"{wrn}► Unable to send spam message.")
            print(f"{dft}Spam — Finished | Took {time.time()-strt}s")

        async def ghost(amt, ntce):
            print(f"{dft}\nGhost — Amount: {amt} | Message: {ntce}")
            msgs = 0
            strt = time.time()
            while msgs < amt:
                ghst = await ctx.send(ntce)
                msgs += 1
                print(f"{scs}► Message has been sent! ({msgs}/{amt})")
                loop = asyncio.get_event_loop()
                loop.create_task(delete(ghst))
                print(f"{scs}► It has also been deleted!")
            print(f"{dft}Ghost — Finished | Took {time.time()-strt}s")

        async def rape():
            print(f"{dft}\nRape — Message: W.I.P.")
            strt = time.time()
            async for m in ctx.history():
                if m.author == bot.user:
                    try: # Close this so invisible message doesn't take up your entire screen
                        await m.edit("""⠀













































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































⠀""")
                        print(f"{scs}► Message has been edited!")
                    except:
                        print(f"{wrn}► Message unable to be edited.")
            print(f"{dft}Rape — Finished | Took {time.time()-strt}s")

        async def purge(amt, mde, trgt):
            print(f"{dft}\nPurge — Amount: {amt} | Mode: {mde} | Target: {trgt if mde == 3 else bot.user if mde == 2 else 'None'}")
            msgs = 0
            strt = time.time()
            async for m in ctx.history():
                if msgs < amt:
                    if mde == 3 and m.author == trgt:
                        try:
                            await m.delete()
                            msgs += 1
                            print(f"{scs}► Message has been deleted! ({msgs}/{amt})")
                        except:
                            print(f"{wrn}► Message unable to be deleted.")
                    elif mde == 2 and m.author == bot.user:
                        try:
                            await m.delete()
                            msgs += 1
                            print(f"{scs}► Message has been deleted! ({msgs}/{amt})")
                        except:
                            print(f"{wrn}► Message unable to be deleted.")
                    elif mde == 1:
                        try:
                            await m.delete()
                            msgs += 1
                            print(f"{scs}► Message has been deleted! ({msgs}/{amt})")
                        except:
                            print(f"{wrn}► Message unable to be deleted.")
            if msgs == 0:
                print(f"{wrn}► No messages were found for deletion.")
            print(f"{dft}Purge — Finished | Took {time.time()-strt}s")

        async def remove(amt):
            print(f"{dft}\nRemove — Amount: {amt}")
            msgs = 0
            strt = time.time()
            async for m in ctx.history():
                if msgs < amt:
                    if m.author == bot.user:
                        try:
                            await m.edit("[REMOVED]")
                            msgs += 1
                            print(f"{scs}► Message has been removed! ({msgs}/{amt})")
                        except:
                            print(f"{wrn}► Message unable to be removed.")
            print(f"{dft}Remove — Finished | Took {time.time()-strt}s")

        async def roll(mx):
            print(f"{dft}\nRoll — Max: {mx}")
            x = str(random.randint(1, mx))
            print(f"{scs}► Rolled a {x} successfully!")
            await message.reply(f"```You have rolled a {x}!```")
            
        async def flip():
            print(f"{dft}\nFlip — Rigged: W.I.P.")
            if random.randint(1, 2) == 1:
                await message.reply(f"```You flipped a coin and it landed on heads!```")
            else:
                await message.reply(f"```You flipped a coin and it landed on tails!```")
            print(f"{scs}► Message with result has been sent!")
        
        async def giveaway(lgnth):
            print(f"{dft}\nGiveaway — Length: {lgnth}s")
            gvwy = await ctx.send(f"```React to this message to enter a giveaway! Lasts for only {lgnth}s!```")
            await gvwy.add_reaction("🎉")
            print(f"{scs}► Giveaway with reaction has been sent! Now waiting {lgnth}s...")
            await asyncio.sleep(lgnth)
            try:
                entrs = await gvwy.reactions[0].users().flatten()
                print(f"{scs}► Giveaway has now ended with the entrees recorded!")
                wnr = random.choice(entrs)
                await gvwy.reply(f"Congratulations, {wnr.mention}, for winning the giveaway!")
            except:
                await gvwy.reply("```Looks like no one entered the giveaway...```")

        if msg.startswith(f"{prfx}help"):
            await message.reply(f"""```COMMANDS
▸ {prfx}who [target]
Fetches some simple info about a user
▸ {prfx}what
Fetches some simple info about the server you sent the command in
▸ {prfx}pfp [target]
Fetches the avatar of a user
▸ {prfx}spam [amount] [mode(1/2)] [message]
Sends a specified amount of messages in either normal mode (1) or delayed mode (2)
▸ {prfx}ghst [amount] [message]
Sends a message and then deletes it after
▸ {prfx}rape
Edits all your messages in the channel you sent the command in to be a large, invisible message.
▸ {prfx}del [amount] [mode(1/2/3)] [target*]
Deletes a specified amount of messages, 1 for all, 2 for self, 3 for a target user's
▸ {prfx}x [amount]
Edits a specified amount of messages to be '[REMOVED]'
▸ {prfx}roll [max]
Rolls a number between one and the specified max
▸ {prfx}flip
Flips a coin and returns either heads or tails
▸ {prfx}give [length(s/m/h/d)]
Creates a giveaway that users can enter by reacting to your message

*This parameter is only required if you pick mode 3```""")
        
        if msg.startswith(f"{prfx}who"):
            cmdI = msg.split(" ")
            if len(cmdI) > 1:
                try:
                    if cmdI[1].startswith("<@"):
                        a = cmdI[1].replace("<@", "")
                        trgtID = int(a.replace(">", ""))
                    else:
                        trgtID = int(cmdI[1])
                    await message.delete()
                    trgt = await bot.fetch_user(trgtID)
                    await info1(trgt)
                    print(f"{scs}► User info has been sent!")
                except:
                    await message.reply("An exception has been raised.")
            else:
                await message.reply("Please enter in a target.")

        if msg.startswith(f"{prfx}what"):
            try:
                await message.delete()
                trgt = await bot.fetch_guild(ctx.guild.id)
                await info2(trgt)
                print(f"{scs}► Server info has been sent!")
            except:
                await message.reply("An exception has been raised.")

        elif msg.startswith(f"{prfx}pfp"):
            cmdA = msg.split(" ")
            if len(cmdA) > 1:
                try:
                    if cmdA[1].startswith("<@"):
                        a = cmdA[1].replace("<@", "")
                        trgtID = int(a.replace(">", ""))
                    else:
                        trgtID = int(cmdA[1])
                    await message.delete()
                    trgt = await bot.fetch_user(trgtID)
                    await avatar(trgt)
                    print(f"{scs}► Avatar has been sent!")
                except:
                    await message.reply("An exception has been raised.")
            else:
                await message.reply("Please enter in a target.")

        elif msg.startswith(f"{prfx}grab"):
            cmdG = msg.split(" ")
            if len(cmdG) > 1:
                try:
                    if cmdG[1].startswith("<@"):
                        a = cmdG[1].replace("<@", "")
                        trgtID = int(a.replace(">", ""))
                    else:
                        trgtID = int(cmdG[1])
                    await grab(trgtID)
                    await message.delete()
                except:
                    await message.reply("An exception has been raised.")
            else:
                await message.reply("Please enter in an user ID.")

        elif msg.startswith(f"{prfx}spam"):
            cmdS = msg.split(" ", 3)
            if len(cmdS) > 3:
                try:
                    amt = int(cmdS[1])
                    mde = int(cmdS[2])
                    await message.delete()
                    await spam(amt, mde, cmdS[3])
                except:
                    await message.reply("An exception has been raised.")
            else:
                await message.reply("Please enter in all required parameters.")

        elif msg.startswith(f"{prfx}ghst"):
            cmdG1 = msg.split(" ", 2)
            if len(cmdG1) > 2:
                try:
                    amt = int(cmdG1[1])
                    await message.delete()
                    await ghost(amt, cmdG1[2])
                except:
                    await message.reply("An exception has been raised.")
            else:
                await message.reply("Please enter in all required parameters.")

        elif msg.startswith(f"{prfx}rape"):
            try:
                await message.delete()
                await rape()
            except:
                await message.reply("An exception has been raised.")

        elif msg.startswith(f"{prfx}del"):
            cmdP = msg.split(" ", 3)
            if len(cmdP) > 2:
                try:
                    amt = int(cmdP[1])
                    mde = int(cmdP[2])
                    trgt = await bot.fetch_user(trgtID) if mde == 3 else None
                    await message.delete()
                    await purge(amt, mde, trgt)
                except:
                    await message.reply("An exception has been raised.")
            else:
                await message.reply("Please enter in all required parameters.")
        
        elif msg.startswith(f"{prfx}x"):
            cmdX = msg.split(" ")
            if len(cmdX) > 1:
                try:
                    amt = int(cmdX[1])
                    await message.delete()
                    await remove(amt)
                except:
                    await message.reply("An exception has been raised.")
            else:
                await message.reply("Please enter in an amount.")

        elif msg.startswith(f"{prfx}roll"):
            cmdR = msg.split(" ")
            if len(cmdR) > 1:
                try:
                    mx = int(cmdR[1]) if int(cmdR[1]) > 0 else 1
                    await message.delete()
                    await roll(mx)
                except:
                    await message.reply("An exception has been raised.")
            else:
                await message.reply("Please enter in a max amount.")

        elif msg.startswith(f"{prfx}flip"):
            try:
                await flip()
            except:
                await message.reply("An exception has been raised.")
        
        elif msg.startswith(f"{prfx}give"):
            cmdG2 = msg.split(" ")
            if len(cmdG2) > 1:
                try:
                    lgnth = convert(cmdG2[1])
                    if lgnth == -1:
                        await message.reply(f"Make sure you use the proper units or (s/m/h/d) next time.")
                        raise
                    elif lgnth == -2:
                        await message.reply(f"The time can only be an integer.")
                        raise
                    await message.delete()
                    await giveaway(lgnth)
                except:
                    await message.reply("An exception has been raised.")
            else:
                await message.reply("Please enter in a max amount of winners, put 0 for infinite.")

bot = client()
try:
    bot.run(tkn)
except:
    print(f"{err}INVALID TOKEN GIVEN\n{dft}")
