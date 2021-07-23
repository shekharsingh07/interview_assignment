FROM python:3

WORKDIR .	# Setting up work directory in container

COPY app/ .				# copy files into work dir

COPY requirements.txt .			# copy dependencies into work dir

RUN pip install -r requirements.txt	# install dependencies

CMD [ "python", "./app/factorial-digits.py"]	# setting entrypoint
