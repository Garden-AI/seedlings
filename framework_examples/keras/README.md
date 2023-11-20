# TensorFlow/Keras Seedling

This example has three notebooks that show a full example of making a Keras model, publishing it with Garden, and using Garden to run the model remotely.

### Training a model

Garden is for publishing and sharing models, so training models happens out of band. But `Keras_MNIST_Train.ipynb` shows how to train a neural net for the classic MNIST digit classification problem.

I published the trained model weights plus the Python class that defines the network structure to Hugging Face at `willengler-uc/keras-mnist``.

### Making a Garden pipeline that invokes the model

I had already used `garden-ai garden create` to make a garden. It has DOI 10.23677/j4cg-6427, which I will use in my notebook.

I use `garden-ai notebook start --base-image=="3.10-tensorflow"` to write a notebook called `tf-mnist.ipynb` with a function that invokes my Keras model. I tag the function with `@garden_pipeline` and specify the garden I'm publishing it to.

Then I say `garden-ai notebook publish tf-mnist.ipynb` to publish my pipeline.

### Running the Garden pipeline

`Keras_MNIST_remote_inference.ipynb` shows how to remotely run the pipeline I just published.