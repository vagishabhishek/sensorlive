from setuptools import setup, find_packages
from typing import List


def get_requirements() -> List[str]:
    requirements_list :List[str] = []
    return requirements_list


setup(
    name="sensor",
    version="0.0.1",
    author="vagish abhishek",
    author_emil="vagish.abhishek@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
