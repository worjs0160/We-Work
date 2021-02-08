from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Calendar


class Calendar_u(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar_u, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, user, day, events):
        events_per_day = events.filter(start_time__day=day).filter(user=user)
        d = ""

        for event in events_per_day:
            d += f"<li style='background-color:#54f62ba6; font-weight: 700;'> {event.get_html_url} </li>"

        if day != 0 and day != datetime.today().day :
            return f"<td ><span class='date'>{day}</span><ul style='list-style: none; padding-left: 0px; padding-right: 0px;'> {d} </ul></td>"

        elif day == datetime.today().day:
            return f"<td style='background-color:#fcf8e3;><span class='date'>{day}</span><ul style='list-style: none; padding-left: 0px;'> {d} </ul></td>"

        return "<td></td>"

    # formats a week as a tr
    def formatweek(self, user, theweek, events):
        week = ""
        for d, weekday in theweek:
            week += self.formatday(user, d, events)
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
            cal += f"{self.formatweek(user, week, events)}\n"
        return cal
