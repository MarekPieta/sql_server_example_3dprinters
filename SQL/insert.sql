use Printers3D

INSERT INTO customer (username, password_hash, first_name, last_name, phone,address, city, loyalty_points) 
VALUES ('JKowalski', '73461cc279e0e1b0d11ba54de652ccc047567f5380f6d6aa6f4f819aab92eaba19a7fda16ea0e6abd1dcd67d42b0928e2fe68a3fbe3afec7dbf325cab0abb364', 'Jan', 'Kowalski', '678564567', 'Biala 3', 'Krakow', 0),
	   ('jkh','73461cc279e0e1b0d11ba54de652ccc047567f5380f6d6aa6f4f819aab92eaba19a7fda16ea0e6abd1dcd67d42b0928e2fe68a3fbe3afec7dbf325cab0abb364', 'Karol', 'Raport', '345094789', 'Krowodrza 3', 'Warszawa', 20),
	   ('zxcv','73461cc279e0e1b0d11ba54de652ccc047567f5380f6d6aa6f4f819aab92eaba19a7fda16ea0e6abd1dcd67d42b0928e2fe68a3fbe3afec7dbf325cab0abb364', 'Jacek', 'Mysz', '123098234', 'Bracka 4', 'Krakow', 40),
	   ('nanana','73461cc279e0e1b0d11ba54de652ccc047567f5380f6d6aa6f4f819aab92eaba19a7fda16ea0e6abd1dcd67d42b0928e2fe68a3fbe3afec7dbf325cab0abb364', 'Halina', 'Szprot', '123653745', 'Tarnowska 3', 'Tarnow', 70),
	   ('Dom1234','73461cc279e0e1b0d11ba54de652ccc047567f5380f6d6aa6f4f819aab92eaba19a7fda16ea0e6abd1dcd67d42b0928e2fe68a3fbe3afec7dbf325cab0abb364', 'Tadeusz', 'Wanna', '235985890', 'Koscielna 4', 'Olsztyn', 40),
	   ('Olek2','73461cc279e0e1b0d11ba54de652ccc047567f5380f6d6aa6f4f819aab92eaba19a7fda16ea0e6abd1dcd67d42b0928e2fe68a3fbe3afec7dbf325cab0abb364', 'Aleksander', 'Tama', '235654645', 'Wroclawska 4', 'Dabrowa Gornicza', 2),
	   ('Rimm3','73461cc279e0e1b0d11ba54de652ccc047567f5380f6d6aa6f4f819aab92eaba19a7fda16ea0e6abd1dcd67d42b0928e2fe68a3fbe3afec7dbf325cab0abb364', 'Ryszard', 'Abacki', '346753235', 'Mila 256', 'Wroclaw', 4),
	   ('Rimm34','73461cc279e0e1b0d11ba54de652ccc047567f5380f6d6aa6f4f819aab92eaba19a7fda16ea0e6abd1dcd67d42b0928e2fe68a3fbe3afec7dbf325cab0abb364', 'Ryszard', 'Arbuz', '3467532235', 'Mila 256', 'Wroclaw', 4),
	   ('Rimm345','73461cc279e0e1b0d11ba54de652ccc047567f5380f6d6aa6f4f819aab92eaba19a7fda16ea0e6abd1dcd67d42b0928e2fe68a3fbe3afec7dbf325cab0abb364', 'Ryszard', 'Arbuz', '3235', 'Mila 256', 'Wroclaw', 4),
	   ('Rimm3455','73461cc279e0e1b0d11ba54de652ccc047567f5380f6d6aa6f4f819aab92eaba19a7fda16ea0e6abd1dcd67d42b0928e2fe68a3fbe3afec7dbf325cab0abb364', 'Ryszard', 'Arbuz', '235235J35', 'Mila 256', 'Wroclaw', 4);
 
INSERT INTO printer_3d (manufacturer, model, nozzle_diameter)
VALUES	('Zordon', 'M980', 0.3),
		('Anycube', 'Z235', 0.2),
		('Tajfun', 'Z32', 0.1),
		('Own Creation', 'Owly', 0.3);

INSERT INTO print_3d (printer_id, customer_username, due_date, completion_date, estimated_printing_time, stl_filename, cost, filament_type, filament_color)
VALUES	(NULL, 'zxcv', '2018-05-08', NULL, '12:34', 'okon.stl', 20.0, 'ABS', 'blue'),
		(NULL, 'JKowalski', '2018-05-10', NULL, '5:30', 'ozz3.stl', 300.0, 'ABS', 'pink'),
		(NULL, 'JKowalski', '2018-08-7', NULL, '6:20', 'sdf.stl', 5.05, 'ABS', 'red'),
		(NULL, 'JKowalski', '2018-06-3', NULL, '3:20', 'rabbit.stl', 24.05, 'PLA', 'black'),
		(NULL, 'JKowalski', '2018-07-5', NULL, '8:20', 'jar.stl', 23.05, 'PLA', 'black'),
		(NULL, 'JKowalski', '2018-06-15', NULL, '7:20', 'rabbit2.stl', 76.05, 'ABS', 'black'),
		(1, 'Olek2', '2018-06-30', NULL, '20:20', 'alice.stl', 5.05, 'PLA', 'yellow'),
		(2, 'Olek2', '2018-06-2', NULL, '1:20', 'mini_home.stl', 5.05, 'PLA', 'pink'),
		(1, 'nanana', '2018-05-2', '2018-04-7', '20:20', 'mini_pillow.stl', 1552.23, 'PLA', 'pink'),
		(1, 'nanana', '2018-05-2', '2018-04-1', '3:20', 'crow.stl', 123.35, 'PLA', 'pink'),
		(1, 'nanana', '2018-05-5', '2018-04-3', '2:20', 'object.stl', 10.12, 'PLA', 'pink'),
		(1, 'nanana', '2018-05-6', '2018-04-3', '1:20', 'to.stl', 20.05, 'PLA', 'pink'),
		(1, 'nanana', '2018-05-7', '2018-04-3', '1:20', 'me.stl', 130.05, 'PLA', 'pink');

