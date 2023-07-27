FROM python:3
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /django-studio
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .