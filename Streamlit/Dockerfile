FROM python:3.7

WORKDIR /Streamlit

COPY requirements.txt ./requirements.txt


RUN pip3 install -r requirements.txt

EXPOSE 8080

COPY . /Streamlit


CMD streamlit run --server.port 8080 --server.enableCORS false edsa_recommender.py
