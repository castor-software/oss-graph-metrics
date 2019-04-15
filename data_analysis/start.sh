docker run --rm \
    -p 10000:8888 \
    -e JUPYTER_ENABLE_LAB=yes \
    -v "$PWD/notebook":/home/jovyan/work \
    -v "$PWD/data":/home/jovyan/work/data \
    jupyter/datascience-notebook:9b06df75e445
