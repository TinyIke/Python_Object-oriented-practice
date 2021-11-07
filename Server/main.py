import Db_handler

import server2

host = "127.0.0.1"
port = 20001
Data_Object = Db_handler.Db_handler()
server = server2.PureSocketServer(host, port, Data_Object)
server.serve()



while(True):    
    print('Welcome to server')
    choise = int(input('Enter 0 to stop:'))
    if (choise == 0):
        print('bye')
        break
    #else:
        #Choise[choise].execute()
    #Data.save(Dict)