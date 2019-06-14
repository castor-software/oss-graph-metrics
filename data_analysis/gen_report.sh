docker run --rm \
    -e JUPYTER_ENABLE_LAB=yes \
    -e REPORT_PROJECT=$1 \
    -v "$PWD/notebook":/home/jovyan \
    -v "$PWD/data":/home/jovyan/data \
    -v "$PWD/figures":/home/jovyan/figures \
    -v "$PWD/reports":/home/jovyan/output \
    jupyter/datascience-notebook:9b06df75e445 \
    jupyter nbconvert --to pdf --execute ./report.ipynb --template hidecode --output ./output/$1
