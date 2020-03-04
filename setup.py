from setuptools import setup, find_packages
setup(
    name = "XFLexer",
    version = "0.1",
    packages = find_packages(),
    install_requires = [ 'pygments' ],
    entry_points = { 'pygments.lexers': 'xflexer = xflexer:XFLexer' }
)

