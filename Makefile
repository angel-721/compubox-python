shell:
	sqlite3 ./database/database.db;

clean:
	rm -rf ./database/database.db;
	sqlite3 ./database/database.db < ./database/schema.sql

add-fighter:
	cd ./src; python3 main.py --add-fighter 1 --hint 1;

add-coach:
	cd ./src; python3 main.py --add-coach 1 --hint 1;

add-fight:
	cd ./src; python3 main.py --add-fight 1 --hint 1;
	
add-round:
	cd ./src; python3 main.py --add-round 1 --hint 1;

add-tournament:
	cd ./src; python3 main.py --add-tournament 1 --hint 1;

populate:
	cd ./src; python3 main.py -p 1;

interesting:
	cd ./src; python3 main.py -i 1;

install:
	pip install -r ./requirements.txt

tests:
	pytest -v -color=yes