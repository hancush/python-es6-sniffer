"""
ES6 Sniffer is a simple CLI to identify installed Node packages that may contain ES6 features.
"""
from setuptools import find_packages, setup

dependencies = ['click', 'semantic_version']

setup(
    name='es6_sniffer',
    version='0.1.0',
    url='https://github.com/hancush/python-es6-sniffer',
    license='BSD',
    author='Hannah Cushman Garland',
    author_email='hannah.cushman@gmail.com',
    description='ES6 Sniffer is a simple CLI to identify installed Node packages that may contain ES6 features.',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'es6-sniffer = es6_sniffer.cli:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
