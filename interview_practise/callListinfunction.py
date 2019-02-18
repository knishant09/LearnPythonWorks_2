

class Test_list:

    def __init__(self):

        print("Testing list pass")
        cmd = ["grep -i 'app.mode' /usr/local/megha/conf/app.properties", "cat /etc/system-release",
               "/usr/sbin/sestatus | head -1 | awk '{print $3}'",
               "/usr/bin/java -version 2>&1 | head -1 | awk '{print $3}",
               "date", "ls /usr/local/megha/conf/users | grep -v 'template'",
               "grep -i 'app.version' /usr/local/megha/conf/app.properties"]
        self.cmd = cmd
        print(type(cmd))
        print(cmd)




    def calling_list(self):
        print(self.cmd)


def main():
    #Passing values are IP, Username, password, Port and Target type (ova/rpm)

    obj = Test_list()

    obj.calling_list()


if __name__ == "__main__":
    main()


