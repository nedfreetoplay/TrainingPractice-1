import cv2
import os

cropping = False
cropped = []
refPt = []
window_name = "Image Cropper"

def click_and_crop(event, x, y, flags, param):
    global refPt, cropping

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True

    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False

        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow(window_name, image)
        cropped.append(refPt)
        refPt = []
print("-----------------------------------------")
print("Данная программа позволяет выделять на изображении объекты для выборки\nВыбранный материал помещается в папку Cropped в директории программы")
print("Управление:\nS - Сохраняет все выбранные объекты\nSpace - Пропускает изображение(Даже если были какие-либо выделения)")
print("Для выделения необходимо зажать левую кнопку мыши и не отпускать до полного выделения объекта")
print("P.S. Выделенные объекты нельзя убирать(Недоработка)")
print("-----------------------------------------\n")
print("Напишите директорию для обработки изображений:")
direct = input()

print("С какого номера изображения будем начинать?: ", end='')
counter = int(input())

files = os.listdir(direct)

images = []
howImage = 0

for val in files:
    if(val.find(".jpg") or val.find(".jpeg") or val.find(".png")):
        images.append(val)
imagesSize = len(images)

for imageName in images:

    image = cv2.imread(direct + "\\" + imageName)
    clone = image.copy()
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, click_and_crop)

    cropped = []

    while True:
        cv2.imshow(window_name, image)
        key = cv2.waitKey(1) & 0xFF

        if key == ord(" "):
            cropped = []
            break

        elif key == ord("s"):
            break

    dr = direct + "\Cropped\\"
    if not os.path.isdir(dr):
        try:
            os.mkdir(dr)
        except OSError:
            print("Создать директорию %s не удалось" % dr)
        else:
            print("Успешно создана директория %s" % dr)
    for img in cropped:
        cropImage = clone[img[0][1]:img[1][1], img[0][0]:img[1][0]]
        cv2.imwrite(dr + str(counter) + ".jpg", cropImage)
        counter = counter + 1
    howImage = howImage + 1

cv2.destroyAllWindows()
