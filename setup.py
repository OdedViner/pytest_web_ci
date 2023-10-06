from setuptools import setup, find_packages

setup(
    name="web-ci",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "run-test = framework.main:main",
        ],
    },
    install_requires=["pytest", "pytest-ordering", "PyYAML"],
)
