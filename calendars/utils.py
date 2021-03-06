from datetime import datetime, timedelta
from calendar import HTMLCalendar
from itertools import chain
from .models import Calendar


class Calendar_Month(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar_Month, self).__init__()

    def formatday(self, user, day, month, events):
        events_per_day = events.filter(start_time__day__lt=(
            day+1)).filter(end_time__day__gt=(day-1)).filter(user=user)

        d = ""
        for event in events_per_day:
            # print(type(event), event.start_time.day,day)

            if event.all_day == True:
                if event.start_time.day == day:
                    d += f"<li style='background-color:#ffc500; padding-left: 10px; font-weight: 700;margin-bottom: 10px;' class='long_text'> {event.get_month_html_url} </li>"
            else:
                if event.start_time.day == day:
                    d += f"<li style='background-color:#54f62ba6; padding-left: 10px; font-weight: 700;margin-bottom: 10px;' class='long_text'> {event.get_month_html_url} </li>"
                else:
                    d += f"<li style='background-color:#54f62ba6; padding-left: 10px; font-weight: 700;margin-bottom: 10px;height: 19px;'><a></a></li>"

        if day != 0 and day != datetime.today().day:
            return f"<td ><span class='date'>{day}</span><ul style='list-style: none; margin-left: 0px; padding-right: 0px;'> {d} </ul></td>"

        elif day == datetime.today().day:
            return f"<td style='background-color:#fcf8e3;'><span class='date'>{day}</span><ul style='list-style: none; padding-left: 0px;'> {d} </ul></td>"

        else:
            if month == datetime.today().month and day == datetime.today().day:
                return f"<td style='background-color:#fcf8e3;'><span class='date'>{day}</span><ul style='list-style: none; margin-left: -25px; padding-right: 0px;'> {d} </ul></td>"
            elif month != datetime.today().month and day == datetime.today().day:
                return f"<td ><span class='date'>{day}</span><ul style='list-style: none; margin-left: -25px; padding-right: 0px;'> {d} </ul></td>"
        return "<td></td>"

    def formatweek(self, user, theweek, month, events):
        week = ""
        for d, weekday in theweek:

            week += self.formatday(user, d, month, events)
        return f"<tr> {week} </tr>"

    def formatmonth(self, user, withyear=True):
        events = Calendar.objects.filter(
            start_time__year=self.year, start_time__month=self.month
        )

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        cal += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f"{self.formatweek(user, week, self.month, events)}\n"
        return cal


class Calendar_Week(HTMLCalendar):
    def __init__(self, year=None, month=None, day=None):
        self.year = year
        self.month = month
        self.day = day

        super(Calendar_Week, self).__init__()

    def time_data(self, user, day, hour, events):
        # print(events," 여기서 데이터 넘어와야함") 2개 잘 넘어옴 시간이 9~10 시까지만 표시중임

        if hour == 8:
            events_per_day = events.filter(start_time__day=day).filter(
                user=user).filter(all_day=True)

            d = ""

            for event in events_per_day:
                d += f"<li class='long_text'> {event.get_html_url} </li>"

            if day != 0:
                return f"<td><ul> {d} </ul></td>"
        else:
            events_per_day = events.filter(start_time__day=day).filter(
                start_time__hour=hour).filter(user=user).filter(all_day=False)

            d = ""

            for event in events_per_day:
                d += f"<li class='long_text'> {event.get_week_html_url} </li>"

            if day != 0:
                return f"<td><ul> {d} </ul></td>"

        return "<td></td>"

    def formatweek(self, user, theweek, events):
        week = ""
        theweek.insert(0, (0, 1))
        for d, weekday in theweek:
            if d == 0:
                week += '<tr><th class="timezon">시간대</th>'
            else:
                if weekday == 0:
                    week += f'<th class="mon">Mon / {d}</th>'
                if weekday == 1:
                    week += f'<th class="tue">Tue / {d}</th>'
                if weekday == 2:
                    week += f'<th class="wed">Wed / {d}</th>'
                if weekday == 3:
                    week += f'<th class="thu">Thu / {d}</th>'
                if weekday == 4:
                    week += f'<th class="fri">Fri / {d}</th>'
                if weekday == 5:
                    week += f'<th class="sat" style="color:blue">Sat / {d}</th>'
                if weekday == 6:
                    week += f'<th class="sun" style="color:red">Sun / {d}</th></tr>\n'
        theweek.pop(0)
        return f"<tr> {week} </tr>"

    def format_time(self, user, theweek, events):
        week = ""
        theweek.insert(0, (0, 1))
        for idx in range(8, 22):
            for d, weekday in theweek:
                # 임시적으로 8이면 하루종일로 체크하게 로직 나중에는 특수한 값으로 변경 등 조치
                if idx == 8:
                    if d == 0:
                        week += f'<tr><td class="time">하루종일</td>'
                    else:
                        week += self.time_data(user, d, idx, events)
                else:
                    # print(theweek, '여기 확인')
                    if d == 0:
                        if idx == 9:
                            week += f'<tr><td class="time">09:00~10:00</td>'
                        else:
                            week += f'<tr><td class="time">{idx}:00~{idx+1}:00</td>'
                    else:
                        if weekday == 0:
                            week += self.time_data(user, d, idx, events)
                        if weekday == 1:
                            week += self.time_data(user, d, idx, events)
                        if weekday == 2:
                            week += self.time_data(user, d, idx, events)
                        if weekday == 3:
                            week += self.time_data(user, d, idx, events)
                        if weekday == 4:
                            week += self.time_data(user, d, idx, events)
                        if weekday == 5:
                            week += self.time_data(user, d, idx, events)
                        if weekday == 6:
                            week += self.time_data(user, d, idx, events)
        theweek.pop(0)
        return f"<tr> {week} </tr>"

    def formatmonth(self, user, withyear=True):
        now_week = self.monthdays2calendar(self.year, self.month)

        for idx, week in enumerate(now_week):
            for day in week:
                if(self.day == day[0]):
                    self.idx = idx

        week = now_week[self.idx]
        data_list = []
        for idx, val in week:
            data_list.append(idx)

        events = Calendar.objects.filter(
            start_time__year=self.year, start_time__month=self.month, start_time__day__in=data_list
        )

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'

        timetext = f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        timetext = timetext.replace('colspan="7"', 'colspan="8"')
        cal += timetext

        cal += f"{self.formatweek(user, now_week[self.idx], events)}\n"
        cal += f"{self.format_time(user, now_week[self.idx], events)}\n"
        return cal


