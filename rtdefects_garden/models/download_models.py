from pathlib import Path
import numpy as np
import requests

all_models = ["segment-model.h5", "small_voids_031023.pth", "voids_segmentation_030323.pth", "voids_segmentation_091321.pth"]

for model_name in all_models:
    save_path = f"./models/{model_name}"

    with requests.get(f"https://g-29c18.fd635.8443.data.globus.org/ivem/models/{model_name}", stream=True) as r:
        r.raise_for_status()
        with open(save_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
