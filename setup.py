from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="emastery",
    version="2.0.6",
    author="Ekyi Quarm Jnr",
    author_email="ekyi.quarm@acity.edu.gh",
    description="Audio Matching and Mastering Python Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    license="GPLv3",
    url="https://github.com/quarm00/MASTER.git",
    packages=find_packages(include=["matchering", "matchering.*"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Other Audience",
        "Natural Language :: English",
        "Topic :: Artistic Software",
        "Topic :: Multimedia",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Topic :: Multimedia :: Sound/Audio :: Conversion",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
)
