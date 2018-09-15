import os
import cv2

def CreateDirectory(path):
    if not os.path.isdir(path):
        try:
            os.mkdir(path)
        except OSError:
            print("Создать директорию %s не удалось" % path)
            return False
        else:
            print("Успешно создана директория %s" % path)
            return True

print("-----------------------------------------")
print("Данная программа преобразовывает папку с изображениями в градацию серого.")
print("Обработанный материал помещается в папку Gray в директории с изображениями.")
print("Данный процесс необходим для обучения Каскада Хаара, так как он воспринимает только серые изображения.")
print("-----------------------------------------\n")
print("Введите путь к папке с изображениями: ")
path = input()

files = os.listdir(path)

images = []
for file in files:
    if (file.find(".jpg") or file.find(".jpeg") or file.find(".png")):
        images.append(file)

if images:
    newPath = path + "\Gray"
    if CreateDirectory(newPath):
        for image in images:
            normalImage = cv2.imread(path + "\\" + image)
            grayImage = cv2.cvtColor(normalImage, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(newPath + "\\" + image, grayImage)
            print("Файл: " + path + "\\" + image + " Был обработан и отправлен по дериктории: " + newPath + "\\" + image)
print("Программа была завершина.\n")