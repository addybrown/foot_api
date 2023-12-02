from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="foot_api_parser",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    author="Adam Sequeira",
    author_email="adamsequeira@outlook.com",
    description="Parses soccer data from foot_api",
    long_description="This function parses football data",
    long_description_content_type="text/markdown",
    url="https://github.com/addybrown/foot_api",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
