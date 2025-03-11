.PHONY: docs

docs: ## build HTML documentation
	sphinx-build -W --keep-going --color docs/ docs/_build/
linkcheck-docs: ## check for broken links
	sphinx-build -W --keep-going --color -b linkcheck docs/ docs/_build/
