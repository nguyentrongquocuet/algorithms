create:
	python3 script.py create $(filter-out $@,$(MAKECMDGOALS))
