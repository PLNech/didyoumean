python setup.py sdist bdist_wheel
twine check dist/*
twine upload dist/*
rm -f dist/*
