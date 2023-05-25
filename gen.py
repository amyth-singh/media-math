#%%
import random
import string
import time
import pandas as pd
import numpy as np
import os

# Resources
data = 'source.csv'
compressed_data = 'source.csv.gz'

class Decorators:
    def __init__(self):
        pass

    def run_timer(func):
            def wrapper():
                t1 = time.time()
                func()
                t2 = time.time() - t1
                print(f"{func.__name__} : ran in {t2} seconds")
            return wrapper

class FileGenerator:
    def __init__(self):
        pass

    def gen_random_string(length):
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def gen_file():
        with open('source.csv', 'w') as file:
            file.write("id,integer1,string1,string2\n")
            target_size = 1024 * 1024 * 1024 # sets target fileseize (1GB)
            current_size = file.tell() # initialise file size
            id_counter = 1 

            while current_size < target_size:
                integer1 = random.randint(1,10) # auto-increment IDs
                string1 = FileGenerator.gen_random_string(random.randint(1, 32)) # random char of len(1 to 32)
                string2 = FileGenerator.gen_random_string(random.randint(1, 32)) # random char of len(1 to 32)
                row = f"{id_counter},{integer1},{string1},{string2}\n" # concat values to csv
                file.write(row) # write rows to csv
                current_size = file.tell() # updates file size
                id_counter += 1 # increment ID counter
            print("file generation complete!")

class GenUtils:
    def __init__(self):
        pass
    
    @Decorators.run_timer
    def gen_file():
        gen_file = FileGenerator.gen_file()
        return gen_file

    def gen_csv_file(data):
        with open(data, 'r') as file:
            df = pd.read_csv(file)
            return df

class GenFileAnalysis:
    def __init__(self):
        pass
    
    def gen_file_row_count():
        df = GenUtils.gen_csv_file(data)
        row_count = df.shape[0]
        return print(f"Total number of rows generated : {row_count}")
    
    def gen_file_last_row_contents():
        df = GenUtils.gen_csv_file(data)
        last_row = df.iloc[-1]
        return last_row
    
    def gen_file_distribution_of_integers():
        df = GenUtils.gen_csv_file(data)
        distribution = df['integer1'].value_counts()
        most_common_item = distribution.idxmax()
        print(f"Most occured Integer : {most_common_item}")
        return distribution

    def gen_file_vowel_analyser():
        df = GenUtils.gen_csv_file(data)
        def count_vowels(string):
            vowels = 'aeiou'
            return sum(char in vowels for char in string)
        df['v_count'] = df.apply(lambda row: sum(count_vowels(str(cell)) for cell in row), axis=1)
        max_vowel_row_index = df['v_count'].idxmax()
        max_vowel_row = df.loc[max_vowel_row_index]
        return max_vowel_row
    
class GenFileCompression:
    def __init__(self):
        pass
    
    @Decorators.run_timer
    def gen_file_gzip_compression():
        df = GenUtils.gen_csv_file(data)
        gzip_file = df.to_csv('source.csv.gz', compression='gzip', index=False)


class GenFileSizeAnalysis:
    def __init__(self):
        pass

    def gen_file_size_checker():
        comp_file_size = os.path.getsize(compressed_data)
        comp_file_size_in_mb = comp_file_size / 1024
        return print(f"Compressed File Size : {comp_file_size_in_mb}")

# Calls to generate data files
generate_csv_file = GenUtils.gen_file
generate_pandas_dataframe_from_csv_file = GenUtils.gen_csv_file
generate_gzip_compressed_file = GenFileCompression.gen_file_gzip_compression

# Calls to analyse contents of data file
get_df_row_count = GenFileAnalysis.gen_file_row_count
get_df_last_row_contents = GenFileAnalysis.gen_file_last_row_contents
get_distribution_of_integers = GenFileAnalysis.gen_file_distribution_of_integers
get_row_with_most_vowels = GenFileAnalysis.gen_file_vowel_analyser
get_gzip_compressed_file_size = GenFileSizeAnalysis.gen_file_size_checker

# Unhash to run
# generate_csv_file()
# generate_pandas_dataframe_from_csv_file()
# generate_gzip_compressed_file()
# get_df_row_count()
# get_df_last_row_contents()
# get_distribution_of_integers()
# get_row_with_most_vowels()
# get_gzip_compressed_file_size()