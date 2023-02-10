from setuptools import setup, find_packages
from typing import List


def filter_requirements(requirements: List[str]):
    return list(
        filter(
            lambda line: not line.startswith("certifi")
            and line not in requirements_dev
            and not line.startswith("-e"),
            requirements,
        )
    )


with open("README.md", "r") as readme_file, open(
    "requirements.txt", "r"
) as requirements_file, open("requirements_dev.txt", "r") as requirements_dev_file:
    long_description = readme_file.read()
    requirements_dev = [line.replace("\n", "") for line in requirements_dev_file.readlines()]
    # filter the odd line containing the ceritifi dependency, and the development dependencies
    requirements = filter_requirements(
        [line.replace("\n", "") for line in requirements_file.readlines()]
    )
    print(requirements)


if __name__ == "__main__":
    setup(
        name="python_template",
        version="0.1.0",
        description="A template for making python packages",
        long_description_content_type="text/markdown",
        long_description=long_description,
        package_dir={"": "src"},
        author="Kesler Isoko",
        author_email="uchekesla@gmail.com",
        packages=find_packages(where="src", exclude=("tests*", "jaguar_backend*")),
        install_requires=requirements,
        classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ],
        extras_require={
            "dev": requirements_dev,
        },
    )
