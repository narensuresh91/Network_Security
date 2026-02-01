'''
The setup.py file is the installation and packaging script for the project.
Setuptools is the Python library that actually handles the packaging and installation process defined in setup.py
Used to define the configuration of the project such as metadata, dependencies and more.
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function returns the list of requirements 
            """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            ##Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e.
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)


    except FileNotFoundError:
        print('Requirement.txt file not found')

    return requirement_lst

print(get_requirements())

setup(
    name="Network_Security",
    version="0.0.1",
    author="Naren",
    author_email="naren.suresh91@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)