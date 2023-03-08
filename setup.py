# Copyright Contributors to the Pyro project.
# SPDX-License-Identifier: Apache-2.0

from __future__ import absolute_import, division, print_function

import os
import sys

MAJOR_PY_VERSION, MINOR_PY_VERSION = sys.version_info[0], sys.version_info[1]

from setuptools import find_packages, setup

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
_jax_version_constraints = ">=0.4"
_jaxlib_version_constraints = ">=0.4"

# Find version
for line in open(os.path.join(PROJECT_PATH, "numpyro", "version.py")):
    if line.startswith("__version__ = "):
        version = line.strip().split()[2][1:-1]

# READ README.md for long description on PyPi.
try:
    long_description = open("README.md", encoding="utf-8").read()
except Exception as e:
    sys.stderr.write("Failed to read README.md:\n  {}\n".format(e))
    sys.stderr.flush()
    long_description = ""

dev_reqs = [
            "dm-haiku",
            "flax",
            "funsor>=0.4.1",
            "graphviz",
            "optax>=0.0.6",
            "pyyaml",  # flax dependency
            "tensorflow_probability>=0.17.0",
        ]

if MAJOR_PY_VERSION == 3 and MINOR_PY_VERSION >= 9:
    # TODO(Du Phan): Consider bumping python req to 3.9+
    dev_reqs.append("jaxns>=2.0.0") # JAXNS req, but requires python >= 3.9 for modern PEP changes to annotations
else:
    sys.stderr.write("Unable to meet `jaxns` requirement, as it requires python>=3.9\n")



setup(
    name="numpyro",
    version=version,
    description="Pyro PPL on NumPy",
    packages=find_packages(include=["numpyro", "numpyro.*"]),
    url="https://github.com/pyro-ppl/numpyro",
    author="Uber AI Labs",
    install_requires=[
        f"jax{_jax_version_constraints}",
        f"jaxlib{_jaxlib_version_constraints}",
        "multipledispatch",
        "numpy",
        "tqdm",
    ],
    extras_require={
        "doc": [
            "ipython",  # sphinx needs this to render codes
            "nbsphinx>=0.8.5",
            "readthedocs-sphinx-search==0.1.0",
            "sphinx",
            "sphinx_rtd_theme",
            "sphinx-gallery",
        ],
        "test": [
            "importlib-metadata<5.0",
            "black[jupyter]>=21.8b0",
            "flake8",
            "importlib-metadata<5.0",
            "isort>=5.0",
            "pytest>=4.1",
            "pyro-api>=0.1.1",
            "scipy>=1.6,<1.7",
        ],
        "dev": dev_reqs,
        "examples": [
            "arviz",
            "jupyter",
            "matplotlib",
            "pandas",
            "seaborn",
            "scikit-learn",
            "wordcloud",
        ],
        "cpu": f"jax[cpu]{_jax_version_constraints}",
        # TPU and CUDA installations, currently require to add package repository URL, i.e.,
        # pip install numpyro[cuda] -f https://storage.googleapis.com/jax-releases/jax_releases.html
        "tpu": f"jax[tpu]{_jax_version_constraints}",
        "cuda": f"jax[cuda]{_jax_version_constraints}",
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="probabilistic machine learning bayesian statistics",
    license="Apache License 2.0",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
