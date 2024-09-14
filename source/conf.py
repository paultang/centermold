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

templates_path = ['_templates']

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
html_title = "Centermold, a Professtional Mold Maker and a Plastic Injection Molding Factory"
html_context = {
    'ga_tracking_id': 'G-LJ9L3WNCW5',  # Replace with your tracking ID
}
html_favicon = '_static/favicon.ico'  # 修改成你的图标文件路径

html_css_files = [
    'custom.css',
]

# conf.py 文件

rst_epilog = """
.. raw:: html

    <hr>
    <div style="text-align:center; margin-top:20px;">
    <p>Contact us: <a href="mailto:inquiry@centermold.com">inquiry@centermold.com</a></p>
    <p>a free quotation for you</p>
"""
