import pandas as pd
dataset=pd.read_csv("ecommerce_transaction_dataset.csv")
dataset.head()

import pandas as pd
dataset=pd.read_csv("ecommerce_transaction_dataset.csv")
dataset=dataset[["InvoiceNo","StockCode"]]
dataset=dataset.dropna()
dataset.head()

import pandas as pd
dataset=pd.read_csv("ecommerce_transaction_dataset.csv")
dataset=dataset[["InvoiceNo","StockCode"]]
dataset=dataset.dropna()
transaction_data=dataset.groupby("InvoiceNo")["StockCode"].apply(list).reset_index(name='Items')
transaction_data.head()

import pandas as pd
dataset=pd.read_csv("ecommerce_transaction_dataset.csv")
dataset=dataset[["InvoiceNo","StockCode"]]
dataset=dataset.dropna()
transaction_data=dataset.groupby("InvoiceNo")["StockCode"].apply(list).reset_index(name='Items')
transactions=transaction_data["Items"].tolist()

#Implement the apriori algorithm on the processes data
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd
import pandas as pd
dataset=pd.read_csv("ecommerce_transaction_dataset.csv")
dataset=dataset[["InvoiceNo","StockCode"]]
dataset=dataset.dropna()
transaction_data=dataset.groupby("InvoiceNo")["StockCode"].apply(list).reset_index(name='Items')
transactions=transaction_data["Items"].tolist()
transaction_encoder = TransactionEncoder()
transaction_array =transaction_encoder.fit(transactions).transform(transactions)
transaction_dataframe = pd.DataFrame(transaction_array,
columns=transaction_encoder.columns_)
freuent_itemsets=apriori(transaction_dataframe,min_support=0.02,
use_colnames=True)
print("The frequent itemsets are:")
print(freuent_itemsets)


#You can also calculate the association rules using the association_rules() function as shown below
from mlxtend.preprocessing import TransactionEncoder 
from mlxtend.frequent_patterns import apriori,association_rules
import pandas as pd 
import pandas as pd
dataset=pd.read_csv("ecommerce_transaction_dataset.csv") 
dataset=dataset[["InvoiceNo","StockCode"]]
dataset=dataset.dropna()
transaction_data=dataset.groupby("InvoiceNo")["StockCode"].apply(list).reset_index(name='Items')

transactions=transaction_data["Items"].tolist()
transaction_encoder = TransactionEncoder()
transaction_array = transaction_encoder.fit(transactions).transform(transactions)
transaction_dataframe = pd.DataFrame(transaction_array, columns=transaction_encoder.columns_) 
freuent_itemsets=apriori(transaction_dataframe,min_support=0.02, use_colnames=True) 
association_rules_df=association_rules(freuent_itemsets, metric="confidence", min_threshold=.50) 
print("The association rules are:") 
print(association_rules_df.head()) 