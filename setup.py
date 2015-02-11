import os
from setuptools import setup, find_packages
setup(
    name='django-admin-multiselect',
    version='0.0.1',
    description='Alternative multiple select widget that works with mobile devices.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    author='Paul Dobre',
    author_email='pauldobrero@gmail.com',
    url='https://github.com/VerticalMediaProjects/django-admin-multiselect',
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License (MIT)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    include_package_data=True,
    install_requires=[]
)
