import modules.bot_creation as m_bot
import modules.keyboard_creation as m_keyboard
import modules.user_sending_message as m_send_message
@m_bot.bot.message_handler(commands=["start"])
def bot_start(message):
    m_bot.bot.send_message(
        message.chat.id, "Hi user!", 
        reply_markup=m_keyboard.menu_bar 
    )
    m_bot.bot.register_next_step_handler(
        message, 
        m_send_message.send_message_user
    )
