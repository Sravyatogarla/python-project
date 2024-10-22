#PROBLEM STATEMENT-4
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

#import the cerials.csv dataset
df=pd.read_csv("cereal.csv")
df

#2 plot ratings of different types of manufacturers.
data=df.groupby("mfr",as_index=False).sum()
data 

#3 xticks range form 0-100

plt.barh(data["mfr"], data["rating"], color='skyblue')

plt.xticks(np.arange(0,100,1000
                    
#4 change the style of the graph to seaborn

sns.set_style("whitegrid")

plt.show()
