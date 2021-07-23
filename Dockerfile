FROM python:3

ADD app/factorial-digits.py /

ADD requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "./app/factorial-digits.py"]
