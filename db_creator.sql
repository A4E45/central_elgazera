USE central_elgazera;
CREATE TABLE employee(EmployeeID INT AUTO_INCREMENT NOT NULL,
						name VARCHAR(255) NOT NULL,
						username VARCHAR(255) NOT NULL,
						mail VARCHAR(255) NULL,
						national_id VARCHAR(255) NOT NULL,
						phone VARCHAR(255) NOT NULL,
						address VARCHAR(255) NULL,
						password VARCHAR(255) NOT NULL,
						PRIMARY KEY (EmployeeID)
							);
CREATE TABLE machines(MachineID INT AUTO_INCREMENT NOT NULL,
						machine_name VARCHAR(255) NOT NULL,
						PRIMARY KEY(MachineID)
							);
CREATE TABLE services(service_name VARCHAR(255) NOT NULL,
					serviceID INT NOT NULL AUTO_INCREMENT PRIMARY KEY

		);
CREATE TABLE company_names(companyID INT AUTO_INCREMENT NOT NULL,
                            company_name   VARCHAR(255)  NOT NULL,
                            PRIMARY KEY(companyID)
                            );
CREATE TABLE vodafone_cards_values(cardID INT AUTO_INCREMENT NOT NULL ,
								card_value FLOAT NOT NULL,
                                PRIMARY KEY(cardID)
                                );

CREATE TABLE orange_cards_values(cardID INT AUTO_INCREMENT NOT NULL,
								card_value FLOAT NOT NULL,
                                PRIMARY KEY(cardID));

CREATE TABLE etisalat_cards_values(cardID INT AUTO_INCREMENT NOT NULL,
	card_value FLOAT NOT NULL,
    PRIMARY KEY(cardID));

CREATE TABLE WE_cards_values(cardID INT AUTO_INCREMENT NOT NULL,
	card_value FLOAT NOT NULL,
    PRIMARY KEY(cardID));

CREATE TABLE charge(order_id INT NOT NULL AUTO_INCREMENT,
						phone_number VARCHAR(255) NOT NULL,
						value FLOAT NOT NULL,
						 _date Date NOT NULL,
						 _time TIME NOT NULL,
						 serviceID INT NOT NULL,
						 EmployeeID INT NOT NULL,
						 MachineID INT NOT NULL,
						 FOREIGN KEY (EmployeeID) REFERENCES employee(EmployeeID),
						 FOREIGN KEY (MachineID) REFERENCES machines(MachineID),
						 FOREIGN KEY (serviceID) REFERENCES services(serviceID),
						 KEY (order_id)

						 );

CREATE TABLE accessories(order_id INT NOT NULL AUTO_INCREMENT,
						name VARCHAR(255) NOT NULL,
						 value INT NOT NULL,
						 quantity INT NOT NULL,
						 _date date NOT NULL,
						 _time TIME NOT NULL,
						 EmployeeID INT NOT NULL,
						 FOREIGN KEY (EmployeeID) REFERENCES employee(EmployeeID),
						 KEY (order_id)
						  );

CREATE TABLE accessories_stored(accessoriesID INT NOT NULL AUTO_INCREMENT,
								name VARCHAR(255) NOT NULL,
								price INT NOT NULL,
								quantity INT NOT NULL,
                                PRIMARY KEY(accessoriesID)
							);

CREATE TABLE tobacco(order_id INT NOT NULL AUTO_INCREMENT,
					name VARCHAR(255) NOT NUll,
					value FLOAT NOT NULL,
					num INT NOT NULL,
					_date DATE NOT NULL,
					_time TIME NOT NULL,
					EmployeeID INT NOT NULL,
					FOREIGN KEY (EmployeeID) REFERENCES employee(EmployeeID),
					KEY (order_id)
						);
CREATE TABLE tobacco_stored(tobaccoID INT NOT NULL AUTO_INCREMENT,
					name VARCHAR(255) NOT NUll,
					quantity INT NOT NULL,
					price FLOAT NOT NULL,
					EmployeeID INT NOT NULL,
					FOREIGN KEY (EmployeeID) REFERENCES employee(EmployeeID),
                    PRIMARY KEY(tobaccoID)
						);
CREATE TABLE phone_cards(company_name VARCHAR(255) NOT NULL,
						value FLOAT NOT NULL,
						quantity INT NOT NULL,
						_date DATE NOT NULL,
						_time TIME NOT NULL,
						EmployeeID INT NOT NULL,
						MachineID INT NOT NULL,
						FOREIGN KEY (EmployeeID) REFERENCES employee(EmployeeID),
						FOREIGN KEY (MachineID) REFERENCES machines(MachineID)
					 );
CREATE TABLE elec_cards(client_number VARCHAR(255) NOT NULL,
						value FLOAT NOT NULL,
						type VARCHAR(255) NOT NULL,
						_date DATE NOT NULL,
						_time TIME NOT NULL,
						EmployeeID INT NOT NULL,
						MachineID INT NOT NULL,
						FOREIGN KEY (EmployeeID) REFERENCES employee(EmployeeID),
						FOREIGN KEY (MachineID) REFERENCES machines(MachineID)
						);
CREATE TABLE other(name VARCHAR(255) NOT NULL,
					num INT NOT NULL,
					value FLOAT NOT NULL,
					_date DATE NOT NULL,
					_time TIME NOT NULL,
					order_id INT NOT NULL AUTO_INCREMENT,
					EmployeeID INT NOT NULL,
					FOREIGN KEY (EmployeeID) REFERENCES employee(EmployeeID),
					KEY (order_id)
						);
CREATE TABLE other_stored(otherID INT NOT NULL AUTO_INCREMENT,
							other_name VARCHAR(255) NOT NULL,
                            price FLOAT NOT NULL,
                            quantity INT NOT NULL,
                            PRIMARY KEY(otherID)
);
CREATE TABLE wanted(client_name VARCHAR(255) NOT NULL,
					value FLOAT NOT NULL,
					order_id INT NOT NULL AUTO_INCREMENT,
					_date DATE NOT NULL,
					_time TIME NOT NULL,
					EmployeeID INT NOT NULL,
					KEY (order_id),
					FOREIGN KEY (EmployeeID) REFERENCES employee(EmployeeID)
						);
CREATE TABLE permissions(EmployeeID INT NOT NULL,
						FOREIGN KEY (EmployeeID) REFERENCES employee(EmployeeID),
						is_admin BOOLEAN NOT NULL,
						charge_add BOOLEAN NOT NULL,
						charge_del BOOLEAN NOT NULL,
						charge_info BOOLEAN NOT NULL,
						accessories_add BOOLEAN NOT NULL,
						accessories_del BOOLEAN NOT NULL,
						accessories_info BOOLEAN NOT NULL,
						tobacco_add BOOLEAN NOT NULL,
						tobacco_del BOOLEAN NOT NULL,
						tobacco_info BOOLEAN NOT NULL,
						other_add BOOLEAN NOT NULL,
						other_del BOOLEAN NOT NULL,
						other_info BOOLEAN NOT NULL,
						wanted_add BOOLEAN NOT NULL,
						wanted_del BOOLEAN NOT NULL,
						search_op BOOLEAN NOT NULL,
						setting_add_brand BOOLEAN NOT NULL,
						setting_add_new_brand BOOLEAN NOT NULL,
						setting_edit_brand BOOLEAN NOT NULL,
						add_employee BOOLEAN NOT NULL,
						edit_employee BOOLEAN NOT NULL,
						reports BOOLEAN NOT NULL,
						dailymoment BOOLEAN NOT NULL,
						permissions BOOLEAN NOT NULL
);
