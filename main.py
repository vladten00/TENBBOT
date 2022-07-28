import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
TOKEN = '5405807626:AAGdmZVCFVfv9JJBRnTPx35VFFGbO4kRwBw'


def start(update, context):
    # посылает сообщение в ответ на команду /start
    update.message.reply_text('Привет, принцесса. Напиши /love или /confession')


def love(update, context):
    # посылает сообщение в ответ на команду /love
    update.message.reply_text('Я тебя тоже люблю. \U0001F600')


# для отладки
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


# to start the bot
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("love", love))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


def confession(update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='yes'),
         InlineKeyboardButton("No", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('do u love me?', reply_markup=reply_markup)


dp.add_handler(CommandHandler("confession", confession))


def confession_reply(update, context):
    query = update.callback_query
    if query.data == 'yes':
        context.bot.edit_message_text(chat_id=query.message.chat_id,
                                      message_id=query.message.message_id,
                                      text='\U0001F46B\U0001F49D', disable_web_page_preview=0)
    else:
        context.bot.edit_message_text(chat_id=query.message.chat_id,
                                      message_id=query.message.message_id,
                                      text='Пожалуйста, подумай еще раз  \U0001F624',
                                      disable_web_page_preview=0)


dp.add_handler(CallbackQueryHandler(confession_reply))