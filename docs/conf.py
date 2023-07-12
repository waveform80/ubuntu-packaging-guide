# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys
import datetime

# -- Project information -----------------------------------------------------

project = 'Ubuntu Packaging Guide'
author = 'Canonical Group Ltd.'
version = '2.0'
copyright = f'{author}, {datetime.date.today().year}'

# -- General configuration ---------------------------------------------------

needs_sphinx = '4.3.2'
extensions = [
    'sphinx_copybutton',
    'sphinx_design',
]
root_doc = 'index'
exclude_patterns = ['.sphinx/venv/*']

# Sphinx-copybutton config options:
# 1) prompt to be stripped from copied code.
# 2) Set to copy all lines (not just prompt lines) to ensure multiline snippets
# can be copied even if they don't contain an EOF line.
copybutton_prompt_text = '$ '
copybutton_only_copy_prompt_lines = False

# -- Localization configuration ----------------------------------------------

# Generate UUIDs and use a single domain for all translations (required for
# certain translation systems, including Launchpad)
gettext_uuid = True
gettext_compact = 'ubuntu-packaging-guide'
locale_dirs = ['../locales']

# -- Options for HTML output -------------------------------------------------

html_theme = 'furo'
html_logo = '_static/ubuntu_logo.png'
html_title = 'Ubuntu Packaging Guide'
html_theme_options = {
    'light_css_variables': {
        'color-sidebar-background-border': 'none',
        'font-stack': 'Ubuntu, -apple-system, Segoe UI, Roboto, Oxygen, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif',
        'font-stack--monospace': 'Ubuntu Mono variable, Ubuntu Mono, Consolas, Monaco, Courier, monospace',
        'color-foreground-primary': '#111',
        'color-foreground-secondary': 'var(--color-foreground-primary)',
        'color-foreground-muted': '#333',
        'color-background-secondary': '#FFF',
        'color-background-hover': '#f2f2f2',
        'color-brand-primary': '#111',
        'color-brand-content': '#06C',
        'color-inline-code-background': 'rgba(0,0,0,.03)',
        'color-sidebar-link-text': '#111',
        'color-sidebar-item-background--current': '#ebebeb',
        'color-sidebar-item-background--hover': '#f2f2f2',
        'sidebar-item-line-height': '1.3rem',
        'color-link-underline': 'var(--color-background-primary)',
        'color-link-underline--hover': 'var(--color-background-primary)',
    },
    'dark_css_variables': {
        'color-foreground-secondary': 'var(--color-foreground-primary)',
        'color-foreground-muted': '#CDCDCD',
        'color-background-secondary': 'var(--color-background-primary)',
        'color-background-hover': '#666',
        'color-brand-primary': '#fff',
        'color-brand-content': '#06C',
        'color-sidebar-link-text': '#f7f7f7',
        'color-sidebar-item-background--current': '#666',
        'color-sidebar-item-background--hover': '#333',
    },
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ['_static']

html_css_files = [
    'css/logo.css',
    'css/github_issue_links.css',
    'css/custom.css',
]
html_js_files = [
    'js/github_issue_links.js',
]

# -- Options for EPUB output -------------------------------------------------

epub_basename = 'ubuntu-packaging-guide'
epub_show_urls = 'no'

# -- Options for PDF output --------------------------------------------------

latex_engine = 'xelatex'
latex_show_pagerefs = True
latex_show_urls = 'footnote'
latex_elements = {
    'papersize': 'a4paper',
}
latex_documents = [
    (
        root_doc,
        'ubuntu-packaging-guide.tex',
        html_title,
        author,
        'manual',
        True,
    ),
]
