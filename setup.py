"""Setup script for PeTTa Jupyter kernel

Installation:
    # Set PETTA_PATH to your PeTTa installation directory
    export PETTA_PATH=/path/to/PeTTa

    # Install the kernel
    pip install -e /path/to/jupyter-petta-kernel

Or use the provided install.sh script for automatic installation.
"""

from setuptools import setup, find_packages

setup(
    name='petta-jupyter',
    version='0.1.0',
    description='Jupyter kernel for PeTTa (MeTTa language)',
    long_description=open('README.md').read() if __file__ else '',
    long_description_content_type='text/markdown',
    author='SingularityNET',
    url='https://github.com/trueagi-io/jupyter-petta-kernel',
    packages=find_packages(),
    package_data={
        'petta_jupyter': ['../resources/kernel.json'],
    },
    include_package_data=True,
    install_requires=[
        'ipykernel>=6.0.0',
        'janus-swi>=1.5.0',
    ],
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Framework :: Jupyter',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
