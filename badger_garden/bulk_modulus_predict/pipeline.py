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
def preprocessing_step(input_df: object) -> object:
    """ """
    import numpy as np
    import pandas as pd
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()

    # Set the required attributes. In your case, you would replace these arrays with the actual values from the original preprocessor.
    scaler.n_samples_seen_ = 4896
    scaler.feature_names_in_ = np.array(['n_ws^third_composition_average',
        'GSenergy_pa_composition_average',
        'ICSDVolume_composition_average', 'GSenergy_pa_arithmetic_average',
        'ThermalExpansionCoefficient_difference',
        'IsSimpleCubic_composition_average',
        'HeatVaporization_composition_average',
        'GSvolume_pa_composition_average', 'ElasticModulus_min_value',
        'ThermalExpansionCoefficient_composition_average',
        'HeatVaporization_max_value', 'BoilingT_composition_average',
        'Electronegativity_composition_average',
        'HeatFusion_composition_average', 'AtomicVolume_difference',
        'BCCenergy_pa_composition_average', 'MeltingT_max_value',
        'MiracleRadius_min_value', 'BCCvolume_pa_composition_average',
        'SecondIonizationEnergy_min_value'], dtype=object)
    scaler.mean_ = np.array([ 1.21300764e+00, -5.05388885e+00,  2.34422807e+01, -5.10699681e+00,
        1.50472263e+02,  7.26221029e-02,  2.72911690e+02,  2.21259957e+01,
        4.96978350e+01,  9.61846637e+01,  4.23386429e+02,  2.57616094e+03,
        1.95325000e+00,  1.75144805e+01,  3.66351124e+03, -4.54080764e+00,
        1.97419950e+03,  1.16809436e+02,  2.05320818e+01,  1.43793995e+01])
    scaler.var_ = np.array([1.89939907e-01, 4.19623230e+00, 7.73563701e+01, 4.00702775e+00,
        1.21057246e+05, 3.83157988e-02, 2.34218297e+04, 7.73156327e+01,
        3.82040699e+03, 4.86934041e+04, 3.14732307e+04, 1.26055519e+06,
        1.65712626e-01, 1.96736665e+02, 5.42994046e+07, 3.83905099e+00,
        6.50087192e+05, 9.54723694e+02, 7.13527608e+01, 1.66565870e+01])
    scaler.scale_ = np.sqrt(scaler.var_)
    scaler.n_features_in_ = 20
    scaler.with_mean = True
    scaler.with_std = True

    transformed = scaler.transform(input_df)
    return pd.DataFrame(transformed, columns=input_df.columns)


@step
def run_inference(
    input_df: object,
    m=Model("willengler@uchicago.edu/uw-vrh-predictor"),
) -> object:
    import numpy as np
    import pandas as pd

    recal_params = {
        "a": [0.9011436139458698],
        "b": [-0.5078164767483223]
    }
    try:
        m.predict(input_df)
    except:
        pass
    model = m.model._model_impl
    try:
        model_name = model.model.__class__.__name__
    except:
        model_name = model.__class__
    yerr = list()
    ensemble_models = ['RandomForestRegressor','GradientBoostingRegressor','BaggingRegressor','ExtraTreesRegressor','AdaBoostRegressor']
    if model_name in ensemble_models:
        X_aslist = input_df.values.tolist()
        for x in range(len(X_aslist)):
            preds = list()
            if model_name == 'RandomForestRegressor':
                for pred in model.model.estimators_:
                    preds.append(pred.predict(np.array(X_aslist[x]).reshape(1, -1))[0])
            elif model_name == 'BaggingRegressor':
                for pred in model.model.estimators_:
                    preds.append(pred.predict(np.array(X_aslist[x]).reshape(1, -1))[0])
            elif model_name == 'ExtraTreesRegressor':
                for pred in model.model.estimators_:
                    preds.append(pred.predict(np.array(X_aslist[x]).reshape(1, -1))[0])
            elif model_name == 'GradientBoostingRegressor':
                for pred in model.model.estimators_.tolist():
                    preds.append(pred[0].predict(np.array(X_aslist[x]).reshape(1, -1))[0])
            elif model_name == 'AdaBoostRegressor':
                for pred in model.model.estimators_:
                    preds.append(pred.predict(np.array(X_aslist[x]).reshape(1, -1))[0])
            if recal_params is not None:
                yerr.append(recal_params['a'][0]*np.std(preds)+recal_params['b'][0])
            else:
                yerr.append(np.std(preds))

    if model_name == 'GaussianProcessRegressor':
        y_pred_new, yerr = model.model.predict(input_df, return_std=True)
    else:
        y_pred_new = model.predict(input_df)

    if len(yerr) > 0:
        pred_df = pd.DataFrame(y_pred_new, columns=['y_pred'])
        pred_df['y_err'] = yerr
    else:
        pred_df = pd.DataFrame(y_pred_new, columns=['y_pred'])

    return pred_df

# the step functions will be composed in order by the pipeline:
ALL_STEPS = (
    preprocessing_step,
    run_inference,
)

################################### PIPELINE ####################################

bulk_modulus_predict: Pipeline = client.create_pipeline(
    title="CMG Bulk Modulus Prediction",
    steps=ALL_STEPS,
    authors=['Doyeon Kim'],
    pip_dependencies=["mastml==3.1.7"],
    description="Proof of concept use of a MAST-ML model in Garden",
    version="0.0.1",
    year=2023,
    tags=[],
    doi="10.23677/08d3-9w95",  # WARNING: DO NOT EDIT DOI
)