create table person (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	date_of_birth DATE NOT NULL
);

insert into person (first_name, last_name, date_of_birth) values ('Mona', 'Kernaghan', '2023-01-24');
insert into person (first_name, last_name, date_of_birth) values ('Estele', 'Bridgwood', '2016-11-29');
insert into person (first_name, last_name, date_of_birth) values ('Alys', 'Futter', '2015-04-09');
insert into person (first_name, last_name, date_of_birth) values ('Wilmer', 'Carpenter', '2013-03-01');
insert into person (first_name, last_name, date_of_birth) values ('Barrett', 'Blachford', '1996-10-23');
insert into person (first_name, last_name, date_of_birth) values ('Darlleen', 'Truss', '2001-12-27');
insert into person (first_name, last_name, date_of_birth) values ('Sander', 'McGuffog', '2022-11-12');
insert into person (first_name, last_name, date_of_birth) values ('Ambrosio', 'Jacquemet',  '2021-02-12');
insert into person (first_name, last_name, date_of_birth) values ('Yehudit', 'Gedge', '1996-09-21');
insert into person (first_name, last_name, date_of_birth) values ('Erika', 'Grewar', '1996-07-06');
