from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.misc import Raw

def setup(app):
    app.add_directive("raw", Raw)


project = "decoupler-py"
extensions = []
master_doc = "index"

