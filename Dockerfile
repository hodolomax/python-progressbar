FROM python:3.7.4-slim
COPY . ./app
WORKDIR /app
RUN apt-get update
RUN pip3 install tqdm
RUN export PYTHONPATH=/app
ENV PYTHONPATH=/app
CMD python3 -u ./progress-bar.py
