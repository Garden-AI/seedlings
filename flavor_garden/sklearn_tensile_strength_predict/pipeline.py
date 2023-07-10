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
def preprocessing_step(composition_string: str) -> object:
    """
    Example input: Fe0.620C0.000953Mn0.000521Si0.00102Cr0.000110Ni0.192Mo0.0176V0.000112Nb0.0000616Co0.146Al0.00318Ti0.0185
    """
    import re
    import pandas as pd

    atomic_weights = {
        'Fe': 55.845, 'C': 12.011, 'Mn': 54.938045, 'Si': 28.0855, 'Cr': 51.9961, 
        'Ni': 58.6934, 'Mo': 95.96, 'V': 50.9415, 'Nb': 92.90638, 'Co': 58.933195, 
        'W': 183.84, 'Al': 26.9815386, 'Ti': 47.867, "N": 28.014
    }
    elements_to_show = ['c', 'mn', 'si', 'cr', 'ni', 'mo', 'v', 'n', 'nb', 'co', 'w', 'al', 'ti']

    # Parse the composition string
    composition = re.findall(r'([A-Z][a-z]?)(\d+\.\d+)', composition_string)
    elements, fractions = zip(*composition)
    fractions = [float(f) for f in fractions]
    
    # Calculate the weights
    weights = [f * atomic_weights[e] for e, f in zip(elements, fractions)]
    total_weight = sum(weights)
    
    # Calculate weight percentages
    weight_percentages = [w / total_weight * 100 for w in weights]
    
    lowercase_elements = [e.lower() for e in elements]
    missing_elements = []
    for e in elements_to_show:
      if e not in lowercase_elements:
        missing_elements.append(e)
    lowercase_elements += missing_elements
    weight_percentages += [0.0] * len(missing_elements)
    
    
    # Create DataFrame
    df = pd.DataFrame([weight_percentages], columns=lowercase_elements)
    df = df.drop(["fe"], axis=1)
    df = df[elements_to_show]
    return df

@step
def run_inference(
    df: object,
    model=Model('willengler@uchicago.edu/steel_test_2'),
) -> object:
    return model.predict(df)

# the step functions will be composed in order by the pipeline:
ALL_STEPS = (
    preprocessing_step,
    run_inference,
)

REQUIREMENTS_FILE = "/Users/will/Sandbox/seedlings/flavor_garden/sklearn_tensile_strength_predict/requirements.txt"  # to specify additional dependencies, replace `None`

################################### PIPELINE ####################################

sklearn_tensile_strength_predict: Pipeline = client.create_pipeline(
    title="Steel Alloy Tensile Strength Prediction",
    steps=ALL_STEPS,
    requirements_file=REQUIREMENTS_FILE,
    authors=['Will Engler'],
    contributors=[],
    description="Pipeline for predicting the tensile strength (in MPa) of different compositions of alloy steels",
    version="0.0.1",
    year=2023,
    tags=[],
    doi="10.23677/etya-kq52",  # WARNING: DO NOT EDIT DOI
)