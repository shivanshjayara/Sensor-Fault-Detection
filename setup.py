from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return the list of requirements
    """
    requirement_list:List[str]=[] 
    return requirement_list


setup(
    name='sensor',
    version="0.0.1",
    author="ineuron",
    author_email="shivansh.jayara2991gmail.com",
    packages=find_packages(),
    install_requires=get_requirements() #["pymongo==4.2.0"],

)

# run this command: "python setup.py install"