from typing import Final
import status_mode, sql_data_input
from telegram import Update, InputFile
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
# from toggle_power import toggle, clean
# from capture_func import capture
from time import sleep

# 모드 저장 전역변수(기본적으로 능동모드로 선언)
mode = 1

# 텔레그램 봇 설정
TOKEN: Final = '7305722961:AAEoDHBK9noJNbgd4wCFufuJlLgBZWWWCeA'
BOT_USERNAME: Final = '@machine_ctl_bot'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):	# 입력 할수 있는 커맨드 설정(비동기 함수로 선언)
	sql_data_input.sql_input()
	await update.message.reply_text('온습도 측정을 시작합니다. 명령어를 보시려면 /help를 입력해주세요.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('1. /help    : 각 기능의 도움말을 보여줍니다.\n')
	await update.message.reply_text('2. /active  : 온습도에 따라 자동으로 에어컨을 토글하는 모드 \n')
	# await update.message.reply_text('3. /passive : 수동조작으로 에어컨을 토글하는 모드\n')
	await update.message.reply_text('3. /check   : 현재 모드를 확인(능동, 수동)\n')
	await update.message.reply_text('4. /toggle  : 에어컨의 전원을 키거나 끕니다\n')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        .')

async def active_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('능동모드 전환\n')
	mode = True
	status_mode.active()


# async def passive_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
# 	await update.message.reply_text('수동모드 전환\n')
# 	mode = False
# 	status_mode.passive()


async def stat_check_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('현재 모드 확인\n')
	if mode == True:
		await update.message.reply_text('현재는 능동모드 입니다.\n')
	else:
		await update.message.reply_text('현재는 수동모드 입니다.\n')

async def toggle_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
	if mode == True:
		await update.message.reply_text('현재는 능동모드 입니다. 수동으로 조작하실수 없습니다.\n')
	else:
		await update.message.reply_text('전원을 토글중입니다...\n')
		status_mode.toggle()
		sleep(1)
		await update.message.reply_text('전원 토글이 완료되었습니다.\n')
		with open('/home/aircon/aircon_ctl/pictures/captured_image.jpg', 'rb') as image_file:
	  		await context.bot.send_photo(chat_id=5708440853, photo=InputFile(image_file))
		await update.message.reply_text('에어컨의 상태를 확인하세요\n')
	

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
	app.add_handler(CommandHandler('active', active_command))
	# app.add_handler(CommandHandler('passive', passive_command))
	app.add_handler(CommandHandler('check', stat_check_command))
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
