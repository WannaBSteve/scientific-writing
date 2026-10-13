.PHONY: validate test evals audit-example check

validate:
	python3 scripts/check_repo.py
	python3 scripts/check_eval_assets.py

test:
	python3 -m unittest discover -s tests -v

evals:
	python3 scripts/check_eval_assets.py

audit-example:
	python3 scripts/audit_prose.py examples/clean-control.md

check: validate test audit-example
