## THIS FILE WAS AUTOMATICALLY GENERATED ##
from garden_ai import GardenClient, Model, Pipeline, step
import typing

client = GardenClient()

@step
def run_inference(
    z: object,
    pos: object,
    batch: object,
    model=Model("willengler@uchicago.edu/physnet-qm9-new"),
) -> object:
    model._lazy_load_model()
    inner_model = model._wrapped_model
    inner_model.to("cpu")
    inner_model.eval()
    return inner_model.forward(z.long().to("cpu"), pos.to("cpu"), batch.long().to("cpu"))

# the step functions will be composed in order by the pipeline:
ALL_STEPS = (
    run_inference,
)

################################### PIPELINE ####################################

zpve_predict: Pipeline = client.create_pipeline(
    title="Predict Zero Point Vibrational Energy with Physnet",
    steps=ALL_STEPS,
    authors=['Hyun Park', 'Eliu Huerta'],
    contributors=[],
    description="Proof of concept demo of Hyun et al's AI framework on Garden",
    version="0.0.1",
    year=2023,
    tags=[],
    doi="10.23677/wwxa-8783",  # WARNING: DO NOT EDIT DOI
)