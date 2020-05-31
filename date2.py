from datetime import datetime
date_string =  "01/01/25 12:10:03.234567"
dt = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
print(dt)