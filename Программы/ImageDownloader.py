import urllib.request
import cv2
import os

def store_raw_images():
    #http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03256166
    #http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04490091
    print("Программа скачивает список изображений с сайта")
    print("Список можно взять на сайте image-net.org")
    print("Введите ссылку на список картинок: ")
    neg_images_link = input()
    neg_images_urls = urllib.request.urlopen(neg_images_link).read().decode()

    if not os.path.exists('neg'):
        os.makedirs('neg')

    pic_num = 786

    for i in neg_images_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+'.jpg')
            img = cv2.imread("neg/"+str(pic_num)+'.jpg', cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/"+str(pic_num)+'.jpg', resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))

store_raw_images()
