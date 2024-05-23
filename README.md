# Proyecto de Machine Learning con datos de COVID-19 México

Este proyecto forma parte de la materia de Machine Learning de la Maestría en Ciencia de Datos de la Universidad de Sonora. Se utilizan los datos abiertos del gobierno de México sobre los casos de COVID-19. Estos datos pueden encontrarse en la siguiente liga: [Información sobre casos de COVID-19 en México](https://datos.gob.mx/busca/dataset/informacion-referente-a-casos-covid-19-en-mexico).

### Integrantes del equipo

- José Barreras
- Luis Ortiz
- Vesna Pivac

## ¿Que problema se plantea resolver?

Utilizando los datos abiertos publicados por el gobierno de México acerca de los casos de COVID-19, se busca identificar qué pacientes tienen un mayor riesgo de fallecer. Se pretende entrenar un modelo de Aprendizaje Automático que pueda predecir si un paciente fallecerá o no basándose en sus características médicas y demográficas disponibles.

El análisis exploratorio de los datos, junto con las pruebas de entrenamiento y validación de los modelos, promete desvelar qué variables son las más influyentes a la hora de predecir el riesgo de defunción. Esto proporcionará información valiosa para futuras intervenciones y políticas de salud pública. 

## ¿Porqué es un problema importante para la institución/organización/empresa?

Este problema es crucial para México porque permite salvaguardar vidas al identificar a los pacientes con mayor riesgo de fallecer, lo que permite a los profesionales de la salud priorizar cuidados intensivos y tratamientos más agresivos para quienes más lo necesiten. Además, en un contexto de recursos limitados como camas de hospital, ventiladores y personal médico, dirigir estos recursos hacia los pacientes en mayor peligro asegura un uso más eficiente y eficaz.

Un modelo predictivo también facilita una mejor planificación y una respuesta rápida a los picos de la pandemia, preparando con antelación los recursos necesarios y evitando colapsos en el sistema de salud. Al identificar los factores que influyen en la probabilidad de defunción, se pueden diseñar políticas de salud más efectivas y campañas de prevención dirigidas a las poblaciones más vulnerables.

En el ámbito político, mostrar que se están tomando medidas basadas en datos e investigación para combatir la crisis del COVID-19 puede aumentar la confianza pública en las decisiones del gobierno y en las medidas de salud implementadas, fomentando una mayor cooperación y cumplimiento por parte de la ciudadanía.

## ¿Cuales son las métricas para medir el impacto de la solución una vez obtenida?

Para evaluar el impacto de la solución una vez implementada a nivel nacional, se pueden utilizar diversas métricas que reflejan los resultados en el sistema de salud. Un indicador clave es el cambio en la tasa de defunciones por COVID-19, comparando las cifras antes y después de la implementación del modelo. Una disminución en esta tasa indicaría que el modelo está ayudando a identificar y tratar adecuadamente a los pacientes en mayor riesgo.

Otro aspecto importante es la eficiencia en la utilización de recursos. La reducción en la saturación de hospitales, unidades de cuidados intensivos y el uso de ventiladores sería un claro indicativo de una mejor asignación de recursos gracias al modelo predictivo. Asimismo, el tiempo de respuesta en la atención de pacientes críticos podría ser evaluado para determinar si la solución permite una intervención más rápida y efectiva.

La calidad de la atención médica también puede ser medida a través de la tasa de recuperación de pacientes, esperando un aumento en esta tasa debido a un tratamiento más adecuado y temprano para aquellos identificados como de alto riesgo. La satisfacción de los pacientes y sus familias con la atención recibida es otro aspecto fundamental, especialmente en términos de confianza y percepción de la efectividad del tratamiento.

Por último, la implementación y adopción del modelo en el sistema de salud se pueden evaluar mediante el porcentaje de instituciones que han adoptado el modelo y lo utilizan en su práctica diaria, así como la capacitación del personal médico en el uso del modelo y su integración en los procesos de toma de decisiones clínicas. Estas métricas, en conjunto, permiten evaluar el impacto práctico y beneficioso de la solución en el sistema de salud, contribuyendo a una mejor atención de los pacientes y optimización de los recursos disponibles.

## ¿Que problema de aprendizaje implica resolver?

El problema que se busca resolver es un problema de **clasificación binaria**. En términos de aprendizaje automático, esto significa que el objetivo es asignar a cada paciente uno de dos posibles resultados:

**Clase 1:** El paciente falleció.

**Clase 2:** El paciente no falleció.

El modelo debe aprender a partir de los datos históricos de pacientes con COVID-19 para predecir, basándose en las características médicas y demográficas disponibles, a cuál de estas dos clases pertenece un nuevo paciente.

## ¿Qué metricas permiten medir la calidad del modelo de aprendizaje? ¿Cuales son sus valores deseables?

Dado que nuestros datos están altamente desbalanceados, con un 99% de pacientes no fallecidos y solo un 1% de fallecidos, es crucial elegir métricas que reflejen adecuadamente el rendimiento del modelo en ambos grupos. Las métricas tradicionales como el *Accuracy* (Exactitud) no son adecuadas en este contexto, ya que un modelo que prediga siempre "no falleció", dado el predominio de esta clase, tendría un alto *Accuracy* pero no sería útil. En su lugar, seleccionamos métricas que nos permiten evaluar la capacidad del modelo para identificar correctamente a los pacientes fallecidos sin perder de vista el contexto de clases desbalanceadas. A continuación se detallan las métricas clave y sus valores deseables:

**Precision (Precisión):** es el número de verdaderos positivos dividido por el número total de predicciones positivas. En otras palabras, es una medida de cuántas de las predicciones positivas del modelo fueron correctas. Un valor de precision alto es deseable para minimizar los falsos positivos. En este caso, tal como en muchos otros contextos, consideraremos como buenos valores superiores a 0.75.

**Recall (Sensibilidad o Tasa de Verdaderos Positivos):** es el número de verdaderos positivos dividido por el número total de positivos reales. Mide la capacidad del modelo para identificar correctamente los casos positivos. Un Recall alto es crucial para este problema, ya que es importante identificar la mayor cantidad posible de casos de fallecimiento. Consideraremos haber logrado un buen Recall si obtenemos valores por encima de 0.6. 

**F1-Score:** es la media armónica de la Precision y el Recall, y es particularmente útil cuando hay un desbalance de clases, como en este caso donde los fallecimientos son una minoría. Un valor cercano a 1 indica un buen equilibrio entre precisión y recall. Consideraremos que valores mayores a 0.75 denotarán un buen F1-score. 

**ROC-AUC (Área Bajo la Curva de la Característica Operativa del Receptor):** la curva ROC muestra la tasa de verdaderos positivos frente a la tasa de falsos positivos a diferentes umbrales. El AUC mide el área bajo esta curva. Mientras que un AUC cercano a 1 indica un excelente rendimiento del modelo, en nuestro presente problema de clasificación consideraremos buenos valores superiores a 0.85.

**AUC-PR (Área Bajo la Curva de Precisión-Recall):** similar al ROC-AUC, pero más informativo en el contexto de clases desbalanceadas. Aquí también un valor cercano a 1 es ideal, pero nosotros consideraremos valores superiores a 0.75 como buenos.

**Matriz de Confusión:** muestra los verdaderos positivos, verdaderos negativos, falsos positivos y falsos negativos. Aunque no fijamos proporciones específicas para cada una de estas categorías, esperamos que la matriz muestre un alto número de verdaderos positivos y verdaderos negativos, y un bajo número de falsos positivos y falsos negativos.

## ¿Como están alineadas las métricas de la calidad del modelo con las métricas de impacto de la solución?

Un valor de *Precision* alto significa que la mayoría de las predicciones positivas son correctas. Esto reduce los falsos positivos, evitando que recursos limitados se asignen a pacientes que no los necesitan. Mejorar la *Precision* podría resultar en una disminución significativa en la saturación de hospitales, por ejemplo, reduciendo la ocupación innecesaria de camas y ventiladores.

Un valor alto de *Recall* asegura que la mayoría de los casos positivos sean identificados, minimizando los falsos negativos. Esto es crucial para garantizar que los pacientes en riesgo reciban la atención necesaria. Un incremento del *Recall* podría correlacionarse con una mejora en la tasa de recuperación de pacientes, debido a la detección temprana y tratamiento de casos críticos.

El resto de las métricas de calidad del modelo (F1-Score, ROC-AUC, AUC-PR) están alineadas con las métricas de impacto de la solución a nivel nacional, ya que todas contribuyen a mejorar el rendimiento del modelo, lo que se traduce en un mejor funcionamiento del sistema de salud. Sin embargo, cada métrica también tiene un aporte específico. Un alto *F1-Score* indica un buen equilibrio entre precisión y recall, mejorando la confianza en las decisiones clínicas y asegurando que los recursos se dirijan efectivamente a los pacientes en mayor riesgo sin sobrecargar el sistema de salud con falsos positivos. El *ROC-AUC* demuestra la capacidad del modelo para distinguir entre pacientes fallecidos y no fallecidos en un rango amplio de umbrales, facilitando la flexibilidad en la toma de decisiones clínicas y permitiendo ajustar umbrales según la disponibilidad de recursos y la situación epidemiológica. Un alto *AUC-PR* es especialmente importante en contextos de desbalance de clases, asegurando que el modelo sea robusto en detectar los casos críticos, lo cual es vital para priorizar la atención y recursos a los pacientes más vulnerables.

## Repositorios
- [Github](https://github.com/VesnaPivac/ML_COVID19-Mexico)
- [Dagshub](https://dagshub.com/VesnaPivac/ML_COVID19-Mexico)

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
