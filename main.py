import pandas as pd
import numpy as np
import seaborn as sns
from IPython.display import display
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
emotionRange = [ 'depressed','alert' ,'mild_pain' ,'extreme_pain' ,'severe_pain' ]
df = pd.read_csv('horse.csv')
groups = df.groupby('outcome')['rectal_temp'].mean()
print(groups)
df['pain'].replace(emotionRange,[1,2,3,4,5],inplace=True)
df['surgery'].replace(['no','yes'],[0,1],inplace=True)
df['age'].replace(['adult','young'],[0,1],inplace=True)
df['temp_of_extremities'].replace(['cold','cool','normal','warm'],[0,1,2,3],inplace=True)
df['peripheral_pulse'].replace(['absent','reduced','normal','increased'],[0,1,2,3],inplace=True)
df['mucous_membrane'].replace(['pale_cyanotic','pale_pink','normal_pink','bright_pink','bright_red','dark_cyanotic'],[0,1,2,3,4,5],inplace=True)
df['capillary_refill_time'].replace(['less_3_sec','3','more_3_sec'],[0,1,2],inplace=True)
df['peristalsis'].replace(['absent','hypomotile','normal','hypermotile'],[0,1,2,3],inplace=True)
df['abdominal_distention'].replace(['none','slight','moderate','severe'],[0,1,2,3],inplace=True)
df['nasogastric_tube'].replace(['none','slight','significant'],[0,1,2],inplace=True)
df['nasogastric_reflux'].replace(['none','less_1_liter','more_1_liter'],[0,1,2],inplace=True)
df['rectal_exam_feces'].replace(['absent','decreased','normal','increased'],[0,1,2,3],inplace=True)
df['abdomen'].replace(['other','distend_small','normal','distend_large','firm'],[0,1,2,3,4],inplace=True)
df['abdomo_appearance'].replace(['clear','cloudy','serosanguious'],[0,1,2],inplace=True)
# df['outcome'].replace(['died','euthanized','lived'],[0,1,2],inplace=True)

print(df.dtypes)

df['rectal_temp'].replace(np.nan,df['rectal_temp'].mean(),inplace=True)
df['pulse'].replace(np.nan,df['pulse'].mean(),inplace=True)
df['respiratory_rate'].replace(np.nan,df['respiratory_rate'].mean(),inplace=True)
df['temp_of_extremities'].replace(np.nan,df['temp_of_extremities'].mean(),inplace=True)
df['peripheral_pulse'].replace(np.nan,df['peripheral_pulse'].mean(),inplace=True)
df['mucous_membrane'].replace(np.nan,df['mucous_membrane'].mean(),inplace=True)
df['capillary_refill_time'].replace(np.nan,df['capillary_refill_time'].mean(),inplace=True)
df['pain'].replace(np.nan,df['pain'].median(),inplace=True)
df['peristalsis'].replace(np.nan,df['peristalsis'].mean(),inplace=True)
df['nasogastric_tube'].replace(np.nan,df['nasogastric_tube'].median(),inplace=True)
df['nasogastric_reflux'].replace(np.nan,df['nasogastric_reflux'].median(),inplace=True)
df['nasogastric_reflux_ph'].replace(np.nan,df['nasogastric_reflux_ph'].mean(),inplace=True)
df['rectal_exam_feces'].replace(np.nan,df['rectal_exam_feces'].median(),inplace=True)
df['abdomen'].replace(np.nan,df['abdomen'].median(),inplace=True)
df['packed_cell_volume'].replace(np.nan,df['packed_cell_volume'].mean(),inplace=True)
df['total_protein'].replace(np.nan,df['total_protein'].mean(),inplace=True)
df['abdomo_appearance'].replace(np.nan,df['abdomo_appearance'].median(),inplace=True)
df['abdomo_protein'].replace(np.nan,df['abdomo_protein'].mean(),inplace=True)
df['abdominal_distention'].replace(np.nan,df['abdominal_distention'].median(),inplace=True)
#
# X= df[['rectal_temp','pulse','respiratory_rate','temp_of_extremities','peripheral_pulse','mucous_membrane','capillary_refill_time',
#        'pain','peristalsis','nasogastric_tube','nasogastric_tube','nasogastric_reflux','nasogastric_reflux_ph','rectal_exam_feces',
#        'abdomen','packed_cell_volume','total_protein','abdomo_appearance','abdomo_protein','abdominal_distention']]
# Y=df['outcome']
#
# X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=101)
# model = LogisticRegression(solver='liblinear')
#
# model.fit(X_train,Y_train)
#
# predictions = model.predict(X_test)
#
# print('Log Score : ',model.score(X_test,Y_test))
# model = tree.DecisionTreeClassifier()
# model.fit(X_train,Y_train)
#
# predictions = model.predict(X_test)
#
# print('Tree Score : ',model.score(X_test,Y_test))
# model = KNeighborsClassifier(n_neighbors=17)
# model.fit(X_train,Y_train)
#
# predictions = model.predict(X_test)
#
# print('KNN Score : ',model.score(X_test,Y_test))
# model = make_pipeline(StandardScaler(),SVC(gamma='auto'))
# model.fit(X_train,Y_train)
#
# predictions = model.predict(X_test)
#
# print('SVC Score : ',model.score(X_test,Y_test))
# model = GradientBoostingClassifier(n_estimators=50, learning_rate=0.06, max_depth=4, random_state=0)
# model.fit(X_train,Y_train)
#
#
#
# plt.show()
# print('Gradient Score : ',model.score(X_test,Y_test))
# # display(df)
# nan_count = df.isna().sum()
#
gk = df.groupby('outcome')['age'].sum()
dat = pd.DataFrame()
dat = pd.concat([dat,gk])
dat = dat.assign(total=[77,44,178])
dat = dat.assign(young = dat['total']-dat[0])
dat['young']=dat['young']/dat['young'].sum()
dat[0]=dat[0]/dat[0].sum()
print(dat)

sns.barplot(data=dat,x=dat.index,y='young')
plt.ylabel('outcome in adult')
plt.title('Outcome Vs. adult')
plt.savefig("Outcome V adult.png")
plt.show()
