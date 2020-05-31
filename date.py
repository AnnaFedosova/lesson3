from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_TIME, "ru_RU")
dt_today = datetime.now()
delta = timedelta (days=1)
delta1 = timedelta (days=31)
dt_yesterday = dt_today - delta
dt_month_ago = dt_today - delta1
print(dt_today.strftime('%d %B %Y'))
print (dt_yesterday.strftime ('%d %B %Y'))
print (dt_month_ago.strftime ('%d %B %Y'))
