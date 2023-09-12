from setuptools import find_packages,setup
from typing import List

def get_req(file_path:str)->List[str]:
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if("-e ." in requirements):
            requirements.remove("-e .")
    return requirements


setup(
name='DSproject',
version='0.0.1',
author="N.V.R.C",
author_email="narravenkataraghucharan03@gmail.com",
packages=find_packages(),
requires=get_req('requirements.txt')
)