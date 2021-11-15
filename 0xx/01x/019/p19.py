from datetime import date, timedelta

# с 1 января 1901 года до 31 декабря 2000 года
start, end = date(1901, 1, 1), date(2000, 12, 31)
days = [start + timedelta(x) for x in range((end - start).days + 1)]
print(len([d for d in days if d.weekday() == 6 and d.day == 1]))