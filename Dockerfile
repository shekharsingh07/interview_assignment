FROM python:3

# Setting up work directory in container
WORKDIR .

# copy source files into work dir
COPY app/ .

# copy dependencies into work dir
COPY requirements.txt .			

# install dependencies
RUN pip install -r requirements.txt	

# setting entrypoint
ENTRYPOINT [ "python", "./app/factorial-digits.py"]
