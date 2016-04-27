#!/usr/bin/env python
# -*- coding: utf-8 -*-


import setuptools

from setuptools.command.test import test as TestCommand  # NOQA
import sys


class Tox(TestCommand):

    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import shlex
        import tox

        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)

{% if cookiecutter.with_pbr == "yes" %}
try:
    import multiprocessing
    assert multiprocessing
except ImportError:
    pass


setuptools.setup(
    setup_requires=["pbr>=1.8"],
    tests_require=["tox"],
    cmdclass={'test': Tox},
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
    dependency_links=links,
    tests_require=["tox"],
    cmdclass={'test': Tox})
{% endif -%}
