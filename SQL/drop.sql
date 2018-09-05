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