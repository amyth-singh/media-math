#%%
import pandas as pd
import time
import os
import gzip
import math

# Resources

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

class GenFileSplit:
    def _init__(self):
        pass
    
    @Decorators.run_timer
    def gen_file_split():
        compressed_file_path = 'source.csv.gz'
        output_dir = 'source_split_files'
        # creates directory to store files
        os.makedirs(output_dir, exist_ok=True)
        df = pd.read_csv(compressed_file_path)
        # calculate no. of rows per split
        total_rows = len(df)
        split_count = 9
        rows_per_file = math.ceil(total_rows / split_count)
        # split into multiple dfs
        split_data = [df[i:i+rows_per_file] for i in range(0, total_rows, rows_per_file)]
        for i, data in enumerate(split_data, start=1):
            # create file names
            split_file_name = f'part-{i}.csv.gz'
            split_file_path = os.path.join(output_dir, split_file_name)
            # write split data to file
            with gzip.open(split_file_path, 'wt', newline='') as split_file:
                data.to_csv(split_file, index=False)
        print("Splitting of the file is complete.")

file = GenFileSplit.gen_file_split
file()