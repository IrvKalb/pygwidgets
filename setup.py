from setuptools import find_packages, setup

setup(
    name='pygwidgets',
    version='1.0.1',
    author='Irv Kalb',
    author_email='Irv@furrypants.com',
    description='User interface widgets for use with Pygame',
    long_description='User interface widgets for building programs using Pygame',
    packages=find_packages(),
    include_package_data=True,
    license="BSD",
    url='https://github.com/IrvKalb/pygwidgets',
    install_requires=[
        'pygame>=1.9',
        ],
    keywords="pygame widgets user interface buttons text dragger animation image",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent"
      ]
    )
