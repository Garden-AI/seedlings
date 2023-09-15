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
def do_correct_work(
    n_seeds: object,
    seed_length: object,
) -> object:
    import tensorflow as tf
    import os
    import huggingface_hub as hfh
    from peptimizer.utils.utils_cpp import cpp_predictor, cpp_optimizer, cpp_generator
    from peptimizer.utils.utils_common.activator import Activation

    if not os.path.exists('hf_model'):
        os.mkdir("hf_model")
    if not os.path.exists('hf_data'):
        os.mkdir("hf_data")

    for model_file_name in ['cpp_generator.hdf5', 'cpp_predictor.hdf5']:
        hfh.hf_hub_download(repo_id="willengler-uc/peptimizer-test", filename=model_file_name, local_dir="hf_model")
    for data_file_name in ['cpp_generator_dataset.txt', 'cpp_predictor_dataset.csv', 'cpp_smiles.json', 'cpp_predictor_dataset_stats.json']:
        hfh.hf_hub_download(repo_id="willengler-uc/peptimizer-test", filename=data_file_name, local_dir="hf_data")

    os.environ['CUDA_VISIBLE_DEVICES'] = '0'

    GENERATOR_DATA_PATH = './hf_data/cpp_generator_dataset.txt'
    GENERATOR_MODEL_PATH = './hf_model/cpp_generator.hdf5'
    SEED_SEQ_LENGTH = 10

    PREDICTOR_DATA_PATH = './hf_data/cpp_predictor_dataset.csv'
    PREDICTOR_MODEL_PATH = './hf_model/cpp_predictor.hdf5'
    PREDICTOR_STATS_PATH = './hf_data/cpp_predictor_dataset_stats.json'

    SMILES_PATH = './hf_data/cpp_smiles.json'
    FP_RADIUS = 3
    FP_BITS = 1024
    SEQ_MAX = 108

    optimizer = cpp_optimizer.Optimizer(
        model_path = PREDICTOR_MODEL_PATH,
        data_path = PREDICTOR_DATA_PATH,
        smiles_path = SMILES_PATH,
        stats_path = PREDICTOR_STATS_PATH,
        fp_radius = FP_RADIUS,
        fp_bits = FP_BITS,
        seq_max = SEQ_MAX
    )
    generator = cpp_generator.Generator(
        model_path = GENERATOR_MODEL_PATH,
        data_path = GENERATOR_DATA_PATH,
        seq_length = SEED_SEQ_LENGTH
    )
    list_seeds = generator.generate_seed(n_seeds = n_seeds, seed_length = seed_length)
    df = optimizer.optimize(list_seeds)
    return df

    # Grab the model binaries.
    # Pull the library code in ... somehow


# the step functions will be composed in order by the pipeline:
ALL_STEPS = (
    do_correct_work,
)

# REQUIREMENTS_`FILE = None  # to specify additional dependencies, replace `None`
                          # with an "/absolute/path/to/requirements.txt"

################################### PIPELINE ####################################

gen_cpp_seqs: Pipeline = client.create_pipeline(
    title="Generate cell penetrating peptide sequences",
    steps=ALL_STEPS,
    # requirements_file=REQUIREMENTS_FILE,
    authors=['Will Engler'],
    contributors=[],
    container_uuid="371a85f3-9523-4ab1-9ae5-7a828b7806c1",
    description="",
    version="0.0.1",
    year=2023,
    tags=[],
    doi="10.23677/0cjb-qk08",  # WARNING: DO NOT EDIT DOI
)