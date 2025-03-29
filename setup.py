from setuptools import setup, find_packages

setup(
    name="delinea_auth_plugin",  # Replace with your package name
    version="1.0.0",
    description="A Python module for authenticating with Thycotic/Delinea Secret Server",
    author="Ben Hart",
    author_email="ben@benhart.dev",
    url="https://github.com/cidrbl0ck/delinea_auth_plugin",  # Replace with your repository URL
    packages=find_packages(),
    install_requires=[
        "requests>=2.0.0",
        "typing", # Add any dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
