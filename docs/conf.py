# -*- coding: utf-8 -*-
import sphinx_book_theme

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]
source_suffix = '.rst'
master_doc = 'index'
project = 'examGenerator'
year = '2023'
author = 'Hamid Vakilzadeh'
copyright = '{0}, {1}'.format(year, author)
version = release = '0.0.0'

pygments_style = 'trac'
templates_path = ['.']
extlinks = {
    'issue': ('https://github.com/hamid-vakilzadeh/examGenerator/issues/%s', '#'),
    'pr': ('https://github.com/hamid-vakilzadeh/examGenerator/pull/%s', 'PR #'),
}
html_theme = 'sphinx_book_theme'
html_theme_path = [sphinx_book_theme.get_html_theme_path()]
html_theme_options = {
    'githuburl': 'https://github.com/hamid-vakilzadeh/examGenerator/',
}

html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = False
html_sidebars = {
    '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = '%s-%s' % (project, version)

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
