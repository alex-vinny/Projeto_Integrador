FROM python

WORKDIR /app

#EXPOSE 5000

COPY . .

RUN pip install -r requirements.txt

#ENV PORT 5000
## descomentar para publicar no heroku
CMD python manage.py runserver 0:$PORT