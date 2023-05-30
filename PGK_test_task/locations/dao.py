import time
import random
from datetime import datetime, timedelta
from typing import List
from benchmark import timing


@timing
def get_current_dislocation() -> List:
    """
    Формирование текущей дислокации вагонов.
    Получаем список вагонов и их дату прибытия.
    Каждый вагон может быть привязан к одной и той же накладной!
    Для того, чтобы получить предсказанную дату прибытия, необходимо вызывать сервис 'get_predicted_dates'
    """
    locations = []
    arrivale_dates = [None, None, None, datetime.now() - timedelta(days=3), datetime.now()]
    time.sleep(2)

    for i in range(0, 20000):
        arrivale_date = random.choice(arrivale_dates)
        location = {
            "wagon": random.randint(10000, 90000),
            "invoice": f"{random.randint(1, 30000)}__HASH__",  # накладная
            "arrivale_date": arrivale_date.strftime("%d.%m.%Y") if arrivale_date else None,
        }
        locations.append(location)
    return locations


@timing
def get_predicted_date_by_invoices(invoices: List) -> List:
    """
    На вход необходимо передать список из уникальных накладных.
    По каждой накладной будет сформировано время прибытия
    """
    time.sleep(1)
    predicted_results = []
    for invoice in invoices:
        predicted_date = datetime.now() + timedelta(days=random.randint(1, 5))
        data = {
            "invoice": invoice,
            "predicted_date": predicted_date.strftime("%d.%m.%Y")
        }
        predicted_results.append(data)

    return predicted_results

@timing
def api_call():
    """
    В качестве ответа должен выдаваться повагонный список из сервиса get_current_dislocation
    с обновленной датой прибытия вагона из сервиса get_predicted_dates
    только по вагонам, у которых она отсутствует
    """
    locations = get_current_dislocation()

    # Получить список уникальных накладных из текущей дислокации только по тем вагонам,
    # где arrivale_date = None
    indexes = []
    invoices = []
    for i, location in enumerate(locations):
        if location['arrivale_date'] is None:
            indexes.append(i)
            invoices.append(location.get('invoice'))

    predicted_data = get_predicted_date_by_invoices(invoices)

    # словарь с соответствиями invoice -> predicted_date
    predicted_dates = {data['invoice']: data['predicted_date'] for data in predicted_data}

    # Обновить оригинальный список вагонов данными, которые прислал сервис get_predicted_dates().
    # Заменить вагоны, где arrivale_date = None на соответствующее поле predicted_date.
    for i in indexes:
        invoice = locations[i]['invoice']
        locations[i]['arrivale_date'] = predicted_dates.get(invoice)

    return locations




