# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Sun'iy Intellekt"
copyright = '2023, Musulmon Lolaev'
author = 'Musulmon Lolaev'
release = '1-tahrir'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'uz_latin'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.

extensions = [
    "nbsphinx",
    'sphinx.ext.mathjax'
]

exclude_patterns = ['_build', '**.ipynb_checkpoints']

numfig = True
math_numfig = True
numfig_secnum_depth = 2
math_eqref_format = "Eq.{number}"