FROM prefecthq/prefect:1.2.3-python3.8
RUN /usr/local/bin/python -m pip install --upgrade pip
WORKDIR /opt/prefect
COPY requirements.txt .
RUN pip install -r requirements.txt