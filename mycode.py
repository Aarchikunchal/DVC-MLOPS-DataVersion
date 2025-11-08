import pandas as pd
import os
# Create  a dataframe 
data = {'Name':['Aarchi','Alice','Bob'],
        'Age':[21,30,35],
        'City':['New York','Los Angeles','Chicago']}
df = pd.DataFrame(data)


# ensure the "data" directory exist at the root level
data_dir="data"
os.makedirs(data_dir , exist_ok=True)

# Define file path
file_path= os.path.join(data_dir ,'sample_data.csv')

# save the dataframe to a csv file , including columns name
df.to_csv(file_path,index=False)
print(f"CSV file saved to {file_path}")

