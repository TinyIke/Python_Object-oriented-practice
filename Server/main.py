import Db_handler

import server2

host = "127.0.0.1"
port = 20001
Data_Object = Db_handler.Db_handler()
server = server2.PureSocketServer(host, port, Data_Object)
server.serve()



while(True):    
    print('---------Menu---------')
    print('0. Quit the program')
    choise = int(input('Enter your choise:'))
    if (choise == 0):
        print('bye')
        break
    #else:
        #Choise[choise].execute()
    #Data.save(Dict)