from setuptools import setup, find_packages

setup(
    name='your-package',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'run-test = new_file.new:main',
        ],
    },
    install_requires=[
        "pytest==6.2.5",
        "pytest-ordering==0.6",
        "PyYAML==6.0.1"
    ],
)
