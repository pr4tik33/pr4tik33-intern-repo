## What is the purpose of database migrations in TypeORM?
Database migration in TypeORM allows managing and version-controlling changes to the database schema. They are useful in production environments where we need to keep track of database changes over time and apply and revert changes in a controlled manner.

## How do migrations differ from seeding?
Migration is all about schema changes (creating , altering, or dropping tables and columns), whereas seeding is the process of populating the database with initial or test data.

## Why is it important to version-control database schema changes?
It is important to version-control database schema changes so that the changes to schema can be tracked , reviewed, audited, and rolled back if necessary. Also it can be used to maintain consistency between different environments (dev, test, prod)

## How can you roll back a migration if an issue occurs?
We can roll back a migration if an issue occurs by simply using the typeorm command : `typeorm migration:revert`. It will revert the last applied migration, undoing the changes made to the database schema.