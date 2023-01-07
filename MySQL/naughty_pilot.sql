
SET foreign_key_checks = 1;

CREATE TABLE naughty_pilot_info (
pilotID VARCHAR(255) NOT NULL PRIMARY KEY,
firstName VARCHAR(255) NOT NULL,
lastName VARCHAR(255) NOT NULL,
phoneNumber VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL
);

CREATE TABLE violation_info (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
pilotID VARCHAR(255),
distance INT NOT NULL,
X INT NOT NULL,
Y INT NOT NULL,
timestamp DATETIME NOT NULL,
FOREIGN KEY (pilotID) REFERENCES naughty_pilot_info(pilotID)
);

