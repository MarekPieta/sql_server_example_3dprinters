USE Printers3D;
GO

--Calculate and print sum of order prices from @date_start to @date_stop
CREATE PROCEDURE print_sum_order_price @date_start DATETIME, @date_stop DATETIME
AS
	DECLARE @sum DECIMAL(10,2)
	SET @sum = (SELECT SUM(cost) FROM print_3d WHERE (completion_date > @date_start AND completion_date < @date_stop))
	PRINT @sum
GO

--Add filament type compability for a printer
CREATE PROCEDURE add_filament_compability @printer_id INT, @filament_type VARCHAR(10), @speed_grade INT, @quality_grade INT
AS
	DECLARE @t TABLE
	(
	id_filament			INT		NOT NULL
	);
	DECLARE @fil_id AS INT

	INSERT INTO @t
	SELECT id FROM filament WHERE type=@filament_type
	
	WHILE EXISTS (SELECT 1 FROM @t)
	BEGIN
				
		SET @fil_id = (SELECT TOP(1) id_filament FROM @t)
		
		INSERT INTO filament_compability (printer_id, filament_id, speed_grade, quality_grade)
		VALUES	(@printer_id, @fil_id, @speed_grade, @quality_grade);

		DELETE TOP(1) FROM @t;
	END;
GO

--Calculate money earned by printing with a particular printer
CREATE PROCEDURE total_printers_earnings
AS
	SELECT manufacturer, model, [Total Earning] 
	FROM printer_3d
	JOIN 
	(SELECT printer_id, SUM(cost) AS [Total Earning] FROM print_3d WHERE printer_id IS NOT NULL GROUP BY printer_id) p
	ON printer_3d.id = p.printer_id 
GO


--Lists printers which are currently realizing an order 
CREATE PROCEDURE show_busy_printers
AS
	SELECT manufacturer, model, stl_filename, estimated_printing_time
	FROM printer_3d
	JOIN 
	(SELECT printer_id, stl_filename, estimated_printing_time,  due_date FROM print_3d WHERE (printer_id IS NOT NULL AND completion_date IS NULL)) p
	ON printer_3d.id = p.printer_id
GO