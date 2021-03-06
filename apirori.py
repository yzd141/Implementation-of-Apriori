
import pandas as pd
import numpy as np

F = open('/groceries.csv','r')
Lines = F.readlines()  
df=[[]]

count = 0

for line in Lines: 
   df.append(line.strip())

df=df[1:]

data=[]

for i in range(9000):
  data.append(df[i].split(','))

data=np.array(data)

data.shape

from mlxtend.preprocessing import TransactionEncoder

te = TransactionEncoder()
te_ary = te.fit(data).transform(data)
df = pd.DataFrame(te_ary, columns=te.columns_)
df

from mlxtend.frequent_patterns import apriori
frequent_itemsets = apriori(df, min_support=0.001, use_colnames=True)

print(frequent_itemsets)

frequent_itemsets = apriori(df, min_support=0.001, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
frequent_itemsets

frequent_itemsets[ (frequent_itemsets['length'] == 3) &
                   (frequent_itemsets['support'] >= 0.01) ]

frequent_itemsets[ (frequent_itemsets['length'] == 2) &
                   (frequent_itemsets['support'] >= 0.03) ]

for item in frequent_itemsets['itemsets']:
  if ('yogurt' in item) & (len(item)==3):
    print(item)
