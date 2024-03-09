FROM --platform=linux/amd64 python:3.12.2-alpine3.19

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk update && apk add --no-cache \
	libpq-dev \
	gcc \
	bash

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000

COPY . .
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "budgeting_site.wsgi"]
