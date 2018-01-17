from setuptools import setup, find_packages

with open ('README.rst',r) as f:
    readme = f.read()

setup(
    name='bgbackup',
    version='0.1.0'
    description='Database backup locally or to AWS s3.'
    long_desctiption=readme,
    author='Kasun Madura Rathanayaka',
    author_email='kasunmaduraeng@gmail.com',
    packages=find_packages('src'),
    package_dir={'':'src'},
    installl_requires=[]
)
