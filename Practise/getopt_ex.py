import getopt, sys
from sys import argv


class Testgetopt():

    def __init__(self, username, password ):
        self.username = username
        self.password = password


    def getopt_test(self):
        print(self.username)
        print(type(self.username))
        print(self.password)

       # print("this is a username:{}
        print("this is a password: %s" %(self.password))





def main(argv):
    print("hello")

    username = ""
    password = ""

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hu:p:', ['username=', 'password='])
        print("13123")
    except getopt.GetoptError as msg:
        print('ERROR in input arguments!')
        print(msg)
        print("""usage: %s [-d|-e|-u|-t] [file|-]
                -d, -u: decode
                -e: encode (default)
                -t: encode and decode string 'Aladdin:open sesame'""" % sys.argv[0])
        sys.exit(2)

    print(len(opts))

    if len(opts) == 0:
        print("enter the following commands: getopt_ex.py -u <username> -p <password>")
        print("""usage: %s [-h | -u | -p]
                -h --help
                -u --username
                -p --password""")
        sys.exit(0)


    try:
        for opt, arg in opts:
            print("23423423")
            if opt in ("-h", "--help"):
                print("getopt_ex.py -u <username> -p <password>")
                sys.exit(0)
            elif opt in ("-u", "--username"):
                username = arg
            elif opt in ('-p', '--password'):
                password = arg
    except Exception as e:
        print(e)
    print(username, password)
    print("***********")
    obj = Testgetopt(username,password)
    obj.getopt_test()


if __name__ == "__main__":
    main(argv)


