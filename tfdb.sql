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
	booking_start_date date NOT NULL,
	start_date date NOT NULL,
	end_date date NOT NULL,
	venue_id INT NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(venue_id) REFERENCES Venue(id) ON DELETE CASCADE
);

CREATE TABLE Stall(
	id INT UNIQUE NOT NULL AUTO_INCREMENT ,
	stall_no INT NOT NULL,
	price FLOAT NOT NULL,
	stall_size INT NOT NULL,
	isBooked BOOL NOT NULL,
	event_id INT NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(event_id) REFERENCES EventTable(id) ON DELETE CASCADE
);

CREATE TABLE Visitor(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	first_name VARCHAR(255) NOT NULL ,
	last_name VARCHAR(255) NOT NULL,
	address VARCHAR(255) NOT NULL,
	pincode INT NOT NULL,
	mobile_no VARCHAR(13) NOT NULL,
	email_id VARCHAR(255) NOT NULL,
	dob date NOT NULL,
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
	industry_id INT NOT NULL,
	country_id INT NOT NULL,
	state_id INT NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(industry_id) REFERENCES industry(id),
	FOREIGN KEY(country_id) REFERENCES country(id),
	FOREIGN KEY(state_id) REFERENCES state(id)
);

CREATE TABLE Booking(
	id INT unique NOT NULL AUTO_INCREMENT,
	booking_date date NOT NULL,
	total_amount float NOT NULL,
	event_id INT NOT NULL,
	exhibitor_id INT NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(exhibitor_id) REFERENCES exhibitor(id) ON DELETE CASCADE,
	FOREIGN KEY(event_id) REFERENCES eventtable(id) ON DELETE CASCADE
);

CREATE TABLE BookingStallMap(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	booking_id INT,
	event_id INT,
	stall_id INT,
	PRIMARY KEY(id),
	FOREIGN KEY(booking_id) REFERENCES booking(id) ON DELETE CASCADE,
	FOREIGN KEY(event_id) REFERENCES eventtable(id) ON DELETE CASCADE,
	FOREIGN KEY(stall_id) REFERENCES stall(id) ON DELETE CASCADE
);

CREATE TABLE MegaConsumerCard(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	spend INT NOT NULL,
	spend_date date NOT NULL,
	payment_mode VARCHAR(255),
	event_id INT,
	booking_id INT,
	visitor_id INT,
	PRIMARY KEY(id),
	FOREIGN KEY(event_id) REFERENCES eventtable(id) ON DELETE CASCADE,
	FOREIGN KEY(booking_id) REFERENCES booking(id) ON DELETE CASCADE,
	FOREIGN KEY(visitor_id) REFERENCES visitor(id) ON DELETE CASCADE
);


INSERT INTO tradefairbooking.country(country_name) SELECT c.Name  FROM world.country c;
INSERT INTO industry(industry_name) VALUES("Other"),("Sport"),("Technology"),("IT"),("Food"),("Financial Services"),("Defence"),("Automobile"),("Agriculture");
INSERT INTO state(state_name, country_id) VALUES ('Maharashtra', 100), ("Andhra Pradesh",100),("Arunachal Pradesh",100),("Assam",100),("Bihar",100),("Chhattisgarh",100),("Goa",100),("Gujarat",100),("Haryana",100),("Himachal Pradesh",100),("Jammu and Kashmir",100),("Jharkhand",100),("Karnataka",100),("Kerala",100),("Madhya Pradesh",100),("Manipur",100),("Meghalaya",100),("Mizoram",100),("Nagaland",100),("Odisha",100),("Punjab",100),("Rajasthan",100),("Sikkim",100),("Tamil Nadu",100),("Telangana",100),("Tripura",100),("Uttar Pradesh",100),("Uttarakhand",100),("West Bengal",100),("Andaman and Nicobar Islands",100),("Chandigarh",100),("Dadra and Nagar Haveli",100),("Daman and Diu",100),("Lakshadweep",100),("National Capital Territory of Delhi",100),("Puducherry",100);