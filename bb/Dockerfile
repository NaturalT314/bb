FROM python:3.10.12

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN chmod +x /app/script.sh

EXPOSE 8000

CMD ["/app/script.sh"]