INSERT INTO filament_manufacturer (name, homepage_address, rating_quality, rating_punctuality)
VALUES	('Ink3', 'http://www.ink.pl', 40, 96),
		('Bunny', 'http://www.bunny.en', 50, 36),
		('Cosmos', 'http://www.cosmos.io', 90, 56),
		('Plastik', 'http://www.plastik.pl', 10, 20);

INSERT INTO filament (manufacturer, type, diameter, melt_temperature_min, melt_temperature_max, melt_temperature_optimal, quality, price, color )
VALUES	('Ink3', 'PLA', 1.75, 180, 200, 190, 20, 70.0, 'black'),
		('Ink3', 'PLA', 1.75, 180, 200, 190, 20, 70.0, 'red'),
		('Ink3', 'PLA', 1.75, 180, 200, 190, 20, 70.0, 'blue'),
		('Ink3', 'PLA', 1.75, 180, 200, 190, 20, 70.0, 'pink'),
		('Ink3', 'PLA', 1.75, 180, 200, 190, 20, 70.0, 'yellow'),
		('Plastik', 'ABS', 1.75, 205, 225, 240, 20, 80.0, 'black'),
		('Plastik', 'ABS', 1.75, 200, 220, 230, 20, 80.0, 'red'),
		('Plastik', 'ABS', 1.75, 200, 220, 230, 20, 80.0, 'blue'),
		('Plastik', 'ABS', 1.75, 200, 220, 230, 20, 80.0, 'yellow');

INSERT INTO filament_compability (printer_id, filament_id, speed_grade, quality_grade)
VALUES	(1, 6, 40, 70),
		(1, 7, 40, 70),
		(1, 8, 40, 70),
		(1, 9, 40, 70);


INSERT INTO filament_history (filament_id, order_date, delivered_date, added_amount)
VALUES	(1, '2018-01-30', '2018-01-31', 3.0),
		(2, '2018-01-30', '2018-01-31', 3.0),
		(3, '2018-01-30', '2018-01-31', 3.0),
		(4, '2018-01-30', '2018-01-31', 3.0),
		(5, '2018-01-30', '2018-01-31', 3.0),
		(6, '2018-02-3', '2018-02-6', 1.0),
		(7, '2018-02-3', '2018-02-6', 1.0),
		(8, '2018-02-3', '2018-02-6', 1.0),
		(9, '2018-02-3', '2018-02-6', 1.0),
		(1, '2018-03-08', '2018-03-08', -0.5),
		(1, '2018-03-10', '2018-03-10', -0.1),
		(3, '2018-03-10', '2018-03-10', -0.34),
		(3, '2018-03-12', '2018-03-12', -0.23);

INSERT INTO employee (first_name, last_name, salary)
VALUES	('Jacek', 'Nowak', 2000),
		('Michal', 'Traktor', 2500),
		('Krzysztof', 'Telefon', 3200),
		('Grzegorz', 'Brzeczyszczykiewicz', 2800),
		('Andrzej', 'Wywrotka', 4300);

INSERT INTO maintenance (printer_id, employee_id, fix, description)
VALUES	(1, 2, 1, 'Nozzle exchange'),
		(1, 2, 1, 'Heat block exchange'),
		(2, 4, 0, 'Lubrication'),
		(3, 5, 0, 'Lubrication'),
		(3, 1, 1, 'Nozzle exchange');

INSERT INTO supplier (name, homepage_address, delivery_cost, delivery_days)
VALUES	('Printo', 'http://www.printo.pl', 10.0, 2),
		('BestDeals', 'http://www.bestdeals.eu', 20.0, 1),
		('NoLess', 'http://www.noless.en', 5.0, 5);

INSERT INTO part (supplier_name, name, manufacturer, price, amount, min_amount)
VALUES	('Printo', 'Lubricant b11', 'DIY Tools', 12.50, 5, 2),
		('Printo', 'Lubricant z23', 'DIY Tools', 22.50, 3, 1),
		('NoLess', 'Nozzlle 0.2', 'Printerss', 3.40, 4 , 3),
		('NoLess', 'Nozzlle 0.3', 'Printerss', 3.40, 5 , 3),
		('NoLess', 'Nozzlle 0.4', 'Printerss', 3.40, 6 , 3),
		('NoLess', 'Nozzlle 0.5', 'Printerss', 3.40, 7 , 3),
		('NoLess', 'Heat block', 'WePrint', 5.00, 1, 2),
		('NoLess', 'Turbo Heat block', 'WePrint', 5.00, 1, 2);


INSERT INTO part_for_maintenance (maintenance_id, part_id, number_of_parts)
VALUES	(3, 1, 0),
		(4, 2, 0),
		(1, 6, 1),
		(2, 5, 1),
		(5, 4, 2);