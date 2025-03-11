# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'wish-list'
copyright = '2025, Ayaz Salikhov'
author = 'Ayaz Salikhov'

version = 'latest'
release = 'latest'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# The file above was generated using sphinx 8.2.3 with this command:
# sphinx-quickstart --project "wish-list" --author "Ayaz Salikhov" -v "latest" -r "latest" -l en --no-sep --no-makefile --no-batchfile
# These are custom options for this project

html_theme = "nature"

extensions = ["myst_parser"]

# MyST configuration reference: https://myst-parser.readthedocs.io/en/latest/configuration.html
myst_heading_anchors = 3
