from setuptools import setup, find_packages

setup(
    name = "regcore",
    version_format='{tag}.dev{commitcount}+{gitsha}',
    license = "public domain", 
    packages = find_packages(),
    include_package_data=True,
    package_data = {
        'regcore': ['templates/search/indexes/regcore/regulation_text.txt'],
    },
    install_requires=[
        'django',
        'django-haystack',
        'jsonschema',
    ],
    classifiers=[
        'License :: Public Domain',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication'
    ],
    setup_requires=['setuptools-git-version'],
)
