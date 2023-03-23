from setuptools import find_packages, setup

setup(
    name="pt_m2",
    version="0.0.1",
    description="A Grammatical Error Correction (GEC) metric based on Pretrained-based (PT-based) models",
    long_description=open("readme.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords=[
        "python",
        "nlp",
        "natural-language-processing",
        "ml",
        "machine-learning",
        "deep-learning",
        "gec",
        "grammatical-error-correction"
    ],
    license="MIT License",
    url="https://github.com/1ucky40nc3/PT-M2",
    packages=find_packages(exclude=[]),
)
