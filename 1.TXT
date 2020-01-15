import pandas     as pd
import numpy      as np
import matplotlib.pyplot as plt
import statistics as sc
import scipy.stats as st
import seaborn as sns
df=pd.read_csv(r'C:\Users\ziadm\Ziad\cell2celltrain.csv') 
#print(df.isnull().sum())
df.replace(-np.inf, np.nan)
df=df.dropna()
#print(df)
#print(df.isnull().sum())
#print(df.iloc[:,0])
#x=df.iloc[:,1].count()
#y=df.CreditRating.value_counts(normalize=True)
#print(y)
#z=df.groupby(["Churn", "Occupation"]).size()
#print(z)
#c=pd.crosstab(df.Churn,df.CreditRating, normalize='index')
#print(c)
#a= df.groupby('Churn')['CreditRating'].value_counts() / df.groupby('Churn')['CreditRating'].count()
#b = a.reset_index(name='cpt')
#a.head()  # your conditional probability table
#z=plt.hist(df.AgeHH1,rwidth=0.9,bins=50)
#plt.show()
#d=sc.mean(df.DroppedCalls)
#g=sc.variance(df.DroppedCalls)
#e = df.DroppedCalls.plot.kde(ind=[1, 2, 3, 4, 5, 6,7,9])
#p=np.sort(df.DroppedCalls)
#q= list(dict.fromkeys(p))
#r=list(norm.cdf(q))
#n=len(q)-1
#plt.plot(q,r)
#plt.show()
#f = df.MonthlyMinutes.plot.density()
#s=df.iloc[:,11:13]
#s.plot.kde()
#Assuming enohom independent ( nes2al feeha )
#cov(X, Y) = (sum (x - mean(X)) * (y - mean(Y)) ) * 1/(n-1)
#corr = df.corr()
#sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values, annot = True, annot_kws={'size':12})
#heat_map=plt.gcf()
#heat_map.set_size_inches(20,15)
#plt.xticks(fontsize=10)
#plt.yticks(fontsize=10)
#plt.show()
#m=sns.boxplot(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values, annot = True, annot_kws={'size':12})





##############################################################################
##STEP 1
numbersOnly=df.select_dtypes(exclude=[np.object])
numbersOnlydf=numbersOnly.drop(columns=['CustomerID'])
corr = numbersOnlydf.corr()
cov=numbersOnlydf.cov()
############################################################################
#THE FITTING
numbersOnly=df.select_dtypes(exclude=[np.object])
numbersOnlydf=numbersOnly.drop(columns=['CustomerID'])
distributions=[st.beta,st.norm,st.expon, st.alpha,st.gamma,st.exponnorm]
d=["beta","norm","expon", "alpha","gamma","exponnorm"]
bestdistributions=[]
argsofbestdistributions=[]
for column in numbersOnlydf:
 Y1,X1=np.histogram(numbersOnlydf[column],bins=20,density=True)
 #plt.plot(X1[1:],Y1)
 error=[]
 s=column
 for distribution in distributions :
    tmp=distribution.fit(numbersOnlydf[column])
    arg = tmp[:-2]
    loc = tmp[-2]
    scale = tmp[-1]
    pdf = distribution.pdf(X1, loc=loc, scale=scale, *arg)
    diff=pdf[1:]-Y1
    msq=pow(diff,2).mean()
    error.append(msq)
 
 v=distributions[error.index(min(error))]
 tmp=v.fit(numbersOnlydf[column])
 argsofbestdistributions.append(tmp)
 print(d[error.index(min(error))] +" distribution "+s)
 bestdistributions.append(d[error.index(min(error))])
#############################################################################
###conditional probablity FITTING
ziad=df.loc[df.Churn=='Yes']
numbersOnly2=ziad.select_dtypes(exclude=[np.object])
numbersOnlydf2=numbersOnly2.drop(columns=['CustomerID'])
distributions=[st.beta,st.norm,st.expon, st.alpha,st.gamma,st.exponnorm]
d=["beta","norm","expon", "alpha","gamma","exponnorm"]
bestdistributionsYES=[]
argsofbestdistributionsYES=[]
for column in numbersOnlydf2:
 Y2,X2=np.histogram(numbersOnlydf2[column],bins=20,density=True)
 #plt.plot(X1[1:],Y1)
 error=[]
 s=column
 for distribution in distributions :
    tmp=distribution.fit(numbersOnlydf2[column])
    arg = tmp[:-2]
    loc = tmp[-2]
    scale = tmp[-1]
    pdf = distribution.pdf(X2, loc=loc, scale=scale, *arg)
    diff=pdf[1:]-Y1
    msq=pow(diff,2).mean()
    error.append(msq)

 v=distributions[error.index(min(error))]
 tmp=v.fit(numbersOnlydf2[column])
 argsofbestdistributionsYES.append(tmp)
 print("YES " + d[error.index(min(error))] +" distribution "+s)
 bestdistributionsYES.append(d[error.index(min(error))])
