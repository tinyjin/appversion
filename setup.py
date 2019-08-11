from setuptools import setup

setup(
    name='appversion',
    version='0.0.1',
    license='MIT',
    description='Get app version from playstore, appstore',
    keywords='app version playstore appstore',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='tinyjin',
    author_email='baram991103@gmail.com',
    packages=['av'],
    install_requires=['beautifulsoup4', 'requests'],
    include_package_data=True,
    url='https://github.com/tinyjin/appversion',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
