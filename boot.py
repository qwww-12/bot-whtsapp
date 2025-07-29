import pywhatkit as kt
import time

def send_instant_message():
    try:
        print("\n--- Send Instant Message ---")
        phone = input("Enter phone number with country code (e.g. +212612345678): ").strip()
        message = input("Enter your message: ").strip()
        
        print("🚀 Launching WhatsApp Web...")
        kt.sendwhatmsg_instantly(
            phone_no=phone,
            message=message,
            wait_time=15,
            tab_close=False  # ما يسدش التاب
        )
        
        print("⏳ Waiting for message to be sent...")
        time.sleep(20)  # نعطي الوقت باش يتسيفط
        
        print("✅ Message should be sent! You can verify manually.")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def schedule_message():
    try:
        print("\n--- Schedule Message ---")
        phone = input("Enter phone number with country code: ").strip()
        message = input("Enter your message: ").strip()
        hour = int(input("Enter hour (24h format): "))
        minute = int(input("Enter minute: "))
        
        kt.sendwhatmsg(
            phone_no=phone,
            message=message,
            time_hour=hour,
            time_min=minute,
            wait_time=15,
            tab_close=False
        )
        
        print(f"⏳ Message scheduled for {hour:02d}:{minute:02d}")
        time.sleep(30)
        print("✅ Done.")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def send_group_message():
    try:
        print("\n--- Send Group Message ---")
        group_id = input("Enter group ID (from group invite link): ").strip()
        message = input("Enter your message: ").strip()
        
        print("🚀 Launching WhatsApp Web for group...")
        kt.sendwhatmsg_to_group_instantly(
            group_id=group_id,
            message=message,
            wait_time=15,
            tab_close=False
        )
        
        print("⏳ Waiting for group message to send...")
        time.sleep(20)
        print("✅ Group message should be sent!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def show_menu():
    while True:
        print("\n===== WhatsApp Bot =====")
        print("1. Send Instant Message")
        print("2. Schedule Message")
        print("3. Send Group Message")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            send_instant_message()
        elif choice == "2":
            schedule_message()
        elif choice == "3":
            send_group_message()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice, try again.")

if __name__ == "__main__":
    show_menu()
