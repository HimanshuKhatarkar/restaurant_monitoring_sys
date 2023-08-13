Restaurant Monitoring System
----------------------------
The Restaurant Monitoring System is a backend API that helps restaurant owners track the online and offline status of their stores during business hours. The system polls each store roughly every hour and records whether the store was active or not in a CSV file. The system also has data on the business hours of all the stores and the timezone for each store.

#The system provides two APIs:

    /trigger_report endpoint that triggers the generation of a report from the data provided (stored in the database). The API has no input and returns a report ID     (a random string). The report ID is used to poll the status of report completion.

    /get_report endpoint that returns the status of the report or the CSV. The API takes a report ID as input and returns the following:

If report generation is not complete, return "Running" as the output

If report generation is complete, return "Complete" along with the CSV file with the following schema: store_id, uptime_last_hour(in minutes), uptime_last_day(in hours), update_last_week(in hours), downtime_last_hour(in minutes), downtime_last_day(in hours), downtime_last_week(in hours) The uptime and downtime reported in the CSV only include observations within business hours. The system extrapolates uptime and downtime based on the periodic polls we have ingested to the entire time interval.

#Data Sources
The system has the following three sources of data:

A CSV file with three columns (store_id, timestamp_utc, status) where status is active or inactive. All timestamps are in UTC.

A CSV file with data on the business hours of all the stores. The schema of this data is store_id, dayOfWeek(0=Monday, 6=Sunday), start_time_local, end_time_local. These times are in the local time zone. If data is missing for a store, assume it is open 24*7.

A CSV file with data on the timezone for each store. The schema is store_id, timezone_str. If data is missing for a store, assume it is America/Chicago. This is used so that data sources 1 and 2 can be compared against each other.



#System Requirements
---------------------
The data sources are not static, and the system should not precompute the answers. The system should keep updating the data every hour.
The system should store the CSVs into a relevant database and make API calls to get the data.

Usage
To start the server, run the following command in the project directory:

    python src\app.py

The server will start running on http://localhost:5000

Also to Precompute the data, run the following command in the project directory:

    python src\precomp\precompute.py

API Documentation
/trigger_report
This endpoint triggers the generation of a report_id from the data provided (stored in the database).

Request
POST /trigger_report

Response
    HTTP/1.1 200 OK
    Content-Type: application/json
Note: If yopu are using Postman to test the API please select Key and Value piar as Content-Type: application/json

{
    "report_id": "random_string"
}

/get_report
This endpoint returns the status of the report or the CSV.

Request
GET get_report?report_id=random_string

Response
    HTTP/1.1 200 OK
    Content-Type: text/csv

    store_id, uptime_last_hour(in minutes), uptime_last_day(in hours), update_last_week(in hours), downtime_last_hour(in minutes), downtime_last_day(in hours),         downtime_last_week(in hours)
    1, 60, 



Also Provided an option to download the csv file in the results directory in csv format Which will be used in future calculations

Functionalities
Used advance python features like -

Multithreading
Caching


-> Backend server takes care of

       - User DATA management
       - Data storage
       - CSV -> Database
       - Data manipulation(CRUD)
       - logic for computing the hours overlap and uptime/downtime
       - psql dealing  with Time typecasting
       - Data preprocessing
       - File download

-> Flask API is used to manage users, files and data manipulation.

