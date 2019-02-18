import os, sys, paramiko
from datetime import datetime, timedelta
import datetime, time



class Createfiles():

    def __init__(self, host, username, password, port, delta_days, start_date, end_date, cp_file_data):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.delta_days = delta_days
        self.start_date = start_date
        self.end_date = end_date
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

       # start = datetime.datetime.now()
       # end = start + timedelta(days=self.num_of_days)

        #start_date = "20150101"
        #end_date = "20151231"
        print(self.start_date, self.end_date)
        start_date = datetime.datetime.strptime(self.start_date,"%Y%m%d")
        print(start_date)
        print(type(start_date))

        end_date = datetime.datetime.strptime(self.end_date,"%Y%m%d")
        print(end_date)
        print(type(end_date))




        #end_date = datetime.datetime.strptime(new_date, "%Y%m%d") + timedelta(days=1)
       # dt = str(self.s.strftime("%Y%m%d"))
        perf_start_time = "perf_start_time=" + self.start_date + "_000000"
        print(perf_start_time)

        conf_start_time = "conf_start_time=" + self.start_date + "_000000"
        print(conf_start_time)

        time.sleep(10)

        perf_import_status = "sed -i -e 's/perf_start_time=[[:digit:]]\+_[[:digit:]]\+/{}/g' /usr/local/megha/conf/importStatus.properties".format(perf_start_time)
        print(perf_import_status)
        stdin, stdout, stderr = self._ssh.exec_command(perf_import_status)
        time.sleep(10)

        conf_import_status = "sed -i -e 's/conf_start_time=[[:digit:]]\+_[[:digit:]]\+/{}/g' /usr/local/megha/conf/importStatus.properties".format(conf_start_time)
        print(conf_import_status)
        stdin, stdout, stderr = self._ssh.exec_command(conf_import_status)
        time.sleep(5)

        stop_jetty = "/usr/local/megha/bin/megha-jetty.sh stop"
        stdin, stdout, stderr = self._ssh.exec_command(stop_jetty)
        time.sleep(10)
        start_jetty = "/usr/local/megha/bin/megha-jetty.sh start"
        stdin, stdout, stderr = self._ssh.exec_command(start_jetty)
        time.sleep(10)


        while start_date < end_date:
            print("this is true")
            start_date = start_date + timedelta(days=self.delta_days)
            print(start_date)
            new_date = start_date.strftime("%Y%m%d")

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

        stop_jetty = "/usr/local/megha/bin/megha-jetty.sh stop"
        stdin, stdout, stderr = self._ssh.exec_command(stop_jetty)
        time.sleep(10)
        start_jetty = "/usr/local/megha/bin/megha-jetty.sh start"
        stdin, stdout, stderr = self._ssh.exec_command(start_jetty)
        time.sleep(10)

       

def main():
    # hostname, Username, password, portnumber, delta days, start_date[YYYYMMDD], end_date[YYYYMMDD], Data file to copy
    obj = Createfiles("192.168.100.95", "root", "root123", 22, 4, "20180316", "20180630", 20180716)
    obj.ssh_connect()
    obj.createdir()

if __name__ == "__main__":
    main()












