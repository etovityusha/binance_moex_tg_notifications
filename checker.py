import requests
from pydantic.main import BaseModel

from config import MIN_PROFIT_FOR_NOTIFICATION, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from notifier import TelegramNotifier


class ScenarioResponse(BaseModel):
    profit: float
    oldest_quote: int
    details: dict


class ProfitChecker:
    def __init__(self, scenario_id: int):
        self.scenario_id = scenario_id
        self.url = f'http://158.101.192.82:6110/scenarios/{scenario_id}'

    def run(self):
        response = requests.get(self.url).json()
        response = ScenarioResponse(
            profit=response['profit'],
            oldest_quote=response['oldest_quote'],
            details=response['details']
        )
        is_actual = response.oldest_quote < 180
        if response.profit > MIN_PROFIT_FOR_NOTIFICATION and is_actual:
            TelegramNotifier(
                bot_token=TELEGRAM_BOT_TOKEN,
                chat_id=TELEGRAM_CHAT_ID
            ).send_message(
                f' Scenario {self.scenario_id}: profit {round(response.profit, 2)} percents'
            )
