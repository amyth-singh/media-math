# Business Intelligence - Data Engineer Interview Task
Refer the 'BUSINESS_INTELLIGENCE_TASK.md' file for all answers

# SQL Assessment - Task
Refer the 'SQL_ASSESSMENT_TASK.md' file for all answers

# gen.py
This script imports modules :

```
random
string
time
pandas
numpy
os
``` 
Creates `data` and `compressed_data` variables as resources, and contains a total of `6` classes:

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