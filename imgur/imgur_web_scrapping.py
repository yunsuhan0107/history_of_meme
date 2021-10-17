import configparser
from imgurpython import ImgurClient

config = configparser.ConfigParser()
configFilePath = r'C:\Users\parks\Python\history_of_meme\imgur\auth.ini'
config.read(configFilePath)

client_id = config.get('credentials', 'client_id')
client_secret = config.get('credentials', 'client_secret')

client = ImgurClient(client_id, client_secret)

items = client.gallery()
# print(items)

for item in items:
    print(item.link)
    print(item.title)
    print(item.views)
    print()