Папка build содержит собранные файлы проекта готовые для использования на сервере.
Папка src содержит исходные файлы для разработки проекта.

Внесение изменений должно происходить в файлах из папки src, после запуска проекта.


Что бы запустить проект установите node если его нет.

gulp serv - команда запуска проекта.

gulp clean - -команда очистки папки build(удаление всех файлов)

gulp - собирает весь проект

!! если проект уже собран, но вы хотите пересобрать его, что сначала обязательно выполните команду gulp clean

gulp css - собрать файлы css

gulp js - собрать файлы js

gulp img - собрать картинки 
 
gulp fonts - собрать шрифты

gulp pages - собрать до страницы

gulp html - собрать главную страницу

gulp server - запускает сервер проекта

gulp watch - запускает команду отслеживания изменений в файлах
