import configparser, urllib.request, datetime, os, requests, hashlib, io
from imgurpython import ImgurClient
# from PIL import Image

config = configparser.ConfigParser()
configFilePath = r'C:\Users\parks\Python\history_of_meme\imgur\auth.ini'
config.read(configFilePath)

client_id = config.get('credentials', 'client_id')
client_secret = config.get('credentials', 'client_secret')

client = ImgurClient(client_id, client_secret)

items = client.gallery()
urlList = []
titleList = []

for item in items:
    if (item.datetime < 1293861599):
        print(item.link + " was uploaded before 2010.")
    elif (item.datetime > 1293861599 and item.datetime < 1546322399):
        print(item.link + " was uploaded after 2010 but before 2018.")
    elif (item.datetime > 1546322399):
        print(item.link + " was uploaded after 2018.")
        print(item.link + " was uploaded on " + str(datetime.datetime.fromtimestamp(item.datetime)))
        urlList.append(item.link)
        titleList.append(item.title)
    # print(item.link)
    # print(item.title)
    # print(item.views)
    # print(item.datetime)
    print()

# print(items.sort)

# def saveImage(url, fpath):
#     contents = urllib.request.urlopen(url)
#     f = open(fpath, 'w')
#     f.write(contents.read())
#     f.close()

# for url in urlList:
#     saveImage(url, r"C:\Users\parks\Python\meme_images")

print("Finished downloading images")

def download_image(image_title, image_url, download_path):
    # Download image and save it to file path
    try:
        # download = urllib.request.URLopener()
        # download.retrieve(image_url, download_path)
        # urllib.request.urlretrieve(image_url, download_path)
        urllib.request.urlretrieve(image_url, os.path.join(download_path, image_title))
        print("File {} downloaded to {}".format(image_url, download_path))

    except urllib.error.URLError as e:
        print("Error downloading image '{}': {}".format(image_url, e))
    except urllib.error.HTTPError as e:
        print("HTTP Error download image '{}': {!s}".format(image_url, e))

print(urlList)
print()

# for url in urlList:
#     index = 0
#     download_image(titleList[index], url, r"C:\Users\parks\Python\meme_images")
#     index += 1

# print("Finished downloading images")

# def persist_image(folder_path:str, url:str):
#     try:
#         image_content = requests.get(url).content

#     except Exception as e:
#         print(f"ERROR - Could not download {url} - {e}")

#     try:
#         image_file = io.BytesIO(image_content)
#         image = Image.open(image_file).convert('RGB')
#         file_path = os.path.join(folder_path, hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
#         with open(file_path, 'wb') as f:
#             image.save(f, "JPEG", quality=85)
#         print(f"SUCCESS - saved {url} - as {file_path}")

#     except Exception as e:
#         print(f"ERROR - Could not save {url} - {e}")

# for url in urlList:
#     persist_image(r"C:\Users\parks\Python\meme_images", url)

# print("Finished downloading images")