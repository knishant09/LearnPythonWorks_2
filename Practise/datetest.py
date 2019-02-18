import datetime
from datetime import datetime, timedelta



start = datetime.now()
end = start + timedelta(days=60)

tmp = start

while tmp < end:
   # print(tmp)
    tmp = tmp + timedelta(days=2)
    print(tmp.strftime("%Y%m%d"))
