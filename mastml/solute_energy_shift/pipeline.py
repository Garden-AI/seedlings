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

# example step using the decorator:
@step
def preprocessing_step(input_data: object) -> object:
    from mastml.feature_generators import ElementalFeatureGenerator
    X_test = input_data["X_test"]
    y = input_data["y"]
    X, y = ElementalFeatureGenerator(composition_df=X_test['Material compositions joined'], 
                                 feature_types=['composition_avg', 'arithmetic_avg', 'max', 'min', 'difference'], 
                                 remove_constant_columns=True).evaluate(X=X, y=y, savepath="./foo", make_new_dir=True)
    return X


@step()
def another_step(data: object) -> object:
    # TODO
    pass


@step
def run_inference(
    input_arg: object
    # model=Model("YOUR MODEL's NAME HERE"),
) -> object:
    pass

# the step functions will be composed in order by the pipeline:
ALL_STEPS = (
    preprocessing_step,
    #another_step,
    #run_inference,
)

REQUIREMENTS_FILE = "/Users/will/Sandbox/seedlings/mastml/solute_energy_shift/requirements.txt"  # to specify additional dependencies, replace `None`
                          # with an "/absolute/path/to/requirements.txt"

################################### PIPELINE ####################################

solute_energy_shift: Pipeline = client.create_pipeline(
    title="Impurity diffusion predictor",
    steps=ALL_STEPS,
    requirements_file=REQUIREMENTS_FILE,
    python_version="3.10",
    authors=['Will Engler'],
    contributors=[],
    description="",
    version="0.0.1",
    year=2023,
    tags=[],
    uuid="530cf2fa-b4b7-42b9-a150-091c9276495f",  # WARNING: DO NOT EDIT UUID
)