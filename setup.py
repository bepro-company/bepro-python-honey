import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bepro-python-honey",
    version="0.0.1.8",
    author="Bepro Company",
    author_email="dev@bepro11.com",
    description="A utility package for Bepro Company",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bepro-company/bepro-python-honey",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
