# coding: utf-8

"""
    API Employment Verification Sandbox

    This API lets you verify a person employment status. If a person has a job it also returns the industrial sector and the industry COVID risk segment.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: api@circulodecredito.com.mx
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "apihub-emplotmentverification-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="API Employment Verification Sandbox",
    author_email="api@circulodecredito.com.mx",
    url="",
    keywords=["Swagger", "API Employment Verification Sandbox"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This API lets you verify a person employment status. If a person has a job it also returns the industrial sector and the industry COVID risk segment.  # noqa: E501
    """
)
