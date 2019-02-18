from configparser import SafeConfigParser




def test_config():
    parser = SafeConfigParser()
    parser.read('config.ini')

    print(parser.get('VM_details','ip'))
    print(parser.get('VM_details', 'Auth'))
    print(parser.get('VM_details', 'startDate'))



test_config()



