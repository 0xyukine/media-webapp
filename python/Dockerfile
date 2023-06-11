FROM python:3

WORKDIR /python
ADD requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python","-u","-m","flask","--app","main.py","run"]
# CMD ["python","-u","./main.py"]