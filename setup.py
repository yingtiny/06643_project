from setuptools import setup

setup(
    name="package",
    version="0.0.1",
    description="Project package",
    long_description="""A long multiline description.""",
    maintainer="Ying-Ting Yeh",
    maintainer_email="yingtiny@cmu.edu",
    license="MIT",
    packages=["package"],
    install_requires=[
        "requests",
        "matplotlib",
    ],
)
