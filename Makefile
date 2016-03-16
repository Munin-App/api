COMMIT:=$(shell git log -1 --pretty=format:'%H')
BRANCH:=$(TRAVIS_BRANCH)

ifeq ($(strip $(BRANCH)),)
	BRANCH:=$(shell git branch | sed -n -e 's/^\* \(.*\)/\1/p')
endif

all: clean bin

clean:

	rm -rf ./build
	rm -rf ./dist
	rm -rf ./release
	rm -rf ./munin.egg-info

test:
	python setup.py test

dist: test
	python setup.py bdist_wheel

release: clean dist

	mkdir release

	mv dist/* dist/munin-py2-none-any.whl
	cd dist && zip -r ../dist.zip .

	cp dist.zip release/$(COMMIT).zip
	cp dist.zip release/$(BRANCH).zip

	rm dist.zip

.PHONY: clean
