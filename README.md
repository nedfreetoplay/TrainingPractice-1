# TrainingPractice-1
Обучение каскаду хаара

Bad(Папка) - Изображение отрицательной выборки(~1200 изображений)

Good(Папка) - Изображения положительной выборки(~600 изображений)

haarcascade(Папка) - Готовые каскады(1 каскад, который был с генерирован мною)

Материал(Папка) - Материал, который был использовал для создания положительной выборки

Программы(Папка) - Программы, которые я написал для создания и использования каскада.

Good.dat - Хронит ссылки на все положительные изображения

Bad - Хронит ссылки на все отрицательные изображения

CreateCascade.bat - Быстрое создание каскада

CreateSamples.bat - Создание samples

samples.vec - обработанные положительные изображения

Программы с описанием:

ImageCollector.py - Данная программа компанует изображения в файл: Good.dat, для Каскада Хаара.

ImageCollectorBad.py - Данная программа компанует изображения в файл: Bad.dat, для Каскада Хаара.

ImageCropper.py - Данная программа позволяет выделять на изображении объекты для выборки. Выбранный материал помещается в папку Cropped в директории программы

ImageDownloader.py - Программа скачивает список изображений с сайта

RGBToGray.py - Данная программа преобразовывает папку с изображениями в градацию серого.
