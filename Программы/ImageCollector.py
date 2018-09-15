import os
import cv2

def OpenFile(fullPath):
    file = ""
    try:
        file = os.open(path + "\\" + "Good.dat", os.O_WRONLY | os.O_CREAT)
    except OSError:
        print("Файл не удалось открыть/создать!")
    else:
        print("Файл успешно открыт/создан!")
    return file

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


print("Данная программа компанует изображения в файл: Good.dat, для Каскада Хаара.")
print("Введите путь к папке с изображениями: ")

path = input()

files = os.listdir(path)

images = []
for file in files:
    if (file.find(".jpg") or file.find(".jpeg") or file.find(".png")):
        images.append(file)

newPath = path + "\\" + "Good"
CreateDirectory(path + "\\" + "Good")

for i in range(0, len(images)):
    form = ""
    if images[i].find(".jpg"):
        form = ".jpg"
    elif images[i].find(".png"):
        form = ".png"
    elif images[i].find(".jpeg"):
        form = ".jpeg"
    os.rename(path + "\\" + images[i], newPath + "\\" + str(i) + form)
    images[i] = str(i) + form
    print("Файл: " + path + "\\" + images[i] + " Переиминован " + newPath + "\\" + str(i) + form)

file = OpenFile(path + "\\" + "Good.dat")

for i in range(0, len(images)):
    image = cv2.imread(newPath + "\\" + images[i])
    height, width, channels = image.shape
    newString = "Good" + "\\" + images[i] + " 1 0 0 " + str(width) + " " + str(height) + "\n"
    os.write(file, bytes(newString, "UTF-8"))

print("Программа завершила свою работу.")
