from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """
    requirement_list = []
    try:
        with open('requirements.txt', 'r') as file:
            requirement_list = [line.strip() for line in file if line.strip() and not line.startswith(('#', '-e'))]
    except FileNotFoundError:
        print("requirements.txt not found. Please create it with your dependencies.")
    return requirement_list

setup(
    name="flipkart",
    version="0.0.1",
    author="Arif Ansari",
    author_email="arif.ansari2024@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)