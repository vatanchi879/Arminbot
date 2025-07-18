
import asyncio
import websockets

# اطلاعات روم
ROOM_ID = "your_room_id_here"
ROOM_TOKEN = "your_room_token_here"
ADMINS = ["AdminUser1"]

# ایموت تستی
EMOTES = {
    1: "dab",
    2: "dance",
    3: "fairytwirl"
}

# تابع اصلی (تست لوپ ساده برای اجرای ایموت)
async def run_bot():
    while True:
        print("🤖 Bot is running... (replace with actual WebSocket logic)")
        await asyncio.sleep(10)  # شبیه‌سازی فعالیت دوره‌ای

# شروع اجرای بات
if __name__ == "__main__":
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        print("🛑 Bot stopped.")
