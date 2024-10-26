from typing import Any

response = {
    0: "Успешное выполнение запроса.",

    10: "Ошибки регистрации/авторизации",
    11: "Пароль должен содердать цифры, буквы верхнего и нижнего регистра и символ.",
    12: "Пароли не совпадают.",
    13: "Проверочный код введен не верно.",
    14: "Срок действия проверочного кода истек. Повторите отправку.",
    15: "Номер телефона не соответствует Российскому стандарту.",
    16: "Такой пользователь уже зарегестрирован.",
    17: "Не допускается смешивание алфавитов в имени.",

    20: "Ошибки проксирования",
    21: "Сторонний сервис недоступен",
    22: "Отказ доступа к стороннему сервису.",


    30: "Сессионные ошибки",
    31: "Сессия пользователя неактивна.",
    32: "",

    40: "Ошибки базы",
    41: "Отказ доступа к базе данных.",

    90: "Общие ошибки.",
    91: "Ошибка на стороне сервера.",
    92: "Отказ в доступе со стороны сервера.",

}


class ResponseCode(object):
    def __init__(self, code: int, data: Any = None):
        self.code: int = code
        self.answer: str = response[self.code]
        self.data: Any = data

    def __call__(self, *args, **kwargs):
        if self.data is None:
            del self.data
            return {'code': self.code,
                    'answer': self.answer
                    }
        else:
            return {'code': self.code,
                    'answer': self.answer,
                    'data': self.data}