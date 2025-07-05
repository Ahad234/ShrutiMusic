import asyncio
from config import BOT_TOKEN, API_ID, API_HASH
from pyrogram import Client
from pyrogram.types import BotCommand

# ✅ Your bot commands
COMMANDS = [
    BotCommand("start", "🚀 Start bot"),
    BotCommand("help", "❓ Help menu"),
    BotCommand("ping", "📡 Ping and system stats"),
    BotCommand("play", "🎵 Start streaming the requested track"),
    BotCommand("vplay", "📹 Start video streaming"),
    BotCommand("playforce", "⚠️ Force play audio track"),
    BotCommand("vplayforce", "⚠️ Force play video track"),
    BotCommand("pause", "⏸ Pause the stream"),
    BotCommand("resume", "▶️ Resume the stream"),
    BotCommand("skip", "⏭ Skip the current track"),
    BotCommand("end", "🛑 End the stream"),
    BotCommand("stop", "🛑 Stop the stream"),
    BotCommand("player", "🎛 Get interactive player panel"),
    BotCommand("queue", "📄 Show track queue"),
    BotCommand("auth", "➕ Add a user to auth list"),
    BotCommand("unauth", "➖ Remove a user from auth list"),
    BotCommand("authusers", "👥 Show list of auth users"),
    BotCommand("cplay", "📻 Channel audio play"),
    BotCommand("cvplay", "📺 Channel video play"),
    BotCommand("cplayforce", "🚨 Channel force audio play"),
    BotCommand("cvplayforce", "🚨 Channel force video play"),
    BotCommand("channelplay", "🔗 Connect group to channel"),
    BotCommand("loop", "🔁 Enable/disable loop"),
    BotCommand("stats", "📊 Bot stats"),
    BotCommand("shuffle", "🔀 Shuffle the queue"),
    BotCommand("seek", "⏩ Seek forward"),
    BotCommand("seekback", "⏪ Seek backward"),
    BotCommand("song", "🎶 Download song (mp3/mp4)"),
    BotCommand("speed", "⏩ Adjust audio playback speed (group)"),
    BotCommand("cspeed", "⏩ Adjust audio speed (channel)"),
    BotCommand("tagall", "📢 Tag everyone"),
    BotCommand("admins", "🛡 Tag all admins"),
    BotCommand("tgm", "🖼 Convert image to URL"),
    BotCommand("vid", "🎞 Download video from social media"),
    BotCommand("dice", "🎲 Roll a dice"),
    BotCommand("ludo", "🎲 Play ludo"),
    BotCommand("dart", "🎯 Throw a dart"),
    BotCommand("basket", "🏀 Play basketball"),
    BotCommand("football", "⚽ Play football"),
    BotCommand("slot", "🎰 Play slot"),
    BotCommand("jackpot", "🎰 Play jackpot"),
    BotCommand("bowling", "🎳 Play bowling"),
    BotCommand("ban", "🚫 Ban a user"),
    BotCommand("banall", "⚠️ Ban all users"),
    BotCommand("sban", "🧹 Delete & ban user"),
    BotCommand("tban", "⏳ Temporary ban"),
    BotCommand("unban", "✅ Unban a user"),
    BotCommand("warn", "⚠️ Warn a user"),
    BotCommand("swarn", "🧹 Delete & warn user"),
    BotCommand("rmwarns", "🗑 Remove all warnings"),
    BotCommand("warns", "📋 Show user warnings"),
    BotCommand("kick", "👢 Kick user"),
    BotCommand("skick", "🧹 Delete msg & kick"),
    BotCommand("purge", "🧽 Purge messages"),
    BotCommand("del", "❌ Delete message"),
    BotCommand("promote", "⬆️ Promote member"),
    BotCommand("fullpromote", "🚀 Full promote"),
    BotCommand("demote", "⬇️ Demote member"),
    BotCommand("pin", "📌 Pin message"),
    BotCommand("unpin", "❎ Unpin message"),
    BotCommand("unpinall", "🧹 Unpin all"),
    BotCommand("mute", "🔇 Mute user"),
    BotCommand("tmute", "⏱ Temp mute"),
    BotCommand("unmute", "🔊 Unmute"),
    BotCommand("zombies", "💀 Ban deleted accounts"),
    BotCommand("report", "🚨 Report to admins")
]

BOT_BIO = "ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴄʜᴀɴɴᴇʟ\n➻ sᴜᴘᴘᴏʀᴛ - 🔹 @ShrutiBots 🔹"
BOT_ABOUT = "🎧 This is a Powerful Telegram Music Bot for Group and Channel Streaming.\n🔹 Support: @ShrutiBots"

async def setup_bot_once():
    try:
        async with Client("auto_profile", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH) as bot:
            me = await bot.get_me()
            await bot.set_bot_commands(COMMANDS)
            await bot.set_chat_description(me.id, BOT_BIO)
            await bot.set_chat_about(me.id, BOT_ABOUT)
            print("✅ Bot commands, bio, and about set successfully.")
    except Exception as e:
        print(f"❌ Error while setting bot profile: {e}")

# Run this only once when script starts
asyncio.get_event_loop().run_until_complete(setup_bot_once())
