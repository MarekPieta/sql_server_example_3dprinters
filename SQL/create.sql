USE Printers3D

--dropping existing tables

IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES where TABLE_NAME='print_3d') 
begin
	DROP TABLE print_3d;
end

IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES where TABLE_NAME='customer') 
begin
	DROP TABLE customer;
end

IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES where TABLE_NAME='filament_compability') 
begin
	DROP TABLE filament_compability;
end

IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES where TABLE_NAME='filament_history') 
begin
	DROP TABLE filament_history;
end

IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES where TABLE_NAME='filament') 
begin
	DROP TABLE filament;
end

IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES where TABLE_NAME='filament_manufacturer') 
begin
	DROP TABLE filament_manufacturer;
end

IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES where TABLE_NAME='part_for_maintenance') 
begin
	DROP TABLE part_for_maintenance;
end

IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES where TABLE_NAME='maintenance') 
begin
	DROP TABLE maintenance;
end

IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES where TABLE_NAME='employee') 
begin
	DROP TABLE employee;
end

IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES where TABLE_NAME='part') 
begin
	DROP TABLE part;
end

IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES where TABLE_NAME='supplier') 
begin
	DROP TABLE supplier;
end

IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES where TABLE_NAME='printer_3d') 
begin
	DROP TABLE printer_3d;
end


--creating tables
CREATE TABLE customer
(
	username		VARCHAR(40)			NOT NULL	PRIMARY KEY,
	password_hash	CHAR(128)			NOT NULL,
	first_name		VARCHAR(40)			NOT NULL,
	last_name		VARCHAR(40)			NOT NULL,
	phone			VARCHAR(40),
	address			VARCHAR(100),
	city			VARCHAR(40),
	loyalty_points	INT					NOT NULL
)

CREATE TABLE printer_3d
(
	id						INT				NOT NULL	IDENTITY(1,1)	PRIMARY KEY,
	manufacturer			VARCHAR(40),
	model					VARCHAR(40),
	nozzle_diameter			DECIMAL(5,3)
)

CREATE TABLE print_3d
(
	id							INT				NOT NULL	PRIMARY KEY								IDENTITY(1,1),
	printer_id					INT							FOREIGN KEY	REFERENCES printer_3d(id),
	customer_username			VARCHAR(40)		NOT NULL	FOREIGN KEY	REFERENCES customer(username),
	due_date					DATETIME,
	completion_date				DATETIME,
	estimated_printing_time		TIME,
	stl_filename				VARCHAR(100),
	cost						DECIMAL(9,2),
	filament_type				VARCHAR(10),
	filament_color				VARCHAR(40)
)

CREATE TABLE filament_manufacturer
(
	name				VARCHAR(40)		NOT NULL PRIMARY KEY,
	homepage_address	VARCHAR(60),
	rating_quality		INT,
	rating_punctuality	INT
)

CREATE TABLE filament
(
	id							INT				NOT NULL	PRIMARY KEY	IDENTITY(1,1),
	manufacturer				VARCHAR(40)		FOREIGN KEY REFERENCES filament_manufacturer(name),
	type						VARCHAR(10)		NOT NULL,
	diameter					DECIMAL(4,2),
	melt_temperature_min		INT,
	melt_temperature_max		INT,
	melt_temperature_optimal	INT,
	quality						INT,
	price						DECIMAL(9,2),
	color						VARCHAR(40)
)

CREATE TABLE filament_compability
(
	id					INT			NOT NULL	PRIMARY KEY	IDENTITY(1,1),
	printer_id			INT			NOT NULL	FOREIGN KEY REFERENCES printer_3d(id),
	filament_id			INT			NOT NULL	FOREIGN KEY REFERENCES filament(id),
	speed_grade			INT,
	quality_grade		INT
)

CREATE TABLE filament_history
(
	id					INT				NOT NULL PRIMARY KEY	IDENTITY(1,1),
	filament_id			INT				NOT NULL FOREIGN KEY REFERENCES filament(id),
	order_date			DATETIME,
	delivered_date		DATETIME,
	added_amount		DECIMAL(7,3)	NOT NULL
)


CREATE TABLE employee
(
	id					INT				NOT NULL PRIMARY KEY	IDENTITY(1,1),
	first_name			VARCHAR(40),
	last_name			VARCHAR(40),
	salary				DECIMAL(10,2)
)


CREATE TABLE maintenance
(
	id					INT				NOT NULL PRIMARY KEY	IDENTITY(1,1),
	printer_id			INT				NOT NULL FOREIGN KEY REFERENCES printer_3d(id),
	employee_id			INT				NOT NULL FOREIGN KEY REFERENCES employee(id),
	fix					BIT				NOT NULL,
	description			VARCHAR(400)
)

CREATE TABLE supplier
(
	name				VARCHAR(40)		PRIMARY KEY,
	homepage_address	VARCHAR(40),
	delivery_cost		DECIMAL(9,2),
	delivery_days		INT
)

CREATE TABLE part
(
	id				INT				NOT NULL	PRIMARY KEY	IDENTITY(1,1),
	supplier_name	VARCHAR(40)		NOT NULL	FOREIGN KEY REFERENCES supplier(name),
	name			VARCHAR(100)	NOT NULL,
	manufacturer	VARCHAR(40),
	price			DECIMAL(8,2),
	amount			INT,
	min_amount		INT
)

CREATE TABLE part_for_maintenance
(
	id					INT		NOT NULL PRIMARY KEY IDENTITY(1,1),
	maintenance_id		INT		NOT NULL FOREIGN KEY REFERENCES maintenance(id),
	part_id				INT		NOT NULL FOREIGN KEY REFERENCES part(id),
	number_of_parts		INT		NOT NULL
)