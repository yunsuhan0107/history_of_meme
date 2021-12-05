from google_images_download import google_images_download

# class instantiation
response = google_images_download.googleimagesdownload()

months = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
count = 0

# download memes from 2000 to 2021
for i in range(0, 22):
    for j in range(0, 12):
        year = 2000 + i
        month = months[count]

        # creating list of arguments
        arguments = {"keywords": str(year) + " " + month + " memes",
                     "limit": 5, "print_urls": True, "format": "jpg"}

        # passing the arguments to the function
        paths = response.download(arguments)

        count += 1

        # printing absolute paths of the downloaded images
        print(paths)