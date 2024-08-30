from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from toggle_power import toggle, clean
from time import sleep

TOKEN: Final = '7305722961:AAEoDHBK9noJNbgd4wCFufuJlLgBZWWWCeA'
BOT_USERNAME: Final = '@machine_ctl_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):	# 입력 할수 있는 커맨드 설정(비동기 함수로 선언)
	await update.message.reply_text('원하는 옵션을 골라주세요.\n 1. /help 2. /cature 3. /toggle')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('1. /help    : 각 기능의 도움말을 보여줍니다.\n')
	await update.message.reply_text('2. /capture : 에어컨의 상태를 보여줍니다.\n')
	await update.message.reply_text('3. /toggle  : 에어컨의 전원을 키거나 끕니다.')

async def capture_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('에어컨의 상태를 촬영중입니다')
	sleep(3)
	# 사진 전송 함수 호출
	await update.message.reply_text('에어컨의 상태를 확인하세요')

async def toggle_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('전원을 토글중입니다...')
	toggle()
	# clean() 필요시 주석제거
	sleep(1)
	await update.message.reply_text('전원 토글이 완료되었습니다.')
	await update.message.reply_text('토글이 안 됐을 수 있으니 /capture로 확인해주세요.')

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

async def service_start(app: Application):
	await app.bot.send_message(chat_id=5708440853, text="서비스가 정상적으로 시작되었습니다.\n/start를 입력해주세요")

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):		# 에러 처리함수(비동기)
	print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
	print('Starting bot..')
	app = Application.builder().token(TOKEN).build()
	
	# commands
	app.add_handler(CommandHandler('start', start_command))
	app.add_handler(CommandHandler('help', help_command))
	app.add_handler(CommandHandler('capture', capture_command))
	app.add_handler(CommandHandler('toggle', toggle_command))
	
	# Messages
	# app.add_handler(CommandHandler(filters.TEXT, handle_massge))

	# Errors
	app.add_error_handler(error)
	
	# bot starting message
	app.post_init = service_start

	#Polls the bot
	print('Polling..')
	app.run_polling(poll_interval=3)
