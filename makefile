all: test test_cython

install:
	python3 setup.py install

cython:
	python3 setup_cython.py build_ext --inplace	

test:
	PYTHONPATH=. python3 tests/test_deezy.py

test_cython: cython
	PYTHONPATH=. python3 tests/test_deezy.py

build: .PHONY
	python3 setup.py build

clean:
	rm -rf build
	rm -f `find . -name '*.c'`
	rm -f `find . -name '*.so'`

.PHONY:
