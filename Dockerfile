FROM python:3.9

ENV PYTHONUNBUFFERED 1

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip && pip install -r requirements.txt
RUN python manage.py collectstatic --no-input

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "bmiwebsite.wsgi:application"]