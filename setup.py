import setuptools

setuptools.setup(
    name="ProgressBar Plug",
    version="0.1.0",
    url="https://jonas.steinka.mp",

    author="Jonas Steinkamp",
    author_email="jonas@steinka.mp",

    description="A progressbar for the OpenHTF framework.",
    long_description=open('README.md').read(),

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 2.7',
    ],

    include_package_data=True,
    packages=setuptools.find_packages(),

    install_requires=[x.strip() for x in open('requirements.txt').readlines()]
)
