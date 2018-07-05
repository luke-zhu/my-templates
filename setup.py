from setuptools import setup, find_packages

# TODO: Figure out a better way to keep reqs in-sync with the requirements
util = [
    'arrow',
    'fire',
    'sh',
]
webservice = open('webservice/requirements.txt').read().split('\n')
dashboard = []
etl = []
ml = [
    # Data Science
    'jupyter',
    'notebook',
    'numpy',
    'scipy',
    'pandas',
    'scikit-learn',
    # Deep Learning
    'torch',
    'torchvision',
    'tensorflow',
    'keras',
]

install_reqs = webservice

setup(
    name='my-templates',
    version='0.1.0',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=webservice,
    extras_require={
        'test': [
            'pytest',
            'pytest-cov',
            'codecov',
        ]
    }
)
