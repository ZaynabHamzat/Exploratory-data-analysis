# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


 
    #converting txt file into csv file
#X = pd.read_csv("drugs by age.txt", delimiter= ",")
#X.to_csv ("drug_use by age.csv")

#importing dataset
Y = pd.read_csv("drug_use by age.csv", sep=',', na_values = '-')

# data cleaning is performed. Fill Nan where there is '-'.
# Also some columns data types is string where they are supposed to be float


for col in Y.columns[2:]:
   Y[col] = pd.to_numeric(Y[col], errors = 'coerce')

Y.drop(columns = ['n'], inplace= True)
Y_copy = Y

#dropping rows 0 - 4 for all age groups between 12 - 16 years old
for i in range(5):
    Y = Y.drop(i)


#drug abuse against age
set_drug_use = Y[['age','alcohol-use','marijuana-use','cocaine-use','crack-use',
                  'heroin-use','hallucinogen-use','inhalant-use','pain-releiver-use',
                  'oxycontin-use','tranquilizer-use','stimulant-use','meth-use','sedative-use']]
set_drug_use.plot('age', kind='bar', figsize= (20, 11), stacked=True, legend=True)
plt.show


#frequeny of abuse
set_drug_freq = Y[['age','alcohol-frequency','marijuana-frequency','cocaine-frequency',
                   'crack-frequency','heroin-frequency','hallucinogen-frequency',
                   'inhalant-frequency','pain-releiver-frequency','oxycontin-frequency',
                   'tranquilizer-frequency','stimulant-frequency','meth-frequency','sedative-frequency']]
set_drug_freq.plot('age', kind= 'bar', figsize= (20, 11), stacked =True, legend = True)
plt.show


#correlation relationships between various drugs
plt.figure(figsize= (18, 18))
sb.heatmap(Y_copy.corr(),square = True, vmax=1, cmap="YlGnBu", annot=True)
plt.show


drug_use = Y_copy[['age','alcohol-use','marijuana-use','cocaine-use','crack-use',
                  'heroin-use','hallucinogen-use','inhalant-use','pain-releiver-use',
                  'oxycontin-use','tranquilizer-use','stimulant-use','meth-use','sedative-use']]


drug_freq = Y_copy[['age','alcohol-frequency','marijuana-frequency','cocaine-frequency',
                   'crack-frequency','heroin-frequency','hallucinogen-frequency',
                   'inhalant-frequency','pain-releiver-frequency','oxycontin-frequency',
                   'tranquilizer-frequency','stimulant-frequency','meth-frequency','sedative-frequency']]
x = 1
for n in range (len(Y_copy.columns)-14):
    fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=True, figsize=(20,8))
    Y_copy[drug_use.columns[x]].plot(x=Y['age'], y=drug_use.columns[x], kind='bar', ax=ax1, color='purple', title=drug_use.columns[x])
    Y_copy[drug_freq.columns[x]].plot(x=Y['age'], y=drug_freq.columns[x], kind='bar', ax=ax2, color='orange', title=drug_freq.columns[x])
    x+=1
plt.show