##############################################################################
#no 5
 
#for column in argsofbestdistributionsYES : 

a=bestdistributionsYES.copy()
b=bestdistributions.copy()

pchurn=1
i=0
test=numbersOnlydf.iloc[2589,:].tolist()
test2=numbersOnlydf2.iloc[15,:].tolist()
for column in numbersOnlydf:
     Y3,X3=np.histogram(numbersOnlydf2[column],bins=100,density=True)
     if(bestdistributionsYES[i]=='beta'):
          tmp1=st.beta.fit(numbersOnlydf2[column])
          arg = tmp1[:-2]
          loc = tmp1[-2]
          scale = tmp1[-1]
          pdf_test = st.beta.pdf(test2[i], loc=loc, scale=scale, *arg)
     if(bestdistributionsYES[i]=='norm'):
          tmp1=st.norm.fit(numbersOnlydf2[column]) 
          arg = tmp1[:-2]
          loc = tmp1[-2]
          scale = tmp1[-1]
          pdf_test = st.norm.pdf(test2[i], loc=loc, scale=scale, *arg)
     if(bestdistributionsYES[i]=='expon'):
          tmp1=st.expon.fit(numbersOnlydf2[column])
          arg = tmp1[:-2]
          loc = tmp1[-2]
          scale = tmp1[-1]
          pdf_test = st.expon.pdf(test2[i], loc=loc, scale=scale, *arg)
     if(bestdistributionsYES[i]=='alpha'):
          tmp1=st.alpha.fit(numbersOnlydf2[column])
          arg = tmp1[:-2]
          loc = tmp1[-2]
          scale = tmp1[-1]
          pdf_test = st.alpha.pdf(test2[i], loc=loc, scale=scale, *arg)
     if(bestdistributionsYES[i]=='gamma'):
          tmp1=st.gamma.fit(numbersOnlydf2[column])
          arg = tmp1[:-2]
          loc = tmp1[-2]
          scale = tmp1[-1]
          pdf_test = st.gamma.pdf(test2[i], loc=loc, scale=scale, *arg)
     if(bestdistributionsYES[i]=='exponnorm'):
          tmp1=st.exponnorm.fit(numbersOnlydf2[column])
          arg = tmp1[:-2]
          loc = tmp1[-2]
          scale = tmp1[-1]
          pdf_test = st.exponnorm.pdf(test2[i], loc=loc, scale=scale, *arg)
     
     
    
     Y4,X4=np.histogram(numbersOnlydf[column],bins=100,density=True)
     if(bestdistributions[i]=='beta'):
          tmp1=st.beta.fit(numbersOnlydf[column])
          arg = tmp1[:-2]
          loc = tmp1[-2]
          scale = tmp1[-1]
          pdf_test2 = st.beta.pdf(test[i], loc=loc, scale=scale, *arg)
     if(bestdistributions[i]=='norm'):
          tmp1=st.norm.fit(numbersOnlydf[column]) 
          arg = tmp1[:-2]
          loc = tmp1[-2]
          scale = tmp1[-1]
          pdf_test2 = st.norm.pdf(test[i], loc=loc, scale=scale, *arg)
     if(bestdistributionsYES[i]=='expon'):
          tmp1=st.expon.fit(numbersOnlydf[column])
          arg = tmp1[:-2]
          loc = tmp1[-2]
          scale = tmp1[-1]
          pdf_test2 = st.expon.pdf(test[i], loc=loc, scale=scale, *arg)
     if(bestdistributionsYES[i]=='alpha'):
          tmp1=st.alpha.fit(numbersOnlydf[column])
          arg = tmp1[:-2]
          loc = tmp1[-2]
          scale = tmp1[-1]
          pdf_test2 = st.alpha.pdf(test[i], loc=loc, scale=scale, *arg)
     if(bestdistributionsYES[i]=='gamma'):
          tmp1=st.gamma.fit(numbersOnlydf[column])
          arg = tmp1[:-2]
          loc = tmp1[-2]
          scale = tmp1[-1]
          pdf_test2 = st.gamma.pdf(test[i], loc=loc, scale=scale, *arg)
     if(bestdistributionsYES[i]=='exponnorm'):
          tmp1=st.exponnorm.fit(numbersOnlydf[column])
          arg = tmp1[:-2]
          loc = tmp1[-2]
          scale = tmp1[-1]
          pdf_test2 = st.exponnorm.pdf(test[i], loc=loc, scale=scale, *arg)
     
     
     
     
     p1=pdf_test/pdf_test2         
     pchurn*=p1
     i+=1







         
         
     
     