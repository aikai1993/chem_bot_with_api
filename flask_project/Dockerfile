FROM python:3.12

WORKDIR /app

COPY requierments.txt .

RUN pip install --no-cache-dir -r requierments.txt

COPY . .

CMD ["flask", "--app", "main", "run", "--host=0.0.0.0", "--debug"]