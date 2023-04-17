# setup.py
import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='medical_translation',
    version='0.0.1',
    author='Clara Richter',
    author_email='cr1100@georgetown.edu',
    description='Using NLP to better understand medical documents.', 
    long_description=long_description, 
    long_description_content_type='text/markdown', 
    packages=setuptools.find_packages(), 
    python_requires='>=3.6'
)