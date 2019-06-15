"""Setup for example-package.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
Templated from:
https://github.com/pypa/sampleproject
"""

from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name
    name="example-package",
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version="0.0.0",
    # This is a one-line description or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#summary
    description="",  # Optional
    # This field corresponds to the "Description" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=long_description,  # Optional
    # This field corresponds to the "Description-Content-Type" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    # valid values are text/plain, text/x-rst, and text/markdown
    long_description_content_type="text/markdown",  # Optional
    # This field corresponds to the "Home-Page" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#home-page-optional
    url="https://github.com/your-account/example-package",  # Optional
    # This should be your name or the name of the organization which owns the
    # project.
    author="your-name",  # Optional
    # This should be a valid email address corresponding to the author listed
    # above.
    author_email="your-email",  # Optional
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # These classifiers are *not* checked by 'pip install'. See instead
        # 'python_requires' below.
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    # This field adds keywords for your project which will appear on the
    # project page.
    # Note that this is a string of words separated by whitespace, not a list.
    keywords="",  # Optional
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(where="src", exclude=["docs", "tests"]),  # Required
    package_dir={"": "src"},
    # Specify which Python versions you support.
    # 'pip install' will check this and refuse to install the project if the version does not match.
    # see
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
    python_requires=">=3.5",
    # This field lists other packages that your project depends on to run.
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[],  # Optional
    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example: $ pip install sampleproject[dev,test]
    extras_require={"dev": ["tox", "pytest", "pytest-cov"]},  # Optional
    # If there are data files included in your packages that need to be
    # installed, specify them here.
    package_data={},  # Optional
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    # data_files=[],  # Optional
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    entry_points={},  # Optional
    # List additional URLs that are relevant to your project as a dict.
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    project_urls={  # Optional
        "Bug Reports": "https://github.com/your-account/example-package/issues",
        "Source": "https://github.com/your-account/example-package/",
    },
)
