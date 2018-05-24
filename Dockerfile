FROM alpine:3.7
COPY requirements.txt /src/requirements.txt
COPY app.py /src
COPY model /src/model
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    pip3 install --upgrade pip && \
    pip3 install -r /src/requirements.txt
ENV FLASK_ENV production
CMD python3 /src/app.py
