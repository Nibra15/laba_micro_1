
FROM python:3.12


WORKDIR /app


COPY ./main.py /app


RUN pip install --no-cache-dir fastapi uvicorn


EXPOSE 6080


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6080"]
