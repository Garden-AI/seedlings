## THIS FILE WAS AUTOMATICALLY GENERATED ##
from garden_ai import GardenClient, Model, Pipeline, step
import typing

client = GardenClient()
##################################### STEPS #####################################

@step
def generate_peptides(
    n_seeds: object,
    seed_length: object,
) -> object:
    import tensorflow as tf
    import os
    import huggingface_hub as hfh
    from peptimizer.utils.utils_cpp import cpp_optimizer, cpp_generator

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

ALL_STEPS = (
    generate_peptides,
)

################################### PIPELINE ####################################

gen_cpp_seqs: Pipeline = client.create_pipeline(
    title="Generate cell penetrating peptide sequences",
    steps=ALL_STEPS,
    authors=['Will Engler'],
    contributors=[],
    container_uuid="371a85f3-9523-4ab1-9ae5-7a828b7806c1",
    description="",
    version="0.0.1",
    year=2023,
    tags=[],
    doi="10.23677/0cjb-qk08",  # WARNING: DO NOT EDIT DOI
)