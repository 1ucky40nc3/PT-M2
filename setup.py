from setuptools import find_packages, setup

setup(
    name="pt_m2",
    version="0.0.1",
    description="A Grammatical Error Correction (GEC) metric based on Pretrained-based (PT-based) models",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="python nlp machine-learning deep-learning",
    license="MIT License",
    url="https://github.com/1ucky40nc3/PT-M2",
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
)
