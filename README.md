# Extra packages for DASF

[![Continuous Test](https://github.com/discovery-unicamp/dasf-core-extras/actions/workflows/ci.yaml/badge.svg)](https://github.com/discovery-unicamp/dasf-core-extras/actions/workflows/ci.yaml)
[![Commit Check Policy](https://github.com/discovery-unicamp/dasf-core-extras/actions/workflows/commit-check.yaml/badge.svg)](https://github.com/discovery-unicamp/dasf-core-extras/actions/workflows/commit-check.yaml)
![Interrogate](https://raw.githubusercontent.com/discovery-unicamp/dasf-core-extras/badges/badges/interrogate_badge.svg)

This repository contains extra packages that can be integrated into DASF.
Most of the code here contains code or libraries that cannot be integrated
into DASF for any purpose or that are still in development.

## Installation

To install, you can use `pip` as default.

```bash
pip3 install .
```

This library will automatically install DASF core package if it is not
installed, but we strongly recommend to use it in a system or container that
already has DASF installed.

### Testing

If you have a working environment with DASF installed, you can execute all
the test sets. Make sure you have all development packages installed such as
**pytest**, **parameterized** and **mock**. To run, you need to execute
`pytest` from the `tests/` directory.

```bash
pytest tests/
```

### Machine Learning Algorithms

The table below is a list of supported machine learning algorithms by DASF framework.

|     **ML Algorithm**     | **CPU** | **GPU** | **Multi-CPU** | **Multi-GPU** |        **Path**        |
|--------------------------|:-------:|:-------:|:-------------:|:-------------:|:----------------------:|
| SOM                      |    X    |    X    |       X       |       X       | dasf_extras.ml.cluster |

### Cite

If you are using this project in your research, please cite our first paper where DASF was proposed.

```bibtex
@inproceedings{dasf,
  title        = {DASF: a high-performance and scalable framework for large seismic datasets},
  author       = {Julio C. Faracco and Otávio O. Napoli and João Seródio and Carlos A. Astudillo and Leandro Villas and Edson Borin and Alan A. Souza and Daniel C. Miranda and João Paulo Navarro},
  year         = {2024},
  month        = {August},
  booktitle    = {Proceedings of the International Meeting for Applied Geoscience and Energy},
  address      = {Houston, TX},
  organization = {AAPG/SEG}
}
```

### Authors

For further reference, below the authors list:

* Julio Faracco
* Edson Borin
