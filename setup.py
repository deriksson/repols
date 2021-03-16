"""Allow easy installation of this package."""

from setuptools import find_packages, setup


def long_description():
    with open("README.md", "r", encoding="utf-8") as readme_file:
        return readme_file.read()


setup(
    name="repols",
    version="1.1.0",
    author="Daniel Eriksson",
    author_email="gustaf.daniel.eriksson@gmail.com",
    description="List GitHub repositories filtered by team",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/deriksson/repols",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Click >= 7.0", "PyGithub"],
    setup_requires=["flake8"],
    entry_points={"console_scripts": ["repols=repols.cli:cli"]},
)
