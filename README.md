# Proyecto de Machine Learning con datos de COVID-19 México

Este proyecto forma parte de la materia de Machine Learning de la Maestría en Ciencia de Datos de la Universidad de Sonora. Se utilizan los datos abiertos del gobierno de México sobre los casos de COVID-19. Estos datos pueden encontrarse en la siguiente liga: [Información sobre casos de COVID-19 en México](https://datos.gob.mx/busca/dataset/informacion-referente-a-casos-covid-19-en-mexico).

## Integrantes del equipo

- José Barreras
- Luis Ortiz
- Vesna Pivac


## Instructions
1. Clone the repo.
2. Run `make dirs` to create the missing parts of the directory structure described below.
3. *Optional:* Run `make virtualenv` to create a python virtual environment. Skip if using conda or some other env manager.
   1. Run `source env/bin/activate` to activate the virtualenv.
4. Run `make requirements` to install required python packages.
5. Put the raw data in `data/raw`.
6. To save the raw data to the DVC cache, run `dvc add data/raw`
7. Edit the code files to your heart's desire.
8. Process your data, train and evaluate your model using `dvc repro` or `make reproduce`
9. To run the pre-commit hooks, run `make pre-commit-install`
10. For setting up data validation tests, run `make setup-setup-data-validation`
11. For **running** the data validation tests, run `make run-data-validation`
12. When you're happy with the result, commit files (including .dvc files) to git.

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make dirs` or `make clean`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   ├── raw.dvc        <- DVC file that tracks the raw data
    │   └── raw            <- The original, immutable data dump
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │   └── metrics.txt    <- Relevant metrics after evaluating the model.
    │   └── training_metrics.txt    <- Relevant metrics from training the model.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── features           <- Scripts to download or generate data
    │   │   ├── build_features.ipynb  <- Notebook that cleans and processes raw data
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   ├── Descarga_de_datos.ipynb  <- Notebook that downloads raw data
    │   │   ├── make_dataset.py
    │   │   └── data_validation.py  <- Script to run data integrity checks
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    ├── .pre-commit-config.yaml  <- pre-commit hooks file with selected hooks for the projects.
    ├── dvc.lock           <- The version definition of each dependency, stage, and output from the 
    │                         data pipeline.
    └── dvc.yaml           <- Defining the data pipeline stages, dependencies, and outputs.


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>


---

To create a project like this, just go to https://dagshub.com/repo/create and select the **Cookiecutter DVC** project template.

Made with 🐶 by [DAGsHub](https://dagshub.com/).
