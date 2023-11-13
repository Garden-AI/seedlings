# Scikit-learn Seedling

This example has three notebooks that show a full example of making a scikit-learn model, publishing it with Garden, and using Garden to run the model remotely.

### Training a model

Garden is for publishing and sharing models, so training models happens out of band. But `Train_Model.ipynb` shows how to train the classic scikit-learn tutorial model for classifying irises.

Then I exported and published my trained model on Hugging Face at `willengler-uc/iris-classifier``.

### Making a Garden pipeline that invokes the model

I had already used `garden-ai garden create` to make a garden. It has DOI 10.23677/6k5t-v242, which I will use in my notebook.

I use `garden-ai notebook start --base-image=="3.10-sklearn"` to write a notebook with a function that invokes my scikit-learn model. I tag the function with `@garden_pipeline` and specify the garden I'm publishing it to.

Then I say `garden-ai notebook publish iris-classifier.ipynb` to publish my pipeline.

### Running the Garden pipeline

`Run_Pipeline.ipynb` shows how to remotely run the pipeline I just published.