This seedling is a work in progress. Leaving some quick notes here on how I got the first pipeline running:

## Custom Container

I built a container using the Dockerfile in this directory. I hosted it on Garden's AWS ECR repo and then registered it with Globus Compute. It has UUID d834134f-4a9d-47be-8886-5c78806f6f78. I then hardcoded that UUID into my local Garden install to register the pipeline against the custom container.

## Uploading the Model

I also couldn't get all the Torch addon requirements installed on my machine needed to serialize/deserialize the model locally and upload it as an MLFlow package. So I made a prototype branch that let me register it in memory from Hyun/Eliu's notebook: https://github.com/Garden-AI/garden/tree/will/register-model-in-memory

There was also a weird issue with the entrypoints library that I think gets installed by the ai4molcryst_argonne repo? That causes a bug deep in MLFlow that prevents model upload. I kludged over that in the notebook context with ...

```
!sed -i "s|if folder.rstrip('/\\\\').endswith('.egg'):|if str(folder).rstrip('/\\\\').endswith('.egg'):|g" /usr/local/lib/python3.10/dist-packages/entrypoints.py
```