import os
import re
import setuptools

NAME             = "spa2num"
AUTHOR           = "Christophe VG"
AUTHOR_EMAIL     = "cartovarc@gmail.com"
DESCRIPTION      = "Spanish word converter to numerical digits"
LICENSE          = "MIT"
KEYWORDS         = "spanish, words, converter, numeric, digits"
URL              = "https://github.com/cartovarc/" + NAME
README           = ".github/README.md"
CLASSIFIERS      = [
  "Environment :: Console",
  "Development Status :: 1 - Planning",
  "Intended Audience :: Developers",
  "Topic :: Text Processing :: Linguistic",
  "Topic :: Software Development :: Libraries :: Python Modules",
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
  
]
INSTALL_REQUIRES = [
  "num2words",
  
]
ENTRY_POINTS = {
  
}
SCRIPTS = [
  
]

HERE = os.path.dirname(__file__)

def read(file):
  with open(os.path.join(HERE, file), "r") as fh:
    return fh.read()

VERSION = re.search(
  r'__version__ = [\'"]([^\'"]*)[\'"]',
  read(NAME.replace("-", "_") + "/__init__.py")
).group(1)

LONG_DESCRIPTION = read(README)

if __name__ == "__main__":
  setuptools.setup(
    name=NAME,
    version=VERSION,
    packages=setuptools.find_packages(),
    author=AUTHOR,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license=LICENSE,
    keywords=KEYWORDS,
    url=URL,
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
    entry_points=ENTRY_POINTS,
    scripts=SCRIPTS,
    include_package_data=True    
  )
