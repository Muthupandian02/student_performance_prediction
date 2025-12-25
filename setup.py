from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)-> List[str]:
    with open('requirements.txt', 'r') as file:
        requirement=file.readlines()
    requirement=[req.strip() for req in requirement if req.strip()!= '-e .']
    return requirement

setup(
    name='MLOPS',
    version='0.0.1',
    author='Muthupandian',
    author_email='muthupandiansuresh2003@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)