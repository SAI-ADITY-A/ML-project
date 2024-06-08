from setuptools import find_packages, setup

from typing import List
HYPHEN = '-e .'
def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

    if HYPHEN in requirements:
        requirements.remove(HYPHEN)

    return requirements

setup(
    name = 'Student_performance',
    author= 'Aditya',
    author_email= '21mm01022@iitbbs.ac.in',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)