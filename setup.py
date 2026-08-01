from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    this function will return list of requirements
    """
    
    requirement_list:List[str] = []
    
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            #process each line
            for line in lines:
                # strip whitespaces and newline charachters
                requirement = line.strip()
                # ignore empty lines and -e.
                
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
             
             
    return requirement_list
print(get_requirements())

setup(
    name = "AI-tarvel-planners",
    version = "0.0.1",
    author = "Anish Shrivastava",
    author_email = "anish09879@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements()
        
        
)