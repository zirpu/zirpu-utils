
clean:
	rm -vrf wheelhouse dist build *.egg-info *.pyc */*.pyc .pyenv __pycache__ */__pycache__ *~

wheel:
	python3 setup.py bdist_wheel bdist
