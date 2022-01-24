from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in rfq_development/__init__.py
from rfq_development import __version__ as version

setup(
	name="rfq_development",
	version=version,
	description="microconsaltant",
	author="ME",
	author_email="shantanu",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
