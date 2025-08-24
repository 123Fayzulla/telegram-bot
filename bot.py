from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text(
        "👋 Welcome.\n\n"
        "Your request delivered❗️ Our assistants will answer as soon as possible✅️"
    )

def help(update, context):
    update.message.reply_text(
        "If you need something, contact with @p_e_r_s_o_n_a_g_e"
    )

updater = Updater("8438539305:AAFazukQSk8YJcti1LnoikIOpXUvZ5OgkaE", use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))

updater.start_polling()
updater.idle()
