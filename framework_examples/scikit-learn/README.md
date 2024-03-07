# Scikit-learn Seedling

This example has three notebooks that show a full example of making a scikit-learn model, publishing it with Garden, and using Garden to run the model remotely.

### Training a model

Garden is for publishing and sharing models, so training models happens out of band. But `Train_Model.ipynb` shows how to train the classic scikit-learn tutorial model for classifying irises.

Then I exported and published my trained model on Hugging Face at `willengler-uc/iris-classifier``.

### Making a Garden entrypoint that invokes the model

I had already used `garden-ai garden create` to make a garden. It has DOI 10.23677/6k5t-v242, which I will use in my notebook.

I use `garden-ai notebook start --base-image=="3.10-sklearn" --requirements=requirements.txt` to write a notebook with a function that invokes my scikit-learn model. My model was trained on an earlier version of sklearn than the one included in the container, so I pinned the version in my requirements. I tag the function with `@garden_entrypoint` and specify the garden I'm publishing it to.

Then I say `garden-ai notebook publish iris-classifier.ipynb` to publish my entrypoint.

### Running the model

`Run_Entrypoint.ipynb` shows how to remotely run the entrypoint I just published.