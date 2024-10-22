#PROBLEM STATEMENT-2 
import pandas as pd

#1 Create the dictionary
data = {'English': {'Sam': 60, 'Jackson': 74, 'Ahree': 85},
    'History': {'Gloria': 83, 'Sam': 65, 'Isla': 78, 'Aron': 72, 'Gray': 61},
    'Geography':{'Jackson':92,'Gloria':95,'Isla':82,'Aron':75,'Ahree':76}, 
    'Mathematics':{'Sam':99,'Gloria':74,'Jackson':89,'Ahree':85,'Gray':95}, 
    'Science':{'Sam':89,'Aron':82,'Gray':78,'Isla':93,'Ahree':87} }
# Convert the dictionary to a pandas Series
series = pd.Series(data)
print(series)

#2 convert the dictionary into a DataFrame
df = pd.DataFrame(data)

#replace all the null values with zeros
df.fillna(0, inplace = True)
print(df)

#3 transpose the DataFrame
df_transposed = df.T

#create a new column 'average' and calculate the average of all subjects
df_transposed['average'] = df_transposed.mean(axis=1)
print(df_transposed)

