#!/usr/bin/env python
# -*- coding: utf-8 -*-


import setuptools

{% if cookiecutter.with_pbr == "yes" %}
try:
    import multiprocessing
    assert multiprocessing
except ImportError:
    pass


setuptools.setup(
    setup_requires=["pbr>=1.8"],
    pbr=True)
{% else %}
def get_description():
    with open("README.rst", "r") as description_fp:
        return description_fp.read().strip()


def get_install_requires():
    import pip

    try:
        requirements = list(pip.req.parse_requirements("requirements.txt"))
    except Exception:
        import pip.download

        requirements = list(pip.req.parse_requirements(
            "requirements.txt", session=pip.download.PipSession()))

    reqs, links = [], []
    for item in requirements:
        if getattr(item, "url", None):
            links.append(str(item.url))
        if getattr(item, "link", None):
            links.append(str(item.link))
        if item.req:
            reqs.append(str(item.req))

    return reqs, links


requires, links = get_install_requires()
setuptools.setup(
    name="{{ cookiecutter.package }}",
    version="{{ cookiecutter.version }}",
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    maintainer="{{ cookiecutter.full_name }}",
    maintainer_email="{{ cookiecutter.email }}",
    license="{{ cookiecutter.license }}",
    description="{{ cookiecutter.summary }}",
    long_description=get_description(),
    packages=[
        "{{ cookiecutter.package }}"
    ],
    install_requires=requires,
    dependency_links=links)
{% endif -%}
