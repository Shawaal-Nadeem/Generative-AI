import shelve


class Database:
    def __init__(self,dbName='Chat History') -> None:
        self.dbName=dbName

    #Load chat history from Shelve File
    def loadChatHistory(self)-> None:
        with shelve.open(self.dbName) as db:
            return db.get('messages',[])
        
    # Save chat history in Shelve file    
    def saveChatHistory(self,message):
        print("Database : Save ",message)
        with shelve.open(self.dbName) as db:
            db['messages']=message