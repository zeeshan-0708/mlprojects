from setuptools import find_packages, setup
from typing import List
import os

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements from the given file,
    excluding any local paths or invalid entries.
    '''
    requirements = []
    if os.path.exists(file_path):
        with open(file_path, encoding="utf-8") as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements if req.strip() and req.strip() != HYPHEN_E_DOT]
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Zeeshan",
    author_email="Zeeshank9371@gmail.com",
    description="A machine learning project template",
    license="MIT",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
