from pyVim import connect

my_host = connect.ConnectNoSSL("192.168.20.219", 443,"domain1\kumar", "kuma@123")

searcher = my_host.content.searchIndex

vm = searcher.FindbyIp




