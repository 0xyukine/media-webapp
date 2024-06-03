FROM python:3

WORKDIR /python
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ADD requirements.txt .
RUN pip install -r requirements.txt
COPY . .

#CMD ["flask","run"]

CMD ["python","-u","-m","flask","--app","main.py","run","--host=0.0.0.0"]
# CMD ["python","-u","./main.py"]
