# Business Intelligence - Data Engineer Task
1. Spin up and connect to a t1.micro instance on AWS (this is eligible for the AWS free tier – for 1 year)

```
    -> bucket name - mediamath-s3-bucket
    -> region - EU (London) eu-west-2
    -> ARN - arn:aws:s3:::mediamath-s3-bucket
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

## split.py
This script splits the compressed 'source.csv.gz' file into 10 equal parts by creating a directory to store files, calculates the no. of rows per split file, converts them into dataFrames, creates filenames and writes the data to destination ('source_split_files' folder)

9. How long does the process take?

```    
    -> gen_file_split : ran in 120.06 seconds
```

## transfer_to_s3.py
This script connects to the 'mediamath-s3-bucket', takes all the files from 'source_split_files' and uploads it in a loop whilst naming the files.

10. Please provide a link  to download one of the 10 files ex: part-3.csv.gz' 

```
-> 'https://mediamath-s3-bucket.s3.amazonaws.com/part-3.csv.gz?AWSAccessKeyId=AKIASVUN4TFQRNO4CFAO&Signature=XmHTeYgDARRMJZD8kVhiM2gNZhk%3D&Expires=1685058707'
```

`Note - Ensure that you are using the generated URL as a direct download link and not trying to access it through a web browser. The generated URL should be used in a programmatic way or with a download manager tool, rather than directly in a browser.`

## bonus
11. What approach would you take if you needed to split 32TB of data?

-> There are several approaches we can consider to accomplish this.

a. parallel processing - to speed up the splitting process, we can leverage parallel processing techniques. Python provides libraries such as 'multiprocessing' and 'concurrent.futures'.

b. leverage streaming - Instead of loading the entire dataset file into memory, we can use the streaming approach where data is processes in small chunks or streams, reading and writing the data in a sequential manner without loading the entire dataset into memory, this won't overwhelm the system's resources

c. distributed computing - if the data splitting task is large and requires processing on multiple machines, we can use Apache Spark, PySpark or Spark Streaming or even Dask, these frameworks allow us to split, transform and anlyse large datasets across clusters if needed.

d. optimise file formatting - consider using optimised file formats that are designed for large-scale processing like Parquet, Arrow etc. they can even reduce storage space and speed up processing.

e. cloud solutions - utilising cloud-based services like AWS S3, Google Cloud Storage, AWS Glue, Google Dataflow etc.. offer scalable storage and processing capabilities, allowing efficient large data handling and splitting.

f. optimise infrastructure - 32TB would require robust hardware infrastructure, ensuring that we have enough storage system capacity and performance alongside workload handling capabilities will help, using speed-storage-solutions like SSDs, or distributed file systems to help I/O performance.

regardless of any optimisation, 32TB files will take time and its important to plan before execution and also test different approaches.