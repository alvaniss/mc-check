from setuptools import setup, find_packages

setup(
    name="mc-check",
    version="1.0.1",
    description="CLI tool to check Minecraft server status using the mcsrvstat.us API",
    author="Dmitrii Orlovski",
    author_email="alvaniss1g@gmail.com",
    url="https://github.com/alvaniss/mc-check",
    license="GPL-3.0",
    py_modules=["mc-check"],
    install_requires=[
        "requests>=2.20.0"
    ],
    entry_points={
        "console_scripts": [
            "mc-check=mc_check:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)