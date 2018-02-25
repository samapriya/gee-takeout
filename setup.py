from setuptools import setup
from setuptools import find_packages

setup(
    name='geetakeout',
    version='0.1',
    packages=find_packages(),
    package_data={'geetakeout': ['geckodriver','geckodriver.exe']},
    url='https://github.com/samapriya/gee-takeout',
    install_requires=['google-api-python-client >= 1.5.4','earthengine_api ==0.1.134','requests >= 2.18.4','clipboard>=0.0.4','beautifulsoup4 >= 4.6.0',
                      'pytest >= 3.0.0','selenium >=3.9.0','python_dateutil >=2.6.1','pySmartDL==1.2.5'],
    license='Apache 2.0',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: GIS',
    ),
    author='Samapriya Roy',
    author_email='samapriya.roy@gmail.com',
    description='Google Earth Engine Takeout Tool',
    entry_points={
        'console_scripts': [
            'geetakeout=geetakeout.geetakeout:main',
        ],
    },
)
