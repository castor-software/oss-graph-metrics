docker run --rm \
    -e JUPYTER_ENABLE_LAB=yes \
    -e REPORT_PROJECT=neo4j \
    -v "$PWD/notebook":/home/jovyan/work \
    -v "$PWD/data":/home/jovyan/work/data \
    -v "$PWD/figures":/home/jovyan/work/figures \
    -v "$PWD/reports":/home/jovyan/work/output \
    jupyter/datascience-notebook:9b06df75e445 \
    jupyter nbconvert --to notebook --execute work/report.ipynb --output output/neo4j
