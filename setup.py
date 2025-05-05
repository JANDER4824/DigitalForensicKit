from setuptools import setup, find_packages

setup(
    name="DigitalForensicKit",
    version="1.0.0",
    author="JANDER4824",
    description="Herramienta modular de análisis forense digital para memoria, disco, red y logs.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JANDER4824/DigitalForensicKit",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "volatility3>=2.4.1",
        "pytsk3>=20210406",
        "pyewf>=20220102",
        "pandas>=1.3.0",
        "matplotlib>=3.4.2",
        "plotly>=5.1.0",
        "pyshark>=0.4.3",
        "scapy>=2.4.5",
        "Flask>=2.0.0",
        "reportlab>=3.5.0",
        "Jinja2>=3.0.0",
        "PyPDF2>=1.26.0",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "dfk-cli=ui.cli:main"
        ]
    },
    license="GPLv3",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
    test_suite="tests",
)