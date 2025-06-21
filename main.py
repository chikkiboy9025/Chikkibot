from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.input_stream import InputAudioStream
import yt_dlp

api_id = 20955666
api_hash = "a5eba0f71ecf9340a52f4a41dfc89e3f"
bot_token = "7047292032:AAHk6v5BLpTzPgd0qjFHPpt6KY5lXaVf6ms"
session = "BQE_whIAxYjjMmzzQC8JNVFefDIR-PUS8Cak4a4EqmgQ_htG6QIuw1zixeeiYfr7vnZ5Au1F6635RU8U67J_QJa_tXlwo5_pVZmf4FtwJLMO6rva9aR4dh7V467r8MDcqxoyNKJ3g_eErpKOl_WsV5ctnUxbweqnwBO5OjF9V07Te4TJEfpU55E-R25Kcq80Vzy9uS3Z7HZ9PPL6K87fP2rMGGk1Ti1JLX3S2Z-takrvT0-pD1g--GMK_hJf0sJyvza2LvKg7qqr4NuA2mPT6F29PLHddj15DPqDn74-MACgMDDJaT5ExL1oLaT0gWGrK8-CE4pJCzbRpaW1Yq-FlrI2hcwAAAGyPxo3AA"

# Assistant Client (Userbot)
app = Client(session, api_id=api_id, api_hash=api_hash)

# Bot Client
bot = Client("MusicBot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# VC using Assistant
vc = PyTgCalls(app)

@bot.on_message(filters.command("play") & filters.private)
async def play_audio(client, message):
    query = " ".join(message.command[1:])
    ydl_opts = {'format': 'bestaudio'}
    info = yt_dlp.YoutubeDL(ydl_opts).extract_info(f"ytsearch:{query}", download=False)['entries'][0]
    url = info['url']

    await vc.join_group_call(
        message.chat.id,
        InputAudioStream(
            url,
        ),
    )
    await message.reply_text(f"Playing: {info['title']}")

# Start both assistant and bot
app.start()
bot.run()
