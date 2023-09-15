FROM docker.io/bengal1/funcx_bc7c6ce2-cc71-4c53-ad0c-fa0b3ad65854:latest

USER root

RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get clean

RUN pip install garden-ai
RUN pip install rdkit
RUN pip install textdistance
RUN pip install pandas==1.5.3
RUN pip install tensorflow==2.13.0
RUN pip install mlflow-skinny
RUN pip install dill==0.3.6
RUN pip install huggingface-hub
RUN pip install git+https://github.com/WillEngler/peptimizer.git

CMD ["sleep", "infinity"]