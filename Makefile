shell:
	sqlite3 ./database/database.db;

clean:
	rm -rf ./database/database.db;
	sqlite3 ./database/database.db < ./database/schema.sql

add-fighter:
	cd ./src; python3 main.py --add-fighter 1 --hint 1;

add-coach:
	cd ./src; python3 main.py --add-coach 1 --hint 1;
