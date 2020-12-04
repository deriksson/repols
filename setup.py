"""Allow easy installation of this package.

"""

# Third-party imports
from setuptools import find_packages, setup

setup(
    name="repols",
    version="0.0.1",
    author="Daniel Eriksson",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Click >= 7.0", "PyGithub"],
    setup_requires=["flake8"],
    entry_points={"console_scripts": ["repols=repols.cli:cli"]},
)
