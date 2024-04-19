# infra - objective
Spin up and connect to a t1.micro instance on AWS (this is eligible for the AWS free tier for a year).
Create a gen.py file that generates a 1gb file with the fields 'id', 'integer1', 'string1', 'string2'. 
'id' should be auto-incrementing, 'integer1' should be randomly assigned as numbers 1-10 and 'string1' and 'string2' should be random characters of length 1-32. the output file should have a header row using the comma as a delimiter and be called "source.csv"

## infra - result
1. Spin up and connect to a t1.micro instance on AWS (this is eligible for the AWS free tier – for 1 year)

```
    -> bucket name - gen-s3-bucket
    -> region - EU (London) eu-west-2
    -> ARN - arn:aws:s3:::gen-s3-bucket
```

2. How many rows did you generate? why?

```
    -> Total number of rows generated : 23031037
    
    -> The total number of rows generated were limited to the defined filesize, as in, the function created the above rows based on the filesize criteria, once the file size reached 1GB it stopped and outputted the file.
```

3. What is the content of the last row? How can you easily find this?

```    
    -> last_row = df.iloc[-1] # Refer gen.py to find function

    COLUMNS                         ROWS
    id                              23031037
    integer1                               7
    string1          wAEdrLZGSzDEbppsYvORDSJ
    string2     hOpUuSgybzkfGPfGgsKYAGQsrVWF
```

4. What is the distribution of 'integer1'? Which is most common?

```
    -> Most occured Integer : 9
    
    COLUMN
    integer1
    9     2305058
    10    2304182
    6     2304046
    3     2303425
    5     2303362
    4     2303083
    8     2302698
    7     2302288
    1     2301803
    2     2301092
```

5. Which row has the most vowels (considering Columns String1 and String2)?

```
    -> Row number : 4831100

    COLUMNS                              ROWS
    id                                   4831100
    integer1                                   8
    string1            ikSlDVrKRsuuvkHVThicuoeOJ
    string2     GcvHBReXPYDoIeaZUcuGViCgouPkOaui
    v_count                                   18
```

6. How large is a compressed (gzip) version of this file?

```    
    -> Compressed File Size : 672754.35
```

7.  How long did the compression process take?

```    
    -> gen_file_gzip_compression : ran in 109.85 seconds
```

# sql - objective
Organisationx serves impressions, which are ads shown to users. In addition, Organisationx captures site visitor data points when users fire a pixel from the particular website. A conversion occurs when a user is served an impression and then continues to take a consumer action which is considered as an event (a form submission, purchase, etc). Organisationx stores this log level information (impressions, events, conversions) in a database for analysis.

Three tables available with log level data (schemas shown below):

Impressions: a row is written to this table each time a user is served an ad.
Conversions: a row is written every time a user who was served an impression has an attributed conversion (you can assume that a user can only purchase one time)
Events: a row is written to the table each time a user has an onsite activity. 

*Note: the events table is not tied to media, this is purely on-site browsing activity.

NOTE : I've used BigQuery SQL to solve the below tests

## sql - result
1. Please write a SQL query to solve the following questions:

How many users were served an impression per day during September?

```
SELECT DATE(timestamp) AS date, COUNT(DISTINCT(user_id)) AS impression_count 
FROM impressions
WHERE timestamp >= '2023-09-01 00:00:00' AND timestamp < '2023-10-01 00:00:00'
GROUP BY DATE(timestamp);
```

The query extracts date from the timestamp using date() function and groups the results by date, It then counts the distict number of user IDs as impression_count to determine the number of users served as impression each day during september.

How many users were served an impression and fired pixel ID 101293 in September?

```
SELECT COUNT(DISTINCT impressions.user_id) AS impression_count
FROM impressions
INNER JOIN events
ON impressions.user_id = events.user_id
WHERE impressions.timestamp >= '2023-09-01 00:00:00' AND impressions.timestamp < '2023-09-01 00:00:00' AND events.pixel_id = 101293;
```

