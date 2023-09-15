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

# RUN pip install einops curtsies p_tqdm pathlib scikit-image argparse wandb cairosvg h5py pynvml jupyter fast-ml faerun
# RUN pip install "deephyper[hps]"

# RUN conda install -c conda-forge pymatgen openbabel -y
# RUN pip install torch==1.13.1 torchvision --extra-index-url https://download.pytorch.org/whl/cu117 timm
# RUN pip install torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-1.13.0+cu117.html
# RUN pip install torch_geometric
# RUN conda install -c dglteam/label/cu117 dgl

# RUN pip install torchmetrics tqdm transformers wandb apex curtsies fairscale imageio joblib Pillow pytorch_lightning PyYAML ray
# RUN pip install scikit-learn ipykernel docopt seaborn umap-learn plotly dash captum MDAnalysis scikit-tda
# RUN pip install git+https://github.com/tensorflow/docs
# RUN pip install git+https://gitlab.com/hyunp2/ai4molcryst_argonne.git
RUN pip install mlflow-skinny
RUN pip install dill==0.3.6
RUN pip install huggingface-hub
RUN pip install git+https://github.com/WillEngler/peptimizer.git

CMD ["sleep", "infinity"]