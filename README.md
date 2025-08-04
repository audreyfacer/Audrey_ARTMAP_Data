# Audrey_ARTMAP_Data

This repository is Audrey's final summer internship project with the Applied Computational Intelligence Laboratory at Missouri S&T.

> [!note] To Audrey
> Audrey, feel free to write, rewrite, and overwrite as much as you'd like in this readme!

> [!note] Another Note to Audrey
> Look at the [File Structure](#file-structure) section to get an understanding of all the files/folders I added here.

## Table of Contents

- [Audrey\_ARTMAP\_Data](#audrey_artmap_data)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
  - [File Structure](#file-structure)

## Usage

This is a Python project, so a working Python environment is required.
A virtual environment manager is recommended, such as [`mamba`](https://mamba.readthedocs.io/en/latest/index.html).
For example, download the [miniforge distribution](https://github.com/conda-forge/miniforge) for your OS.

Next, create a virtual environment like so:

```shell
mamba create -n audrey python=3.12
```

Activate that environment with

```shell
mamba activate audrey
```

and install the python dependencies once you're inside that environment with

```shell
pip install -r requirements.txt
```

## File Structure

This section outlines the location and meaning of the files in this repo:

- [`cluster/](cluster): scripts for running this project's experiments  on high-performance clusters.
- [`data/`](data): the location of downloaded, generated, and/or preprocessed data.
- [`notebooks/`](notebooks): IPython notebooks for experiment development, scratch spaces, etc.
- [`scripts/](scripts): experiment driver scripts.
- [`.flake8`](.flake8): some custom Python [Flake8](https://flake8.pycqa.org/en/latest/) linting preferences, such as the config to make `flake8` stop yelling if lines are longer than a meager 80 characters.
- [`.gitignore`](.gitignore): a file with patterns that are ignored by git tracking.
- [`README.md`](README.md): this file.
- [`requirements.txt`](requirements.txt): the pip requirements file containing all of the Python dependencies for the project.
