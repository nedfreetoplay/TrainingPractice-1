import cv2
import os

print("-----------------------------------------")
print("Данная программа показывает обработанные изображения каскадом")
print("Управление:\nSpace - Следующее изображение")
print("-----------------------------------------\n")

print("Введите полный путь до каскада: ")
wood_cascade = cv2.CascadeClassifier(input())
print("Введите папку с изображениями для поиска объектов: ")
path = input()

files = os.listdir(path)

images = []
for file in files:
    if (file.find(".jpg") or file.find(".jpeg") or file.find(".png")):
        images.append(file)

for i in range(0, len(images)):
    originalImage = cv2.imread(path + "\\" + images[i])
    gray = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    wCascade = wood_cascade.detectMultiScale(gray, 1.1, 5)
    for (x, y, w, h) in wCascade:
        cv2.rectangle(originalImage, (x, y), (x+w, y+h), (255, 0, 0), 2)
    while True:
        cv2.imshow('img', originalImage)
        key = cv2.waitKey(1) & 0xFF

        if key == ord(" "):
            break

cv2.destroyAllWindows()








