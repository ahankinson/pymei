try:
	from setuptools import setup, find_packages
except ImportError:
	from ez_setup import use_setuptools
	use_setuptools()
	from setuptools import setup, find_packages

longdesc = """ Long description """

setup(
	name = 'pymei',
	long_description = longdesc,
	version = '0.1',
	url = "http://www.musiclibs.net/pymei",
	include_package_data=True
)

