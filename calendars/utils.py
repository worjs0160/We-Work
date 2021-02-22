from datetime import datetime, timedelta
from calendar import HTMLCalendar
from itertools import chain
from .models import Calendar


class Calendar_u(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar_u, self).__init__()

    # formats a day as a td
    # filter events by day
<<<<<<< HEAD
    def formatday(self, user, day, events):
        # events_per_day = events.filter(start_time__day=day).filter(user=user)
        
        finish_day = events.filter(start_time__day__lt=(day+1)).filter(end_time__day__gt=(day-1)).filter(user=user)
        print(day, finish_day)
        
        d = ""

        for event in finish_day:
            d += f"<li style='background-color:#54f62ba6; font-weight: 700; padding-left: 10px;margin-bottom: 10px;'> {event.get_html_url} </li>"

        if day != 0 and day != datetime.today().day:
            return f"<td ><span class='date'>{day}</span><ul style='list-style: none; padding-left: 0px; padding-right: 0px;'> {d} </ul></td>"

        elif day == datetime.today().day:
            return f"<td style='background-color:#fcf8e3;'><span class='date'>{day}</span><ul style='list-style: none; padding-left: 0px;'> {d} </ul></td>"
=======
    def formatday(self, user, day, month, events):
        events_per_day = events.filter(start_time__day=day).filter(user=user)
        
        d = ""
        for event in events_per_day:
            d += f"<li style='background-color:#54f62ba6; padding-left: 5px; font-weight: 700;'> {event.get_html_url} </li>"

        if day != 0 and day != datetime.today().day :
            return f"<td ><span class='date'>{day}</span><ul style='list-style: none; margin-left: -25px; padding-right: 0px;'> {d} </ul></td>"
>>>>>>> e60a65e93b14afb8928fc01a6567718bdbb061e7

        else:
            if month == datetime.today().month and day == datetime.today().day:
                return f"<td style='background-color:#fcf8e3;'><span class='date'>{day}</span><ul style='list-style: none; margin-left: -25px; padding-right: 0px;'> {d} </ul></td>"
            elif month != datetime.today().month and day == datetime.today().day:
                return f"<td ><span class='date'>{day}</span><ul style='list-style: none; margin-left: -25px; padding-right: 0px;'> {d} </ul></td>"
        return "<td></td>"

    # formats a week as a tr
    def formatweek(self, user, theweek, month, events):
        week = ""
        # print(theweek, '일주일 데이터 확인~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!')
        for d, weekday in theweek:
<<<<<<< HEAD
            # print(d, events, '일주일 데이터 확인~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!')
            week += self.formatday(user, d, events)
=======
            week += self.formatday(user, d, month, events)
>>>>>>> e60a65e93b14afb8928fc01a6567718bdbb061e7
        return f"<tr> {week} </tr>"

    # formats a month as a table
    # filter events by year and month
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

    # def formatday(self, user, day, events):
    #     print(events, day, user,"formatday -----------------------------")
    #     events_per_day = events.filter(start_time__day=day).filter(user=user)
    #     d = ""

    #     for event in events_per_day:
    #         d += f"<li> {event.get_html_url} </li>"

    #     if day != 0:
    #         return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
    #     return "<td></td>"

    def time_data(self, user, day, hour, events):

        events_per_day = events.filter(start_time__day=day).filter(
            start_time__hour=hour).filter(user=user)

        d = ""

        for event in events_per_day:
            d += f"<li> {event.get_html_url} </li>"

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
        for idx in range(9, 22):
            for d, weekday in theweek:
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
            d += f"<li> {event.get_html_url} </li>"

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
            theday.append([(a,recombination)])

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