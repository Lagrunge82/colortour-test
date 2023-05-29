# Инструкция по запуску проекта.

1) Склонируйте репозиторий:

    ```git clone git@github.com:Lagrunge82/colortour-test.git```
2) Установите виртуальное окружение в каталоге **colortour-test**:

    ```python -m venv venv```
3) Активируйте виртуальное окружение
   
   ```[Windows] .\venv\Scripts\activate```

   ```[unix-like] source ./venv/bin/activate```
4) Установите зависимости

   ```pip install -r requirements.txt```
5) Переименуйте файл **.env.sample** в **.env** и впишите в него значение переменных.
6) Для запуска тестов выполните команду:

   ```pytest -s -v```
7) Для запуска сервера выполните команду:

   ```uvicorn main:app --reload```

   Теперь к приложению можно обратиться по url:

   ```http://127.0.0.1:8000/api/v1/orders```

   - Метод: POST
   - Формат данных: Request body application/json
   - Пример запроса:

   ```
   {
      "volume": 1000.0,
      "number": 5,
      "amountDif": 5.0,
      "side": "BUY",
      "priceMin": 20000.0,
      "priceMax": 40000.0
   }
   ```