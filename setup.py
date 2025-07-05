from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='grafico-andre',
    version='0.0.1',
    author='Andre',
    author_email='andrepraz@gmail.com',
    description='gerar gráfico de linha quando passar um dicionário de dados',
    long_description=page_description,
    long_description_content_type='text/markdown',
    url='https://github.com/andrepraz/simple-package-andre',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)