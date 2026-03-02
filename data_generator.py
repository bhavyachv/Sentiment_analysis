import pandas as pd
import random

products=['Phone','Laptop','Headphones','Watch','Camera']
pos_adj= ['amazing','great','fantastic','superb','excellent','perfect']
neg_adj=['terrible','awful','worst','bad','garbage','useless']

data=[]

for i in range (1000):
    prod=random.choice(products)
    adj=random.choice(pos_adj)
    review=f"This {prod} is {adj}!"
    data.append([review,"Positive"])

for i in range(1000):
    prod = random.choice(products)
    adj = random.choice(neg_adj)
    review = f"This {prod} is {adj}!"
    data.append([review, "Negative"])

df=pd.DataFrame(data,columns=['Review','Sentiment'])
df=df.sample(frac=1,random_state=42).reset_index(drop=True)

df.to_csv('reviews.csv',index=False)
print("✅ Generated reviews.csv with 2000 reviews!")