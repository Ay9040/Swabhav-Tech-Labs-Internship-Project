CREATE TABLE Country(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	country_name VARCHAR(255) NOT NULL,
	PRIMARY KEY(id)
);

CREATE TABLE State(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	state_name VARCHAR(255) UNIQUE NOT NULL,
	country_id INT NOT NULL,
	FOREIGN KEY(country_id) REFERENCES country(id),
	PRIMARY KEY(id)
);

CREATE TABLE Industry(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	industry_name VARCHAR(255) UNIQUE NOT NULL,
	PRIMARY KEY(id)
);

CREATE TABLE Venue(
	id INT UNIQUE NOT NULL AUTO_INCREMENT ,
	city VARCHAR(255) NOT NULL,
	address VARCHAR(255) NOT NULL,
	country_id INT NOT NULL,
	state_id INT NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(country_id) REFERENCES Country(id),
	FOREIGN KEY(state_id) REFERENCES State(id)
);

CREATE TABLE EventTable(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	event_name VARCHAR(255) NOT NULL,
	booking_start_date datetime NOT NULL,
	start_date datetime NOT NULL,
	end_date datetime NOT NULL,
	venue_id INT NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(venue_id) REFERENCES Venue(id)
);

CREATE TABLE Stall(
	id INT UNIQUE NOT NULL AUTO_INCREMENT ,
	stall_no INT NOT NULL,
	price FLOAT NOT NULL,
	stall_size INT NOT NULL,
	isBooked BOOL NOT NULL,
	event_id INT UNIQUE NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(event_id) REFERENCES EventTable(id)
);

CREATE TABLE Visitor(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	first_name VARCHAR(255) NOT NULL ,
	last_name VARCHAR(255) NOT NULL,
	address VARCHAR(255) NOT NULL,
	pincode INT NOT NULL,
	mobile_no VARCHAR(13) NOT NULL,
	email_id VARCHAR(255) NOT NULL,
	dob DATETIME NOT NULL,
	gender BOOL NOT NULL,
	PRIMARY KEY(id) 
);

CREATE TABLE Exhibitor(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	exhibitor_name VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL,
	phoneno VARCHAR(255) NOT NULL,
	company_name VARCHAR(255),
	company_description VARCHAR(255),
	address VARCHAR(255),
	pincode INT NOT NULL,
	industry_id INT UNIQUE NOT NULL,
	country_id INT UNIQUE NOT NULL,
	state_id INT UNIQUE NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(industry_id) REFERENCES industry(id),
	FOREIGN KEY(country_id) REFERENCES country(id),
	FOREIGN KEY(state_id) REFERENCES state(id)
);

CREATE TABLE Booking(
	id INT unique NOT NULL AUTO_INCREMENT,
	booking_date datetime NOT NULL,
	total_amount float NOT NULL,
	event_id INT UNIQUE NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(event_id) REFERENCES eventtable(id)
);

CREATE TABLE BookingStallMap(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	booking_id INT,
	event_id INT,
	stall_id INT,
	PRIMARY KEY(id),
	FOREIGN KEY(booking_id) REFERENCES booking(id),
	FOREIGN KEY(event_id) REFERENCES eventtable(id),
	FOREIGN KEY(stall_id) REFERENCES stall(id)
);

CREATE TABLE MegaConsumerCard(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	spend INT NOT NULL,
	spend_date DATETIME NOT NULL,
	payment_mode VARCHAR(255),
	event_id INT,
	booking_id INT,
	visitor_id INT,
	PRIMARY KEY(id),
	FOREIGN KEY(event_id) REFERENCES eventtable(id),
	FOREIGN KEY(booking_id) REFERENCES booking(id),
	FOREIGN KEY(visitor_id) REFERENCES visitor(id)
);

INSERT INTO country (id,country_name) VALUES
	(1, 'India');

INSERT INTO state (id,state_name,country_id) VALUES
	(1, 'Maharashtra', 1),
	(2, 'Gujrat', 1);


