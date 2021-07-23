FROM python:3

ADD app/sum_factorial.py /

ADD requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "./app/sum_factorial.py"]
