CREATE TABLE naughty_pilots (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    pilotID VARCHAR(255) NOT NULL,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    phoneNumber VARCHAR(255) NOT NULL,
    createDt DATETIME NOT NULL,
    email VARCHAR(255) NOT NULL,
    distance INT NOT NULL,
    datetime DATETIME NOT NULL
)

