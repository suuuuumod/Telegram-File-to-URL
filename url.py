from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = 'YOUR_ACTUAL_BOT_TOKEN'  # Замените на токен вашего бота

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Пришли мне файл, и я пришлю тебе прямую ссылку для скачивания.')

def handle_docs(update: Update, context: CallbackContext) -> None:
    document = update.message.document
    new_file = context.bot.get_file(document.file_id)

    file_direct_link = new_file.file_path
    update.message.reply_text(f'Ваша ссылка для скачивания файла: {file_direct_link}')

def main():
    updater = Updater(token=TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.document, handle_docs))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
