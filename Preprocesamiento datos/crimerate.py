#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from numpy import NaN
from pandas.core.frame import DataFrame


# In[6]:


crimeMX= pd.read_csv('crimemexico.csv',sep='\t', on_bad_lines='skip')


# In[29]:


print("Dimensiones \n", crimeMX.shape)


# In[9]:


print("Numero de datos \n", crimeMX.size)


# In[10]:


print("Nombre de columnas \n", crimeMX.columns)


# In[11]:


print("Nombre de filas \n", crimeMX.index)


# In[12]:


print("Tipo de datos de las columnas \n", crimeMX.dtypes)


# In[60]:


#elimacion de valores faltanes
crimeMX = crimeMX.dropna(axis=0,how='any')


# In[95]:


#creacion del dataframe con los datos que nos interesan
columnas = ['Estado', 'Municipio','Tipo de delito','Modalidad']
newCrimeMX = pd.DataFrame(columns=columnas)


# In[96]:


newCrimeMX['Estado']=crimeMX['State']
newCrimeMX['Municipio']=crimeMX['City']
newCrimeMX['Tipo de delito']=crimeMX['Tipo de delito']
newCrimeMX['Modalidad']=crimeMX['Modalidad']


# In[98]:


newCrimeMX = newCrimeMX.loc[newCrimeMX['Estado'] == 'Colima']


# In[104]:


print(newCrimeMX)


# In[103]:


newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Abuso de confianza') == False]
newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Extorsion') == False]
newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Fraude') == False]
newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Incesto') == False]
newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Incumplimiento de obligaciones de asistencia familiar') == False]
newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Otros delitos contra la familia') == False]
newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Otros delitos que atentan contra la libertad personal') == False]
newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Tráfico de menores') == False]
newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Trata de personas') == False]
newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Violencia de género en todas sus modalidades distinta a la violencia familiar') == False]
newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Aborto') == False]
newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Falsificación') == False]
newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Falsedad') == False]
newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Contra el medio ambiente') == False]
newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Otros delitos del Fuero Común') == False]
newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Delitos cometidos por servidores públicos') == False]
newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Evasión de presos') == False]
newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Narcomenudeo') == False]
newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Otros delitos contra la sociedad') == False]
newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Electorales') == False]
newCrimeMX = newCrimeMX[newCrimeMX['Tipo de delito'].str.contains('Corrupción de menores') == False]


# In[92]:


newCrimeMX = newCrimeMX.dropna(subset=['Estado'])


# In[105]:


newCrimeMX.to_csv('newCrimeMX.csv')


# In[ ]:




