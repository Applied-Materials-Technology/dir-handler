# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

# Point to the directory containing your package 
# (e.g., project root or 'src/' depending on your layout)
sys.path.insert(0, os.path.abspath('../../src'))  # or os.path.abspath('../..')

project = 'dir-handler'
copyright = '2026, meganasampson'
author = 'meganasampson'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = 'furo'
html_static_path = ['_static']


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',    # Enables support for Google/NumPy style docstrings
    'sphinx.ext.viewcode',    # Adds links to the highlighted source code
    'sphinx.ext.githubpages',
    'sphinx_design',
]

# Autodoc settings (optional tuning)
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}