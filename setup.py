from setuptools import setup, find_packages

setup(
    name="legal_agent",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "faiss-cpu",
        "sentence-transformers",
        "pytest",
        "pytest-cov"
    ],
)
