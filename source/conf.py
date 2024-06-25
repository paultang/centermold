# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CenterMold'
copyright = '2024, bill'
author = 'bill'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_sitemap',

]

html_baseurl = 'https://www.centermold.com//en/latest/'  # Replace with your Read the Docs URL

sitemap_url_scheme = "{link}"

# templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# 在文档中添加自定义JavaScript文件
def setup(app):
    app.add_js_file('seo.js')



# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_title = "CenterMold, a professtional Mold Tooling and Plastic Injection Molding Company"

html_context = {
    'ga_tracking_id': 'G-LJ9L3WNCW5',  # Replace with your tracking ID
}


"""
{% extends "!layout.html" %}

{% block extrahead %}
  {{ super() }}
  <!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-LJ9L3WNCW5"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-LJ9L3WNCW5');
</script>
{% endblock %}
"""