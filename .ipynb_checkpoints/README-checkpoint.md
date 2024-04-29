# Proyecto de Machine Learning con datos de COVID-19 México

Este proyecto forma parte de la materia de Machine Learning de la Maestría en Ciencia de Datos de la Universidad de Sonora. Se utilizan los datos abiertos del gobierno de México sobre los casos de COVID-19. Estos datos pueden encontrarse en la siguiente liga: [Información sobre casos de COVID-19 en México](https://datos.gob.mx/busca/dataset/informacion-referente-a-casos-covid-19-en-mexico).

### Integrantes del equipo

- José Barreras
- Luis Ortiz
- Vesna Pivac

## Problema a abordar
- ¿Que problema se plantea resolver? En términos que todo mundo entienda.
- ¿Porqué es un problema importante para la institución/organización/empresa?
- ¿Cuales son las métricas para medir el impacto de la solución una vez obtenida?
- ¿Que problema de aprendizaje implica resolver? Si es clasificación, especificar cuales serían las clases.
- ¿Qué metricas permiten medir la calidad del modelo de aprendizaje? ¿Cuales son sus valores deseables?
- ¿Como están alineadas las métricas de la calidad del modelo con las métricas de impacto de la solución? De preferencia tratar de cuantificar.

Utilizando los datos abiertos publicados por el gobierno de México acerca de los casos de COVID-19 tratamos de analizar y predecir la posibilidad de fallecimiento de un paciente según la información disponible. 
La información es publicada por el Sistema de Vigilancia Epidemiológica de Enfermedades Respiratoria Viral. Incluye información de cada paciente registrado. La información que resulta valiosa para nosotros es la sintomatología del paciente, que nos describe con certeza la situación biológica del individuo. Al compararlo con todos los registros, esperamos obtener la posibilidad de fallecimiento del afectado en cuestión. 

Cómo podemos fácilmente deducir, es un problema bastante valioso para el sistema de salud nacional. Puede funcionar cómo una especie de semáforo de riesgo. La limitada asistencia médica disponible, sería más eficiente al distribuir sus esfuerzos. Prestando especial atención a pacientes con mayor riesgo de fallecimiento. 
De ninguna manera esperamos reemplazar una evaluación y opinión experta de un médico tratante. Esperamos construir una herramienta que sirva de apoyo y/o complemento para la evaluación médica profesional. 

Las métrica principal que se pretende afectar es la del número de fallecimientos en el país. Esperamos que con una atención más certera y a tiempo, se puedan evitar fallecimientos. La naturaleza del proyecto hace que sea difícil la evaluación: Un diagnóstico correcto (alta probabilidad de fallecimiento), dispararía especial atención al paciente, lo cuál esperamos que pueda evitar tal fallecimiento. Por lo que una predicción exitosa de nuestra parte (un paciente con alta probabilidad de muerte), preferiblemente dispararía atención especial, que en caso de tener éxito, evitaría tal fallecimiento. 

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
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │   ├── processed      <- Data dictionaries, manuals, and all other explanatory materials of processed data
    │       └── Diccionario.xlsx    <- Processed Data dictionary
    │   └── raw            <- Data dictionaries, manuals, and all other explanatory materials of raw data
    │       ├── Catalogos.xlsx      <- Raw Data catalog
    │       ├── Diccionario.xlsx    <- Raw Data dictionary
    │       └── Actualizaciones en la presentación de información referente a casos de COVID.pdf <- Info of raw data
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
