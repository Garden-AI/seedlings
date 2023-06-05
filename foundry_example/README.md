# End-to-end Walkthrough Guide

This seedling describes the end-to-end process of publishing work as a Garden.

## Starting with the data

Machine learning work often begins with a dataset, in this example, a published dataset from `foundry-ml` is used. The `dendrite_segmentation.ipynb` notebook walks through the steps to download data from foundry and then train and save a model using that data.

## Publishing to Garden

Taking the model that was trained and saved in the first notebook, we transition to the `garden_publish.ipynb` notebook. From there, the saved model is coverted into a Garden object and registered. The registered model is invoked using a pipeline, and the pipeline is registered and added to a garden. And for the last step, the garden is published to the public search index.

## Admiring your work!

Perform a quick search of the index to verify that the publication step succeeded!
