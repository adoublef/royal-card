FROM python:3.9-alpine AS runtime
WORKDIR /code

# prepare python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app ./

ENTRYPOINT ["python", "main.py"]
