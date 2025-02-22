# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Sun'iy Intellekt"
copyright = '2025, Musulmon Lolaev'
author = 'Musulmon Lolaev'
release = '1.1-tahrir'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_css_files = ['custom.css']

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "collapse_navigation" : False
}

locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.

extensions = [
    "nbsphinx",
    'sphinx.ext.mathjax',
    'sphinx_rtd_theme',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig'
]

exclude_patterns = ['_build', '**.ipynb_checkpoints']

numfig = True
math_numfig = True
numfig_secnum_depth = 2
math_eqref_format = "Eq.{number}"

mathjax_path = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"

mathjax_config = {
    'TeX': {'equationNumbers': {'autoNumber': 'AMS', 'useLabelIds': True}},
}

suppress_warnings = ['autosectionlabel.*']