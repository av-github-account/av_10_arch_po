# Получаем и кэшируем актуальные курсы валют от внешнего API.

import requests, json, os, time
from typing import Dict

class CurrencyRateService:
    def __init__(self, api_url="https://api.exchangerate-api.com/v4/latest/USD", cache_file="exchange_rates.json", cache_expiry=3600):
        self.api_url = api_url
        self.cache_file = cache_file
        self.cache_expiry = cache_expiry

    def _load_from_cache(self) -> Dict:
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'r') as f:
                try:
                    data = json.load(f)
                    if time.time() - data['timestamp'] < self.cache_expiry:
                        return data['rates']
                except (json.JSONDecodeError, KeyError):
                    pass
        return None

    def _save_to_cache(self, rates: Dict):
        data = {'timestamp': time.time(), 'rates': rates}
        with open(self.cache_file, 'w') as f:
            json.dump(data, f)

    def get_rates(self) -> Dict:
        rates = self._load_from_cache()
        if rates:
            return rates

        try:
            response = requests.get(self.api_url, timeout=10)
            response.raise_for_status()
            data = response.json()
            self._save_to_cache(data['rates'])
            return data['rates']
        except Exception as e:
            print(f"Error fetching exchange rates: {e}")
            return {}