This query performs an inner join between the 'impressions' and 'events' tables based on 'user_id' column. It filters the data to include only records with a timestamp in September and where the 'pixel_id' in the 'events' table matches the value 101293. Finally, it counts the distinct number of 'user_id's from the 'impressions' table that meets these conditions, giving the desired count of users served an impression and fired 'pixel_id' 101293 in September.

How many attributed converters fired pixel ID 101293 and how many attributed conversions did not fire pixel ID 101293 before conversion (please write this in one query)?

```
SELECT COUNT(DISTINCT events.user_id) AS attributed_converters_fired_pixel, COUNT(DISTINCT conversions.user_id) AS attributed_conversiona_no_pixel 
FROM events
JOIN conversions
ON events.user_id = conversions.user_id
LEFT JOIN impressions
ON conversions.user_id = impressions.user_id
AND impressions.timestamp < conversions.conversion_timestamp
WHERE events.pixel_id = 101293
AND impressions.user_id IS NULL;
```

The query uses a LEFT JOIN to connect the 'impressions' table with the 'conversions' table based on the 'user_id', ensuring that we consider only conversions that occured after any related impressions. Then, it filters for the 'pixel_id' 101293 in the 'events' table to count attrributed converters that fired the pixel. Finally, it includes a condition in the WHERE clause to select only those conversions that didn't have any matching impression i.e, attributed conversions that did not fire pixel ID 101293 before conversion.

2. Using the log tables and knowing that we have this data available:

Write SQL that would output a frequency distribution for all converters before conversion. 

```
SELECT conversions.pixel_id, COUNT(*) AS frequency
FROM conversions
LEFT JOIN impressions
ON conversions.user_id = impressions.user_id
AND impressions.timestamp < conversions.conversion_timestamp
WHERE impressions.user_id IS NULL
GROUP BY conversions.pixel_id;
```

The query retrieves the 'pixel_id' column from the 'conversions' table and performs a LEFT JOIN with the 'impressions' table. It matches the 'user_id' columns and checks if the impression timestamp is before the conversion timestamp. The condition 'impressions.user_id IS NULL' filters for converters that did not have any matching impresion before conversion. Finally, the query uses the GROUP BY clause to group the conversions by 'pixel_id', and the COUNT(*) function calculated the frequency of each 'pixel_id' giving the frequenct distribution, including the number of converters associated with each 'pixel_id' before conversion.

Please write out how you would determine what the optimal frequency is and if there is a point that we should cap the frequency [You can create your own sample output to demonstrate]
*frequency = the number of impressions served to a user

- Determine what the optimal frequency is and if there is a point that we should cap the frequency?

To determine the optimal frequency and identify a point at which we should cap the frequency, we can analyse the distribution of impressions served to users. Here's a simple example:

```
SELECT user_id, COUNT(*) AS frequency
FROM impressions
GROUP BY user_id;
```

The above calculates the frequency of impressions for each user by grouping the data by the 'user_id' column.

We can examine statistical measures such as mean, median, mode and standard deviation to understand the central tendency and spread of the distribution. Additionally, we can plot a histogram or box plot to visualiase the frequency distribution graphically.

- Determine the optimal frequency

The optimal frequency will depend on various factors such as the specific campaign goals, target audience, and advertising strategy for example, wheather the campaign aims for high exposure or more controlled impressions or evaluate the potential impact on user experience and ad fatigue or monitor performance such as CTR and conversion rates at different frequency levels and also take associated costs into consideration. example we may learn that a moderate frequency range of 3-5 impressions per user yields better performance compared to lower or higher frequency levels.

If however, at any given point the frequency becomes excessive and negatively impacts campaign performance or user experience, we should consider capping the frequency and set a limit on the number of impressions served per user.

Table Schemas:

IMPRESSIONS	 	 
column_name	column_description	example_field
user_id	unique user ID 	ABC
auction_id	auction ID that uniquely identifies an impression	293842029
advertiser_id	unique ID associated with client name	12345
advertiser_name	client name	Client A
total_spend_cpm	total spend on individual impression in CPM format (CPM = spend * 1,000)	5.92
country	country where impression is served	United States
DMA	DMA where impression is served	New York
device	device of impression served 	Desktop/Laptop
timestamp	timestamp of the impression	9/10/18 9:08
		
