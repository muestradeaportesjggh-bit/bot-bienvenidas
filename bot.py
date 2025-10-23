import telebot
import os

TOKEN = "8256194778:AAET_ebeOkFfHUMmjGK_6uZY_fjKPz9Jd1c"
bot = telebot.TeleBot(TOKEN)

@bot.chat_member_handler()
def manejar_miembros(m):
    user = m.new_chat_member.user
    
    if m.new_chat_member.status == "member":
        bot.send_message(m.chat.id, f"🎉 ¡Bienvenido/a {user.first_name} al grupo!")
        print(f"✅ {user.first_name} entró")
    
    elif m.new_chat_member.status == "left":
        bot.send_message(m.chat.id, f"👋 {user.first_name} ha salido del grupo")
        print(f"❌ {user.first_name} salió")

print("🤖 Bot ACTIVO 24/7")
bot.infinity_polling()
