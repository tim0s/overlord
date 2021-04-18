import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="overlord", 
    version="0.0.1",
    author="Timo Schneider",
    author_email="timos@inf.ethz.ch",
    description="Automatically upload files to overleaf.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tim0s/overlord",
    project_urls={
        "Bug Tracker": "https://github.com/tim0s/overlord/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

