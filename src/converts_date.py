import datetime as dt


def converts_date(date: str) -> str:
    """
    Меняет формат даты из ГГГГ-ММ-ДД в ДД.ММ.ГГГГ
    """
    date = date[0:10]
    old_format = dt.datetime.strptime(date, '%Y-%m-%d')
    new_format = dt.datetime.strftime(old_format, '%d.%m.%Y')
    return new_format
