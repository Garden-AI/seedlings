## THIS FILE WAS AUTOMATICALLY GENERATED ##
from garden_ai import GardenClient, Model, Pipeline, step
import typing

client = GardenClient()
##################################### STEPS #####################################
"""
Brief notes on steps (see docs for more detail):

    - you may define your pipeline using as many or as few @steps as you like.

    - Any python function or callable can be made into a step by decorating it
        with `@step`, like below.

    - these functions will be composed in the pipeline (i.e. calling the pipeline
        is equivalent to calling each step in order).

    - the steps MUST have valid type-hints for all positional arguments and
        return types.
      - don't use `Any` or `None` in step annotations
      - these type-hints are used to verify that steps are compatible when
          composing (no checking at runtime)
"""

@step
def run_inference(
    input_tensor: object,
    model=Model("willengler@uchicago.edu/keras-mnist-digit-predict"),
) -> object:
    import tensorflow as tf
    predictions = model.predict(input_tensor)
    return tf.math.argmax(predictions, 1)

# the step functions will be composed in order by the pipeline:
ALL_STEPS = (
    run_inference,
)

################################### PIPELINE ####################################

keras_mnist_digit_predict: Pipeline = client.create_pipeline(
    title="MNIST Digit Prediction in Garden",
    steps=ALL_STEPS,
    pip_dependencies=[
        "tensorflow==2.13.0",
        "mlflow-skinny==2.4.1"
    ],
    authors=['Will Engler'],
    contributors=[],
    description="",
    version="0.0.1",
    year=2023,
    tags=[],
    doi="10.23677/twn4-sw80",  # WARNING: DO NOT EDIT DOI
)