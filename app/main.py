from pipeline.extract import raw_data_extract

path = "data/input"

df_list = raw_data_extract(path)

print(df_list)

