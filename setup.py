import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="IFcoltransG",
    version="0.0.1",
    author="IFcoltransG",
    license="unlicense",
    author_email="IFcoltransG+PyPI@protonmail.ch",
    description="A hashable immutable dictionary",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IFcoltransG/HashableDict",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    python_requires='>=3.7',
)
