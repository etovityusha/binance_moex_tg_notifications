import requests


class TelegramNotifier:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id

    def send_message(self, message, disable_notification=False):
        if len(message) > 4096:
            raise ValueError("Длина сообщения не должна превышать 4096 символов.")
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage?chat_id={self.chat_id}&text={message}"
        if disable_notification:
            url += '&disable_notification=true'
        response = requests.get(url)
        return {"success": response.status_code == 200}
