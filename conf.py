project = "GATE DA Notes"
author = "Amby"

extensions = ["myst_parser", "sphinx_design", "sphinx_copybutton"]
myst_enable_extensions = ["amsmath", "dollarmath", "colon_fence"]

root_doc = "index"
exclude_patterns = [
    "_build", ".venv", ".venv-sphinx", "README.md", "Thumbs.db", ".DS_Store",
]

html_theme = "pydata_sphinx_theme"
html_title = "GATE DA Notes"
html_theme_options = {
    "header_links_before_dropdown": 7,
    "show_toc_level": 2,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/sbmldev/gate-da",
            "icon": "fa-brands fa-github",
        }
    ],
}