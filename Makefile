setup:
	@python3 -m pip install -r requirements.txt

run:
	@python3 app.py --hosp=${hosp} --randon=${randon} --qnt_point=${qntd}

.PHONY: setup
