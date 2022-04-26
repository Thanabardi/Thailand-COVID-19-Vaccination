# Thailand-COVID-19-Vaccination
A mockup Thailand-COVID-19-Vaccination application, to search or update vaccination information classified by province.

## Data example   
vaccination by dose table   
| id |	province |	over_60_1st_dose |	total_1st_dose |	total_2nd_dose |	total_3rd_dose | date |
|----|-----------|-------------------|-----------------|-------------------|-------------------|------|
| 1	|Krabi       |	49646            |	373452         |	348632         |	91393          | 5/3/22 23:15:00 PM|
| 2	|Bangkok     |	1304946          |	9633649        |	8843614        |	4866624	       | 5/3/22 23:15:00 PM|
| 3	|Kanchanaburi|	79988            |	531823         |	498563         |	166139         | 5/3/22 23:15:00 PM|
| ...|...        |	...              |	...            |	...            |	...            | ...               |


vaccination by authorizations table
| id |	province |	total_doses |	AstraZeneca |	Pfizer  |	Sinovac |	Sinopharm |	Moderna |	Johnson_Johnson | date |
|----|-----------|--------------|---------------|-----------|-----------|-------------|---------|-------------------|------|
| 1	|Krabi       |	820698      |	349625      |	162652  |	245726  |	53053     |	9642    |	0               | 5/3/22 23:15:00 PM|
| 2	|Bangkok     |	23989865    |	12299551    |	4879353 |	2606270	|	2501415   |	1700153	|	2450            | 5/3/22 23:15:00 PM|
| 3	|Kanchanaburi|	1203171     |	362197      |	241846  |	255756  |	335557    |	7490    |	325             | 5/3/22 23:15:00 PM|
| ...|...        |	...         |	...         |	...     |	...     |	...       |	...     |	...             | ...               |


Data comes from [หมอพร้อม](https://dashboard-vaccine.moph.go.th/dashboard.html)    
Data transformed by [the-researcher-covid-data](https://github.com/porames/the-researcher-covid-data)    

## Documents
[Wiki Home](../../wiki/Home)    
[Package Diagram](../../wiki/Package-Diagram)    
[UML Class Diagram](../../wiki/UML-Class-Diagram)    

## Installing dependencies
    pip install -r requirement.txt

## Getting Started
    # Create vaccination_by_province database and load data from csv file
    python vaccination_by_province.py

    # Run application
    python gui.py
