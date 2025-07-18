
import asyncio
import websockets

# اطلاعات روم
ROOM_ID = "ec567b4662aeec03b5095109baa516b2ec205559a7317e8254c8d4bb858a8855"
ROOM_TOKEN = "660e6448818d797101c5d230&invite_id=683a0084e81a61a989705c89"
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
