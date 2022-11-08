import telegram
import time

# chat id 설정
chat_id = '1634697207'
chat_id_sumin = '5210842931' # 수민이 아이디

# 실행
while True:
    bot_token = "5481129438:AAGlrBFZK_ZDvGGLYBYt3Kg6mPL260K5kFM"
    bot = telegram.Bot(bot_token)
    final_message = "독하다 독해"

    # image = '8541218392_l (1).jpg'
    # bot.send_photo(chat_id, photo=open(image, 'rb'))

    bot.sendMessage(chat_id_sumin, text=final_message)
    # bot.sendMessage(chat_id, text=final_message)
    time.sleep(1)