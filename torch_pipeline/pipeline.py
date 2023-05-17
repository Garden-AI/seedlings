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
    model=Model("willengler@uchicago.edu-pytorch-example/1"),
) -> object:
    return model.predict(input_tensor)

# the step functions will be composed in order by the pipeline:
ALL_STEPS = (
    run_inference,
)

REQUIREMENTS_FILE = "/Users/will/Sandbox/seedlings/torch_pipeline/requirements.txt"  # to specify additional dependencies, replace `None`
                          # with an "/absolute/path/to/requirements.txt"

################################### PIPELINE ####################################

torch_pipeline: Pipeline = client.create_pipeline(
    title="Pytorch Example",
    steps=ALL_STEPS,
    requirements_file=REQUIREMENTS_FILE,
    authors=['Will Engler'],
    contributors=[],
    description="",
    version="0.0.1",
    year=2023,
    tags=[],
    uuid="aa2273f1-4a04-4807-81e8-cbd928824e92",  # WARNING: DO NOT EDIT UUID
)