#To create the version
from setuptools import find_packages,setup
from typing import List

file_path='requirements.txt'
HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function  will return the list of requirement
    '''
    requirements=[]
    with open(file_path) as file_obj:
        for line in file_obj:
            if line.strip() != HYPHEN_E_DOT.strip():
                requirements.append(line.strip())
    return requirements


setup(
    name='sensor',
    version='0.0.1',
    author='Vipul',
    author_email='vipuljain81492@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)