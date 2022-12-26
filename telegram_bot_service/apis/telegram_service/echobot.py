import requests

CHAT_ID = 1101805271

requests.post('https://api.telegram.org/bot5887651365:AAFFCwjRLxYIdehdq-fE42W8Rplah3a7oBM/sendMessage',
    data= {'chat_id' : CHAT_ID, 'text' : "Hola que tal"} )