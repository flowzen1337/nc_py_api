FROM python:3.11.4-bookworm

COPY requirements.txt /
ADD main.py /app/
ADD nc_py_api /app/nc_py_api

RUN \
    apt-get update && \
    apt-get install -y \
    ffmpeg libsm6 libxext6 gifsicle

RUN \
  python3 -m pip install -r requirements.txt

WORKDIR /app
ENTRYPOINT ["python3", "main.py"]
