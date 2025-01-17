import requests
import allure

@allure.epic("Авиасейлс - поиск дешевых билетов")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://www.aviasales.ru/", name="Авиасейлс")

class Travel:
    """
                Класс определяет сущность Travel, позволяющую поиск авиабилетов
                по различным критериям на сайте компании Авиасейлс.
                Результат запроса приходит в формате JSON, который обрабатывается
    """


    def __init__(self) -> None:
        self.token = TOKEN
        self.url = BASE_URL
    """
                активация
    """

    @allure.story("")
    @allure.feature("")
    @allure.title("")
    @allure.description("")
    def low_cost_com(self):
        headers = {'X-Access-Token': self.token}
        params = {
            "origin": "MOW",
            "destination": "AER",
            "depart_date": "2025-07",
            "return_date": "2025-07",
            "page": "3",
            "currency": "RUB"
}
        resp = requests.get(f"{self.url}cheap", headers = headers, params = params)
        return resp


    @allure.story("")
    @allure.feature("")
    @allure.title("")
    @allure.description("")
    def direct_tickets(self):
        headers = {'X-Access-Token': self.token}
        params = {
            "origin": "MOW",
            "destination": "AER",
            "depart_date": "2025-07",
            "return_date": "2025-07",
        }
        resp = requests.get(f"{self.url}direct", headers=headers, params=params)
        return resp


    @allure.story("")
    @allure.feature("")
    @allure.title("")
    @allure.description("")
    def every_day_tickets(self):
        headers = {'X-Access-Token': self.token}
        params = {
            "origin": "MOW",
            "destination": "AER",
            "depart_date": "2025-07",
            "return_date": "2025-07",
        }
        resp = requests.get(f"{self.url}direct", headers=headers, params=params)
        return resp