FROM python:3.11-alpine as base
FROM base as builder
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM base
COPY --from=builder /root/.local /root/.local
WORKDIR /code
COPY bot.py .
ENV PATH=/root/.local:$PATH
CMD ["python", "-u", "./bot.py"]