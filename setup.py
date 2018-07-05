from setuptools import setup, find_packages

# TODO: Figure out a better way to keep this in-sync with the requirements
microservice_reqs = open('webservice/requirements.txt').read().split('\n')
dashboard_reqs = []
etl_reqs = []

setup(
    name='my-templates',
    version='0.1.0',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        # Utility
        'arrow',
        'fire',
        'sh',
        # Web
        'Flask',
        'Flask-GraphQL',
        'Flask-SQLAlchemy',
        'gunicorn',
        'graphene',
        'graphene_sqlalchemy',
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
    ],
    extras_require={
        'test': [
            'pytest',
            'codecov',
        ]
    }
)
