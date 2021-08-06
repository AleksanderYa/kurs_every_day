import time
import requests


def send_message(bot_message):
    bot_token = '1841807907:AAEDJ9ansdw0yWGMtrY7tLhqnzEHbXBtkrI'
    bot_chatID = '1075097936'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
