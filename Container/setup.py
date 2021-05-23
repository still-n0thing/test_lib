import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "testlib",
    version = "0.0.1",
    author = "whymihere",
    author_email = "himanshu12361@gmail.com",
    description = "A small example package",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/still-n0thing/test_lib",
    project_urls={
        "Bug Tracker": "https://github.com/still-n0thing/test_lib/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)