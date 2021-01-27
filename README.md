Пример отправки запроса curl:

curl -i -X POST -H "Content-Type: multipart/form-data" -F "file_to_check=@path_to_file" http://localhost:5000/check_faces

где path_to_file - путь к обрабатываемому изображению
