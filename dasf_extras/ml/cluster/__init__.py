#!/usr/bin/env python3

""" Init module for Clustering ML algorithms (extras). """

from dasf_extras.ml.cluster.som import SOM  # noqa

cluster_methods = [
    "SOM",
]

__all__ = cluster_methods