class Calendar_Day(HTMLCalendar):
    def __init__(self, year=None, month=None, day=None):
        self.year = year
        self.month = month
        self.day = day

        super(Calendar_Day, self).__init__()

    def time_data(self, user, day, hour, events):

        events_per_day = events.filter(start_time__day=day).filter(
            start_time__hour=hour).filter(user=user)

        d = ""

        for event in events_per_day:
            d += f"<li class='long_text'> {event.get_day_html_url} </li>"

        if day != 0:
            return f"<td><ul> {d} </ul></td>"
        return "<td></td>"

    def formatweek(self, user, theweek, events):
        day = ""
        theweek.insert(0, (0, 1))
        for d, weekday in theweek:
            if d == 0:
                day += '<tr><th class="timezon">시간대</th>'
            else:
                if weekday == 0:
                    day += f'<th class="mon">Mon / {d}</th></tr>\n'
                if weekday == 1:
                    day += f'<th class="tue">Tue / {d}</th></tr>\n'
                if weekday == 2:
                    day += f'<th class="wed">Wed / {d}</th></tr>\n'
                if weekday == 3:
                    day += f'<th class="thu">Thu / {d}</th></tr>\n'
                if weekday == 4:
                    day += f'<th class="fri">Fri / {d}</th></tr>\n'
                if weekday == 5:
                    day += f'<th class="sat" style="color:blue">Sat / {d}</th></tr>\n'
                if weekday == 6:
                    day += f'<th class="sun" style="color:red">Sun / {d}</th></tr>\n'
        theweek.pop(0)
        return f"<tr> {day} </tr>"

    def format_time(self, user, theweek, events):
        day = ""
        theweek.insert(0, (0, 1))
        for idx in range(9, 22):
            for d, weekday in theweek:
                if d == 0:
                    if idx == 9:
                        day += f'<tr><td class="time">09:00~10:00</td>'
                    else:
                        day += f'<tr><td class="time">{idx}:00~{idx+1}:00</td>'
                else:
                    if weekday == 0:
                        day += self.time_data(user, d, idx, events)
                    if weekday == 1:
                        day += self.time_data(user, d, idx, events)
                    if weekday == 2:
                        day += self.time_data(user, d, idx, events)
                    if weekday == 3:
                        day += self.time_data(user, d, idx, events)
                    if weekday == 4:
                        day += self.time_data(user, d, idx, events)
                    if weekday == 5:
                        day += self.time_data(user, d, idx, events)
                    if weekday == 6:
                        day += self.time_data(user, d, idx, events)

        theweek.pop(0)
        return f"<tr> {day} </tr>"

    def formatmonth(self, user, withyear=True):
        now_week = self.monthdays2calendar(self.year, self.month)
        for idx, week in enumerate(now_week):
            for day in week:
                if(self.day == day[0]):
                    self.idx = idx
        week = now_week[self.idx]

        theday = []
        for a, recombination in week:
            theday.append([(a, recombination)])

        for idx, week in enumerate(theday):
            for day in week:
                if(self.day == day[0]):
                    self.idx = idx
        today = theday[self.idx]

        data_list = []
        for idx, val in today:
            data_list.append(idx)
        events = Calendar.objects.filter(
            start_time__year=self.year, start_time__month=self.month, start_time__day__in=data_list
        )
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'

        timetext = f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        timetext = timetext.replace('colspan="7"', 'colspan="2"')
        cal += timetext
        cal += f"{self.formatweek(user, theday[self.idx], events)}\n"
        cal += f"{self.format_time(user, theday[self.idx], events)}\n"
        return cal
