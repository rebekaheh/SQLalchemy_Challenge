CREATE TABLE animal_species(
animal_name VARCHAR,
species VARCHAR);

INSERT INTO animal_species (animal_name, species)
VALUES ('Mickey Mouse', 'duck'), ('Minnie Mouse', 'duck'), ('Donald Duck', 'mouse');

SELECT * FROM animal_species

UPDATE animal_species
SET species = 'mouse'
WHERE animal_name = 'Mickey Mouse';

UPDATE animal_species
SET species = 'mouse'
WHERE animal_name = 'Minnie Mouse';

UPDATE animal_species
SET species = 'duck'
WHERE animal_name = 'Donald Duck';

SELECT * FROM animal_species