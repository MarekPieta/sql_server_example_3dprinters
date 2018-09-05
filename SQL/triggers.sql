USE Printers3D
GO

--Automatically adding loyalty points for prints

CREATE TRIGGER trg_loyalty_points_add ON print_3D
FOR INSERT
AS
	DECLARE @t TABLE
	(
		customer_username VARCHAR(40), 
		new_points INT
	)
	DECLARE @n VARCHAR(40) 
	DECLARE @n_p INT
	
	INSERT INTO @t
	SELECT customer_username, (added + loyalty_points) AS new_points 
	FROM (SELECT customer_username, CAST(SUM(cost)AS INT) AS added FROM inserted GROUP BY customer_username) p
	JOIN customer ON customer.username = p.customer_username

	WHILE EXISTS (SELECT 1 FROM @t)
    BEGIN
        SET @n = (SELECT TOP 1 customer_username FROM @t);
		SET @n_p = (SELECT TOP 1 new_points FROM @t);
        
		UPDATE customer
		SET customer.loyalty_points=@n_p 
		WHERE customer.username=@n
		
		DELETE TOP(1) FROM @t;
    END
GO

--Checking on insert if customer telephone number is proper

CREATE TRIGGER customer_insert_properly
ON customer
INSTEAD OF INSERT
AS
	DECLARE @i TABLE (
    username		VARCHAR(40)			NOT NULL	PRIMARY KEY,
	password_hash	CHAR(128)			NOT NULL,
	first_name		VARCHAR(40)			NOT NULL,
	last_name		VARCHAR(40)			NOT NULL,
	phone			VARCHAR(40),
	address			VARCHAR(100),
	city			VARCHAR(40),
	loyalty_points	INT					NOT NULL
	);
	DECLARE @p VARCHAR(40)

	INSERT INTO @i
	SELECT * FROM inserted

	WHILE EXISTS (SELECT 1 FROM @i)
		BEGIN
			SET @p = (SELECT TOP 1 phone FROM @i);
			if ( (LEN(@p) != 9) OR (@p LIKE '%[^0123456789]%'))
			BEGIN
				PRINT 'Number has to be 9 digit length and digits have to be numeric'
			END
			ELSE
			BEGIN
				INSERT INTO customer SELECT TOP(1) * FROM @i
				PRINT 'OK'
			END
			DELETE TOP(1) FROM @i;
		END;
GO


--Automatically reducing number of parts in stock while adding it to maintenance
CREATE TRIGGER part_amount_updater
ON part_for_maintenance
AFTER INSERT
AS
	DECLARE @p TABLE
	(
	id					INT		NOT NULL,
	maintenance_id		INT		NOT NULL,
	part_id				INT		NOT NULL,
	number_of_parts		INT		NOT NULL
	);
	DECLARE @number_parts INT 
	DECLARE @p_id INT
 
	INSERT INTO @p 
	SELECT * FROM inserted;
	
	WHILE EXISTS (SELECT 1 FROM @p)
	BEGIN
		SET @number_parts = (SELECT TOP(1) number_of_parts FROM @p)		
		SET @p_id = (SELECT TOP(1) part_id FROM @p)
		
		UPDATE part
		SET part.amount -= @number_parts
		WHERE part.id = @p_id 
		DELETE TOP(1) FROM @p;
	END;

GO