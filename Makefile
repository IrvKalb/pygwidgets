all:

sdist:
	python3 setup.py sdist

install:
	pip3 install --user --force-reinstall --no-index -f dist pygwidgets

clean:
	rm -fr __pycache__ dist MANIFEST *.egg-info src/__pycache__ src/*.egg-info

	
upload:
	twine upload dist/* --verbose
