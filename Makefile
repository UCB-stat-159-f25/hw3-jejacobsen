.PHONY: env html clean

env:
	@if conda env list | grep -q 'hw3-env'; then \
		echo "Updating existing environment..."; \
		conda env update -f environment.yml -n hw3-env; \
	else \
		echo "Creating new environment..."; \
		conda env create -f environment.yml -n hw3-env; \
	fi

html:
	myst build --html

clean:
	rm -rf figures/* audio/* _build/
