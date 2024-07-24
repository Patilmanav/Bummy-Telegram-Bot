import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler
import requests
from keys import token

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
keyboard = [
    [InlineKeyboardButton("Get Data", callback_data='interact')],
    [InlineKeyboardButton("Get Data Using Id", callback_data='employee')]
]
reply_markup = InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Click here to get Employee Data: ",reply_markup=reply_markup)

async def interact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = ""
    try: 
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/json'
        }
        res = requests.get('https://dummy.restapiexample.com/api/v1/employees',headers=headers)
        print(res.status_code)
        data = res.json()
        if res.status_code == 200:
            message+=f"Employee Details\n\n"
            for index,employee in enumerate(data['data']):
                message += f"id = {employee['id']}\nName = {employee['employee_name']}\nSalary = {employee['employee_salary']}\nAge = {employee['employee_age']}\n\n"
            message += "\n\n"
        else:
            message = data["message"]
        
    except Exception as e:
        message = f"Error: {e}\nTry Again"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup=reply_markup)
    
async def employee(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = ""
    if context.args:
        if len(context.args) == 1:
            print(context.args[0])
            _id = context.args[0]
            # message += str(context.args)
            try: 
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                    'Accept': 'application/json'
                }
                res = requests.get('https://dummy.restapiexample.com/api/v1/employees',headers=headers)
                print(res.status_code)
                data = res.json()
                if res.status_code == 200:
                    for employee in data['data']:
                        # print("Id = ",type(employee['id']),type(_id))
                        if str(employee['id']) == _id:
                            message = ""
                            message+=f"Employee Details\n\n"
                            message += f"id = {employee['id']}\nName = {employee['employee_name']}\nSalary = {employee['employee_salary']}\nAge = {employee['employee_age']}\n\n"
                            break
                        else:
                            message = "Data Not Found"
                    message += "\n\n "
                else:
                    message += data["message"]
                
            except Exception as e:
                message = f"Error: {e}\nTry Again"
        else:
            message = "Argument Required: /employee <id>"
            
    else:
        message = "Usage: /employee <id>"
        
    
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message,reply_markup=reply_markup)

if __name__ == '__main__':
    application = ApplicationBuilder().token(token=token).build()
    
    start_handler = CommandHandler('start', start)
    getDataBy = CommandHandler('employee', employee)
    interact_handler = CallbackQueryHandler(interact, pattern='interact')
    employee_handler = CallbackQueryHandler(employee,pattern='employee')
    
    application.add_handler(start_handler)
    application.add_handler(interact_handler)
    application.add_handler(employee_handler)
    application.add_handler(getDataBy)
    
    application.run_polling()