import os, sys, paramiko
from datetime import datetime, timedelta
import datetime, time



class Createfiles():

    def __init__(self, host, username, password, port, num_of_days, cp_file_data):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.num_of_days = num_of_days
        self.cp_file_data = cp_file_data
        self._ssh = ""

    def ssh_connect(self):
        print(self.username)
        print(self.host)
        print(self.port)
        print(self.password)

        self._ssh = paramiko.SSHClient()
        self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._ssh.connect(self.host, self.port, self.username, self.password)


    def createdir(self):

        start = datetime.datetime.now()
        end = start + timedelta(days=self.num_of_days)
        '''''
        start_date = "20150101"
        end_date = "20151231"

        start_date = datetime.datetime.strptime(start_date,"%Y%m%d")
        print(start_date)
        print(type(start_date))

        end_date = datetime.datetime.strptime(end_date,"%Y%m%d")
        print(end_date)
        print(type(end_date))

        while start_date < end_date:
            print("this is true")
            start_date = start_date + timedelta(days=5)
            print(start_date)
            print(start_date.strftime("%Y%m%d"))
        '''''



        tmp = start + timedelta(days=1)

        while tmp < end:
            
            tmp = tmp + timedelta(days=4)
            new_date = tmp.strftime("%Y%m%d")
            print(new_date)

            mk_dir = "echo 'megha.jeos' | su - megha -c 'mkdir /usr/local/megha/db/perf/{}'".format(new_date)
            print(mk_dir)
            stdin, stdout, stderr = self._ssh.exec_command(mk_dir)
            time.sleep(2)
            err = str(stderr.readlines())
            if "File exists" in err:
                print("Deleting Existing Files")
                rm_dir = "rm -rf /usr/local/megha/db/perf/{}".format(new_date)
                stdin, stdout, stderr = self._ssh.exec_command(rm_dir)
                print("Files are getting deleted")
                time.sleep(3)


            cp_files = "echo 'megha.jeos' | su - megha -c 'cp -r /usr/local/megha/db/perf/{}/* /usr/local/megha/db/perf/{}/'".format(self.cp_file_data, new_date)
            print(cp_files)
            stdin, stdout, stderr = self._ssh.exec_command(cp_files)
            print(stderr.readlines())
            time.sleep(2)

        end_date = datetime.datetime.strptime(new_date,"%Y%m%d") + timedelta(days=1)
        dt = str(end_date.strftime("%Y%m%d"))
        perf_end_time = "perf_end_time=" + dt + "_000000"
        print(perf_end_time)

        update_import_status = "sed -i -e 's/perf_end_time=[[:digit:]]\+_[[:digit:]]\+/{}/g' /usr/local/megha/conf/importStatus.properties".format(perf_end_time)
        print(update_import_status)
        stdin, stdout, stderr = self._ssh.exec_command(update_import_status)

        stop_jetty = "/usr/local/megha/bin/megha-jetty.sh stop"
        stdin, stdout, stderr = self._ssh.exec_command(stop_jetty)
        time.sleep(10)
        start_jetty = "/usr/local/megha/bin/megha-jetty.sh start"
        stdin, stdout, stderr = self._ssh.exec_command(start_jetty)
        time.sleep(10)



def main():
    # hostname, Username, password, portnumber, delta date, start date, end_date, copy_date_file
    #obj = Createfiles("192.168.100.95", "root", "root123", 22, 5, 20150101, 201 20180717)
    obj = Createfiles("192.168.100.95", "root", "root123", 22, 4, 365, 20180717)
    obj.ssh_connect()
    obj.createdir()

if __name__ == "__main__":
    main()












