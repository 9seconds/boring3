#!/usr/bin/env python
# -*- coding: utf-8 -*-


import setuptools


# please check following link to understand how everything works:
# https://setuptools.readthedocs.io/en/latest/setuptools.html#configuring-setup-using-setup-cfg-files
{%- if cookiecutter.setuptools_scm == "no" %}
setuptools.setup()
{%- else %}
setuptools.setup(use_scm_version=True)
{%- endif %}
