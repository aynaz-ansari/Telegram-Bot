from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes
TOKEN = ''#tokenbot
BOT_USERNAME = '@Usernamebot'

async def start_command (update : Update , context : ContextTypes.DEFAULT_TYPE):
  user = update.effective_user
  await update.message.reply_text(f"سلام{user.first_name or ''} به کانال کدزنی با آیناز خوش آمدید.")

async def help_command (update : Update , context : ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text('من یک ربات برای آموزش زبان برنامه نویسی پایتون هست.')

async def custom_command (update : Update , context : ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text(' این یک دستور سفارشی است.')


def handel_response(text: str):
  if not text:
    return "کاربر گرامی ،پیامی دریافت نشد."
  user_text = text.lower()
  if "سلام" in user_text:
    return " سلام "
  if "hello" in user_text:
    return "hello"
  if "پایتون چیست؟" in user_text:
    return "پایتون یک زبان برنامه نویسی سطح بالا و شی گرا است که توسط Guido van Rossum توسعه یافته است."

  if "what is python?" in user_text:
    return "Python is a versatile, high-level, object-oriented programming language known for its simple and readable syntax, making it a popular choice for beginners and experienced developers."

  return" پیام شما را متوجه نشدم!"

async def handel_message (update : Update , context : ContextTypes.DEFAULT_TYPE):
  if not update.message or not update.message.text :
    return
  message = update.message
  text = message.text
  chat_type = message.chat.type

  print(f"user : {message.chat.id} , chat type : {chat_type}")

  if chat_type in ("group" , "supergroup"):
    if (BOT_USERNAME in text.lower()):
      t = text.replace(BOT_USERNAME , ' ').strip()
      respose = handel_response(t)
    else:
      return
  else:
    respose = handel_response(text)

  await message.reply_text(respose)

async def error(update : Update , context : ContextTypes.DEFAULT_TYPE):
  print(f'update : {error} cause error: {context.error}')

if __name__ == "__main__":
    print("bot is strarting...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start" , start_command))
    app.add_handler(CommandHandler("help" , help_command))
    app.add_handler(CommandHandler("custom" , custom_command))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND ,handel_message))

    app.add_error_handler(error)

    print("polling")

    app.run_polling(poll_interval=3)


