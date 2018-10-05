from distutils.core import setup

setup(
    name='pygwidgets',
    version='0.9.0',
    author='Irv Kalb',
    author_email='Irv@furrypants.com',
    description='User interface widgets for use with Pygame',
    py_modules=['pygwidgets'],
    package_dir = {'': 'src'},
    url='http://www.furrypants.com/',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: BSD2-Clause License",
        "Operating System :: OS Independent",
      ]
    )
