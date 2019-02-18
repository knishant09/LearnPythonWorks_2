import subprocess, time
from datetime import datetime
from datetime import timedelta


def lsof_dump():

    i = 1

    while i > 1:
        print("*********************")
        print(i)
        print("*********************")

        cmd = "lsof"

        time.sleep(360)

        new_date = datetime.now() + timedelta(seconds=360)
        n_date = new_date.strftime("%Y%m%d%H%M%S")

        print(n_date)

        output = subprocess.check_output(cmd)

#        f = open('{}.csv'.format(new_date), 'wb')
        f = open('%s.txt' % n_date, 'wb')
        f.write(output)

        i += 1

lsof_dump()