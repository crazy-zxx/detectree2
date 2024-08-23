from setuptools import find_packages, setup

setup(
    name="detectree2",
    version="1.0.8",
    author="James G. C. Ball",
    author_email="ball.jgc@gmail.com",
    description="Detectree packaging",
    url="https://github.com/PatBall1/detectree2",
    # package_dir={"": "detectree2"},
    packages=find_packages(),
    test_suite="detectree2.tests.test_all.suite",
    install_requires=[
        "pyyaml>=5.1",
        "numpy",
        "rtree",
        "proj",
        "geos",
        "pypng",
        "geopandas",
        "rasterio==1.3a3",
        "fiona",
        "pycrs",
        "descartes",
        "detectron2@git+https://github.com/facebookresearch/detectron2.git",
    ],
)
