from dotenv import load_dotenv,find_dotenv
from openai import OpenAI
from database import Database
class BotModel:
    def __init__(self,name) -> None:
        self.name=name
        self.model='gpt-3.5-turbo-1106'
        _: bool=load_dotenv(find_dotenv())
        self.client:OpenAI = OpenAI()
        self.db= Database()
        self.messages=self.loadChatHistory()

    def loadChatHistory(self)->None:
        return self.db.loadChatHistory()
    
    def saveChatHistory(self)->None:
        return self.db.saveChatHistory(self.messages)
    
    def deleteChatHistory(self)->None:
        print('Chat History : Deleted')
        self.messages=[]
        self.saveChatHistory()

    def getMessage(self)->None:
        return self.messages
    
    def appendMessage(self,message)->None:
        self.messages.append(message)

    def sendMessage(self,message)->None:
        self.appendMessage(message)
        stream=self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            stream=True
        )
        return stream