EVENTS	 	 
column_name	column_description	example_field
user_id	unique user ID 	ABC
pixel_id	unique ID for event pixel	283928
pixel_name	event pixel name	Homepage
revenue	revenue associate with pixel (only populated if merit pixel)	100
country	country where pixel is fired	United States
DMA	DMA where pixel is fired	New York
device	device of pixel fire	Desktop/Laptop
timestamp	timestamp of pixel fire	9/1/18 0:11
		
CONVERSIONS	 	 
column_name	column_description	example_field
user_id	unique user ID 	ABC
pixel_id	unique ID for conversionn pixel	283928
pixel_name	merit pixel name	Purchase
imp_auction_id	impression auction ID for attributed impression	293842029
conversion_timestamp	timestamp for conversion	9/15/18 10:09
impression_timestamp	timestamp for attributed impression	9/10/18 9:08

## gen.py
This script imports modules :

```
random
string
time
pandas
numpy
os
``` 
Creates `data` and `compressed_data` variables as resources.

Has `6` classes:

```
Decorators -> custom-python-decorator to measure processing time of classes/functions.

class Decorators:
    def run_timer(func):

FileGenerator -> create a randomised criteria bound dataset.

class FileGenerator:
    def gen_random_string(length):
    def gen_file():

GenUtils -> converts dataset into a pandas dataframe.

class GenUtils:
    def gen_file():
    def gen_csv_file(data):


GenFileAnalysis -> functions that analysis the data such as counting rows, analysising number of vowels, distribution data and more are present here.

class GenFileAnalysis:
    def gen_file_row_count():
    def gen_file_last_row_contents():
    def gen_file_distribution_of_integers():
    def gen_file_vowel_analyser():


GenFileCompression -> compresses file into gzip format.

class GenFileCompression:
    def gen_file_gzip_compression():

GenFileSizeAnalysis -> checkes the size of compressed file. 

class GenFileSizeAnalysis:
    def gen_file_size_checker():

```

Finally, calls to generate csv_files, dataframes and compressed files are present :

```
generate_csv_file = GenUtils.gen_file
generate_pandas_dataframe_from_csv_file = GenUtils.gen_csv_file
generate_gzip_compressed_file = GenFileCompression.gen_file_gzip_compression
```

calls to analyse contents of data files:

```
get_df_row_count = GenFileAnalysis.gen_file_row_count
get_df_last_row_contents = GenFileAnalysis.gen_file_last_row_contents
get_distribution_of_integers = GenFileAnalysis.gen_file_distribution_of_integers
get_row_with_most_vowels = GenFileAnalysis.gen_file_vowel_analyser
get_gzip_compressed_file_size = GenFileSizeAnalysis.gen_file_size_checker
```

## split.py
This script imports modules:

```
pandas
time
os
gzip
math
```

Has `2` classes :

```
Decorators -> custom-python-decorator to measure processing time of classes/functions.

class Decorators:
    def run_timer(func):

GenFileSplit -> splits compressed_file into 10 parts, gzips it.

class GenFileSplit:
    def gen_file_split():
```

## transfer_to_s3.py
This script uploads files on to an S3 bucket

Imports modules :

```
pandas
gen
split
boto3
time
```

Creates resource variables such as :
...
dummy key
```
access_key_id = key_id
secret_access_key = key_id
s3 = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
```

Has `3` classes:

```
Decorators -> custom-python-decorator to measure processing time of classes/functions.

class Decorators:
    def run_timer(func):

GenFileUpload -> takes compressed gzip parts and uploaded to AWS S3 bucket

class GenFileUpload():
    def gen_file_to_s3():

GenFileS3Download -> Creates a donwloadable link from a file on S3
class GenFileS3Download:
    def gen_file_s3_download_link():
```
