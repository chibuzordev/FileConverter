from setuptools import setup, find_packages

setup(
    name="data-converter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "openpyxl",
        "xlsxwriter"
    ],
    entry_points={
        "console_scripts": [
            "dataconvert=cli:main"
        ]
    },
    author="Your Name",
    description="A file conversion framework for CSV/Excel/JSON data transformation.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/chibuzordev/FileConverter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
