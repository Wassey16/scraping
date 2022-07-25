# scraping
### Commands to get data from a local csv file into a mongodb collection in a dockert container 
```bash
docker cp file-path  docker-container-hash:/tmp
docker exec -it docker-container-hash bash 
cd tmp 
mongoimport --db DB_Name --collection Collection_Name --type csv --headerline --file Name-of-file-to-import
```
* docker-cp to copy the file in /tmp location of the container
* then in container get in `/tmp` because file is located there 
* DB_Name: represents the name of the database that contains the collection Collection_Name.
* type: specifies the file type CSV (Optional field).
* headerline: details the mongoimport command to take the 1st record of CSV file(s) as field names.
* Name-of-file-to-import: represents the name and path of the CSV file to be imported/restored
