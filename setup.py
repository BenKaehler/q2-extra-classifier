from setuptools import setup, find_packages

setup(
    name="q2-extra-classifier",
    version='2017.5.0.dev',
    packages=find_packages(),
    install_requires=['q2-feature-classifier', 'q2cli'],
    author="Ben Kaehler",
    author_email="kaehler@gmail.com",
    description="Functionality for taxonomic classification",
    license='BSD-3-Clause',
    url="https://qiime2.org",
    entry_points={
        'qiime2.plugins':
        ['q2-extra-classifier=q2_extra_classifier.plugin_setup:plugin'],
        'console_scripts': 
        ['qiime_kludge=q2_extra_classifier._cli:qiime_kludge']
    }
)
