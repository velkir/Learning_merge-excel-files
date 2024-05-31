import pandas as pd
import os

def create_dfs_list(directory):
  raw_files = os.listdir(directory)
  dfs = []
  for file in raw_files:
    if file.endswith(".xlsx"):
      dfs.append(pd.read_excel(os.path.join(directory, file)))
  print("Files added to DataFrame list!")
  return dfs

def concat_excel_files(dataframes_list, output_excel_name="output.xlsx"):
  merged_df = pd.concat(dataframes_list, ignore_index=True)
  merged_df.to_excel(output_excel_name, index=False)
  print("Files successfully merged into {} file".format(output_excel_name))

path="excel_files_merge"

dataframes = create_dfs_list(path)
concat_excel_files(dataframes)