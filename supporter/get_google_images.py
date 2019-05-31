from google_images_download import google_images_download



def get_google_images(keyword, num):
    response = google_images_download.googleimagesdownload()   #class instantiation

    arguments = {"keywords":keyword,
                 "limit":int(num),
                 "print_urls":True}   #creating list of arguments
    paths = response.download(arguments)

    return(paths)

if __name__ == "__main__":
    text_value = input("Text to search Images: ")
    num_value = input("Number of Images: ")
    shelves = get_google_images(text_value, num_value)
    print(shelves)
