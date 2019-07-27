import os
from setuptools import setup

from artisanlib import __version__

setup(
    name                = "artisan",
    version             = __version__,
    description         = "Visual scope for coffee roasters",
    license             = "GPLv3",
    url                 = "https://github.com/artisan-roaster-scope/artisan",
    packages            = ["artisanlib", "artisanlib.const", "artisanlib.plus"],
#    package_dir         = {"": "src"},
    scripts             = ["artisan.py"],
)
