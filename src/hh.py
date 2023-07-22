from abc import ABC, abstractmethod
import requests
import os

API_KEY = os.getenv("API_KEY_SJ")


class Api(ABC):
    """
    Создаем класс для работы с API сайтов с вакансиями
    """

    @abstractmethod
    def get_vacancies(self, vacancy):
        pass


class ApiHH(Api):
    """
    Создаем класс для работы с API HH.ru
    """
    def get_vacancies(self, vacancy):
        hh_dict = {}
        for page in range(0, 3):
            params = {
                "text": vacancy,
                "per_page": 100,
                "page": page,
            }
            response = requests.get("https://api.hh.ru/vacancies", params=params).json()
            hh_dict.update(response)
        return hh_dict


class ApiSuperJob(Api):
    """
    Создаем класс для работы с API Superjob
    """
    def get_vacancies(self, vacancy):
        params = {
            "keyword": vacancy
        }
        headers = {
            'X-Api-App-Id': API_KEY

        }
        response = requests.get("https://api.superjob.ru/2.0/vacancies", params=params, headers=headers).json()
        return response
