import os, sys, shutil, errno
import datetime
from dateutil.rrule import rrule, DAILY


start_date = datetime.date(2018, 05, 06)
end_date = datetime.date(2018, 05, 07)

current = os.getcwd()
print current

src = 'D:\\django\\demo1'


for li in os.listdir(src):
    print li

for dt in rrule(DAILY, dtstart=start_date, until=end_date):
    target = os.path.join(current, dt.strftime("%Y%m%d"))
    os.mkdir(target)

#print filter(lambda x: os.path.isdir(x), os.listdir('.'))

directories = [d for d in os.listdir('.') if os.path.isdir(d)]

cmd = 'cp -r src directories[0]'

os.system(cmd)
'''''

for i in directories:
    try:
        os.system("cp -r src ")

shutil.copyfile(src, i)
    except IOError as e:
        print("Unable to copy file. %s" % e)
    except:
        print("Unexpected error:", sys.exc_info())

'''''



