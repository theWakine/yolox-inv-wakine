FROM pytorch/pytorch:latest

RUN apt-get update && apt-get install -y ffmpeg cmake build-essential python3-dev git

RUN apt-get update \
     && apt-get install -y \
        libgl1-mesa-glx \
        libx11-xcb1 \
     && apt-get clean all \
     && rm -r /var/lib/apt/lists/*

RUN /opt/conda/bin/conda install --yes \
    astropy \
    matplotlib \
    pandas \
    scikit-learn \
    scikit-image 

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "start.py"]
