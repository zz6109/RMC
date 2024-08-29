from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '7305722961:AAEoDHBK9noJNbgd4wCFufuJlLgBZWWWCeA'
BOT_USERNAME: Final = '@machine_ctl_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):	# 입력 할수 있는 커맨드 설정(비동기 함수로 선언)
	await update.message.reply_text('Hello! Master')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('option index 1. /start 2. /help 3. /toggle_power')

async def toggle_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('custom')

# responses

def handle_response(text: str)-> str:	
	processed: str = text.lower()

	if 'hello' in text:
		return '1'
	return 'iput again'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):	# 입력 메세지 처리 함수(비동기)
	message_type: str = update.message.chat.type
	text: str = update.message.text

	print(f'User ({update.message.caht.id}) in {message_type}: "{text}"')

	print('Bot:', response)
	await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):		# 에러 처리함수(비동기)
	print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
	print('Starting bot..')
	app = Application.builder().token(TOKEN).build()
	
	# commands
	app.add_handler(CommandHandler('start', start_command))
	app.add_handler(CommandHandler('help', help_command))
	app.add_handler(CommandHandler('toggle', toggle_command))
	
	# Messages
	# app.add_handler(CommandHandler(filters.TEXT, handle_massge))

	# Errors
	app.add_error_handler(error)
		
	#Polls the bot
	print('Polling..')
	app.run_polling(poll_interval=3)
