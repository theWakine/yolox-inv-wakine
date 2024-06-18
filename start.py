import subprocess

commands = [
    ["python3", "rframe.py", "--frames=120,130,140", "-i", "assets/develop_streem.ts"],
    ["python3", "tools/demo.py", "image", "-n", "yolox-s", "-c", "weights/yolox_s.pth", "--path", "assets/frame_120.jpg", "--conf", "0.25", "--nms", "0.45", "--tsize", "640", "--save_result", "--device", "cpu"],
    ["python3", "tools/demo.py", "image", "-n", "yolox-s", "-c", "weights/yolox_s.pth", "--path", "assets/frame_130.jpg", "--conf", "0.25", "--nms", "0.45", "--tsize", "640", "--save_result", "--device", "cpu"],
    ["python3", "tools/demo.py", "image", "-n", "yolox-s", "-c", "weights/yolox_s.pth", "--path", "assets/frame_140.jpg", "--conf", "0.25", "--nms", "0.45", "--tsize", "640", "--save_result", "--device", "cpu"],
    ["python3", "tools/demo.py", "video", "-n", "yolox-s", "-c", "weights/yolox_s.pth", "--path", "assets/develop_streem.ts", "--conf", "0.25", "--nms", "0.45", "--tsize", "640", "--save_result", "--device", "cpu"]
]

processes = []

for command in commands:
    print(f"Запуск команды: {command}")
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.DEVNULL, text=True)
    processes.append((command, process))

for command, process in processes:
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Команда {command} завершилась с ошибкой: {stderr}")
    else:
        print(f"Команда {command} выполнена успешно: {stdout}")
