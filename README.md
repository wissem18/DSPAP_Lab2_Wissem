# DSPAP Lab 2 — Best Practices for Programming Projects in AI

This project is a structured and reproducible data science workflow built around the Open Food Facts nutrition dataset. The purpose is to transform a working analysis into a cleaner, more maintainable project that follows standard practices in Python development, project organization, reproducible environments, and collaborative Git-based work.

The analysis focuses on a set of key nutritional variables, including sugars, fat, salt, proteins, fiber, and energy content. It uses principal component analysis (PCA) to reduce the dimensionality of the data and identify structure in the feature space, while also computing descriptive statistics to summarize the nutritional profile of the dataset.

## Project objective

The main goals of this project are to:

- organize the project into a clear and readable structure;
- improve code quality through modular functions and clear naming;
- store configuration values separately from notebook logic;
- handle missing data and missing-file errors more robustly;
- document the project clearly for reuse and collaboration;
- make it easy to share and extend with Git and GitHub.

## Project structure

- `data/` — cleaned input datasets used by the analysis
- `config/` — project configuration files, including the YAML configuration for PCA and dataset paths
- `notebooks/` — Jupyter notebooks used for exploratory and instructional work
- `src/` — reusable Python modules containing the project logic
- `requirements.txt` — project dependencies required to reproduce the environment
- `README.md` — overview of the project and setup instructions

## Environment setup

To reproduce the environment, create a virtual environment in the project root and install the listed dependencies.

### macOS / Linux

```bash
python3 -m venv Lab2venv
source Lab2venv/bin/activate
python -m pip install -r requirements.txt
```

### Windows

```bash
python -m venv Lab2venv
Lab2venv\Scripts\activate
python -m pip install -r requirements.txt
```

It is important that the virtual environment remains local to the machine and is not committed to Git. The repository includes a `.gitignore` entry to exclude the environment folder from version control.

## Running the analysis

1. Activate the project environment.
2. Select the `Lab2venv` interpreter in VS Code.
3. Open the notebook in `notebooks/`.
4. Run the notebook cells in order.


## Contributors

- Wissem Yousfi
