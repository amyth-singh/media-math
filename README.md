# Objective
Spin up and connect to a t1.micro instance on AWS (this is eligible for the AWS free tier for a year).
Create a gen.py file that generates a 1gb file with the fields 'id', 'integer1', 'string1', 'string2'. 
'id' should be auto-incrementing, 'integer1' should be randomly assigned as numbers 1-10 and 'string1' and 'string2' should be random characters of length 1-32. the output file should have a header row using the comma as a delimiter and be called "source.csv"

## Output

1. Spin up and connect to a t1.micro instance on AWS (this is eligible for the AWS free tier – for 1 year)

```
    -> bucket name - gen-s3-bucket
    -> region - EU (London) eu-west-2
    -> ARN - arn:aws:s3:::gen-s3-bucket
```

2. Install Python 3 (and any other packages you may prefer) and create a script (gen.py) that can generate a 1GB file

```
    -> # Refer gen.py file
```

3. How many rows did you generate? why?

```
    -> Total number of rows generated : 23031037
    
    -> The total number of rows generated were limited to the defined filesize, as in, the function created the above rows based on the filesize criteria, once the file size reached 1GB it stopped and outputted the file.
```

4. What is the content of the last row? How can you easily find this?

```    
    -> last_row = df.iloc[-1] # Refer gen.py to find function

    COLUMNS                         ROWS
    id                              23031037
    integer1                               7
    string1          wAEdrLZGSzDEbppsYvORDSJ
    string2     hOpUuSgybzkfGPfGgsKYAGQsrVWF
```

5. What is the distribution of 'integer1'? Which is most common?

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

6. Which row has the most vowels (considering Columns String1 and String2)?

```
    -> Row number : 4831100

    COLUMNS                              ROWS
    id                                   4831100
    integer1                                   8
    string1            ikSlDVrKRsuuvkHVThicuoeOJ
    string2     GcvHBReXPYDoIeaZUcuGViCgouPkOaui
    v_count                                   18
```

7. How large is a compressed (gzip) version of this file?

```    
    -> Compressed File Size : 672754.35
```

8.  How long did the compression process take?

```    
    -> gen_file_gzip_compression : ran in 109.85 seconds
```

# SQL
Refer the 'SQL_ASSESSMENT_TASK.md' file for all answers

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
