FROM python:3.10

WORKDIR /usr/app

COPY ./voronoi ./
COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD [ "python", "./voronoi/diagrams_voronoi.py"]