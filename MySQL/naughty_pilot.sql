CREATE TABLE naughty_pilot_info (
pilotID VARCHAR(255) NOT NULL,
firstName VARCHAR(255) NOT NULL,
lastName VARCHAR(255) NOT NULL,
phoneNumber VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL
);

CREATE TABLE naughty_pilot_drone (
id INT NOT NULL,
distance INT NOT NULL,
X INT NOT NULL,
Y INT NOT NULL,
timestamp DATETIME NOT NULL,
FOREIGN KEY (id) REFERENCES naughty_pilot_info(id)
);
