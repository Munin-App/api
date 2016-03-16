from setuptools import setup, find_packages

with open('requirements.txt') as f:
    dependencies = f.read().splitlines()

setup(
    name='munin',
    version='0.0.1',
    author='Mihir Singh (@citruspi)',
    author_email='hello@mihirsingh.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=dependencies
)
