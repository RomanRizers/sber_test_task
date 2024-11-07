"""
У тимлида очень плотный календарь, настолько, что он не понимает, когда ему
работать свою работу.
Первым шагом он хочет понять сколько времени проводит на встречах.
Он сделал выгрузку своего календаря со всеми встречами. И теперь хочет понять,
сколько минут в каждый из дней недели он проводит на встречах.
"""

from datetime import datetime
from collections import defaultdict

def meeting_info(meeting_id, user_id, start_time, end_time):
    """Создает словарь, представляющий информацию о встрече."""
    return {
        "id": meeting_id, 
        "user_id": user_id, 
        "meet_start": start_time, 
        "meet_end": end_time
    }

data = [
    meeting_info(1, 777, "2023-07-24 16:00:00", "2023-07-24 17:00:00"),
    meeting_info(2, 777, "2023-07-24 16:00:00", "2023-07-24 16:50:00"),
    meeting_info(3, 777, "2023-07-24 18:00:00", "2023-07-24 18:30:00"),
    meeting_info(4, 777, "2023-07-24 17:30:00", "2023-07-24 18:10:00"),
    meeting_info(5, 777, "2023-07-24 17:00:00", "2023-07-24 17:10:00"),
    meeting_info(6, 777, "2023-07-24 16:20:00", "2023-07-24 16:50:00"),
    meeting_info(7, 777, "2023-07-25 12:00:00", "2023-07-25 16:50:00"),
    meeting_info(8, 777, "2023-07-25 18:00:00", "2023-07-25 18:30:00"),
    meeting_info(9, 777, "2023-07-26 17:30:00", "2023-07-26 18:10:00"),
    meeting_info(10, 777, "2023-07-26 17:00:00", "2023-07-26 17:10:00"),
    meeting_info(11, 777, "2023-07-27 16:20:00", "2023-07-27 16:50:00")
]

meetings_sum = defaultdict(int)
weekday_map = {
    'Monday': 'Понедельник',
    'Tuesday': 'Вторник',
    'Wednesday': 'Среда',
    'Thursday': 'Четверг',
    'Friday': 'Пятница',
    'Saturday': 'Суббота',
    'Sunday': 'Воскресенье'
}

def parse_datetime(date_str):
    """Преобразует строки в datetime."""
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

for event in data:
    start = parse_datetime(event["meet_start"])
    end = parse_datetime(event["meet_end"])
    
    duration_minutes = (end - start).seconds / 60
    weekday = start.strftime("%A")
    weekday_russian = weekday_map[weekday]
    meetings_sum[weekday_russian] += duration_minutes

for day, total_minutes in meetings_sum.items():
    print(f"{day}: {total_minutes:.1f} минут")
