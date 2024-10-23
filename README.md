Sratring guide:

1. git clone https://github.com/theWakine/yolox-inv-wakine.git

2. Скачать модель yolox_s.pth здесь -> https://github.com/Megvii-BaseDetection/YOLOX?tab=readme-ov-file и вставить его в папку weights

3. docker-compose up --build -d 

4. docker-compose exec -it yolox-app-1 /bin/bash

5. Данные обработанные через данную программу лежат в папке /app/YOLOX_outputs
