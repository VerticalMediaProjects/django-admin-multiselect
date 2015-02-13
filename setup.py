import os
from setuptools import setup, find_packages
setup(
    name='django-admin-multiselect',
    version='0.0.5',
    description='Alternative multiple select widget that works with mobile devices.',
    author='Kreios S.a r.l.',
    author_email='christian.hillerkus@kreios.lu',
    url='https://github.com/kreioslu/django-admin-multiselect',
    download_url='https://github.com/kreioslu/django-admin-multiselect/tarball/0.0.5',
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    keywords=['django', 'admin', 'multiselect'],
    zip_safe=False,
    include_package_data=True,
    install_requires=[]
)
