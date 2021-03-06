import pandas     as pd
import numpy      as np
import scipy.stats as st
df=pd.read_csv(r'C:\Users\ziadm\Ziad\cell2celltrain.csv') 
#print(df.isnull().sum())
df.replace(-np.inf, np.nan)
df=df.dropna()


numbersOnly=df.select_dtypes(exclude=[np.object])
numbersOnlydf=numbersOnly.drop(columns=['CustomerID'])



corr = numbersOnlydf.corr()
cov=numbersOnlydf.cov()
ziad=df.loc[df.Churn=='Yes']
numbersOnly2=ziad.select_dtypes(exclude=[np.object])
numbersOnlydf2=numbersOnly2.drop(columns=['CustomerID'])

bestdistributionsYES=['expon','gamma','expon','exponnorm','exponnorm','norm','alpha','expon','alpha','expon','beta','expon','expon','beta','beta','expon','beta','exponnorm','alpha','norm','expon','expon','beta','expon','exponnorm','beta','alpha','alpha','gamma','beta','gamma','expon','expon','expon']
bestdistributions=['exponnorm','expon','exponnorm','expon','expon','norm','exponnorm','exponnorm','expon','exponnorm','beta','expon','expon','expon','expon','expon','expon','exponnorm','exponnorm','norm','expon','beta','norm','alpha','exponnorm','beta','exponnorm','beta','gamma','expon','expon','norm','expon','norm']

r=0
l=0

while (k<13001) :
        test=numbersOnlydf.iloc[k,:].tolist()
        #test2=numbersOnlydf2.iloc[59,:].tolist()
        pqw=[]
        pchurn=1
        i=0
        for column in numbersOnlydf:
                     Y3,X3=np.histogram(numbersOnlydf2[column],bins=20,density=True)
                     if(bestdistributionsYES[i]=='beta'):
                          tmp1=st.beta.fit(numbersOnlydf2[column])
                          arg = tmp1[:-2]
                          loc = tmp1[-2]
                          scale = tmp1[-1]
                          pdf_test = st.beta.pdf(test[i], loc=loc, scale=scale, *arg)
                     if(bestdistributionsYES[i]=='norm'):
                          tmp1=st.norm.fit(numbersOnlydf2[column]) 
                          arg = tmp1[:-2]
                          loc = tmp1[-2]
                          scale = tmp1[-1]
                          pdf_test = st.norm.pdf(test[i], loc=loc, scale=scale, *arg)
                     if(bestdistributionsYES[i]=='expon'):
                          tmp1=st.expon.fit(numbersOnlydf2[column])
                          arg = tmp1[:-2]
                          loc = tmp1[-2]
                          scale = tmp1[-1]
                          pdf_test = st.expon.pdf(test[i], loc=loc, scale=scale, *arg)
                     if(bestdistributionsYES[i]=='alpha'):
                          tmp1=st.alpha.fit(numbersOnlydf2[column])
                          arg = tmp1[:-2]
                          loc = tmp1[-2]
                          scale = tmp1[-1]
                          pdf_test = st.alpha.pdf(test[i], loc=loc, scale=scale, *arg)
                     if(bestdistributionsYES[i]=='gamma'):
                          tmp1=st.gamma.fit(numbersOnlydf2[column])
                          arg = tmp1[:-2]
                          loc = tmp1[-2]
                          scale = tmp1[-1]
                          pdf_test = st.gamma.pdf(test[i], loc=loc, scale=scale, *arg)
                     if(bestdistributionsYES[i]=='exponnorm'):
                          tmp1=st.exponnorm.fit(numbersOnlydf2[column])
                          arg = tmp1[:-2]
                          loc = tmp1[-2]
                          scale = tmp1[-1]
                          pdf_test = st.exponnorm.pdf(test[i], loc=loc, scale=scale, *arg)
                     
                     
                    
                     Y4,X4=np.histogram(numbersOnlydf[column],bins=20,density=True)
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
                     if(bestdistributions[i]=='expon'):
                          tmp1=st.expon.fit(numbersOnlydf[column])
                          arg = tmp1[:-2]
                          loc = tmp1[-2]
                          scale = tmp1[-1]
                          pdf_test2 = st.expon.pdf(test[i], loc=loc, scale=scale, *arg)
                     if(bestdistributions[i]=='alpha'):
                          tmp1=st.alpha.fit(numbersOnlydf[column])
                          arg = tmp1[:-2]
                          loc = tmp1[-2]
                          scale = tmp1[-1]
                          pdf_test2 = st.alpha.pdf(test[i], loc=loc, scale=scale, *arg)
                     if(bestdistributions[i]=='gamma'):
                          tmp1=st.gamma.fit(numbersOnlydf[column])
                          arg = tmp1[:-2]
                          loc = tmp1[-2]
                          scale = tmp1[-1]
                          pdf_test2 = st.gamma.pdf(test[i], loc=loc, scale=scale, *arg)
                     if(bestdistributions[i]=='exponnorm'):
                          tmp1=st.exponnorm.fit(numbersOnlydf[column])
                          arg = tmp1[:-2]
                          loc = tmp1[-2]
                          scale = tmp1[-1]
                          pdf_test2 = st.exponnorm.pdf(test[i], loc=loc, scale=scale, *arg)
                     
                     
                     
                     
                     p1=pdf_test/pdf_test2         
                     pqw.append(p1)
                     i+=1             
             
             
        
        
        abc=14245/49752
        #pfinal=pchurn*abc     
        #print(pfinal)   
        res=1
        j=0
        
        
        c=[1,2,3,4,5,13,14,15,16,17,18,25,26,27,28,29,30,33]
        #j==1 or j==2 or j==3 or j==4 or j==5 or j==13 or j==14 or j==15 or j==16 or j==17 or j==18 or j==25 or j==26 or j==27 or j==28 or j==29 or j==3o or j==33
        
        while (j<34) :
                if(j==1 or j==2 or j==3 or j==4 or j==5 or j==13 or j==14 or j==15 or j==16 or j==17 or j==18 or j==25 or j==26 or j==27 or j==28 or j==29 or j==30 or j==33) :
                    j+=1
                else   :
                    res=res*pqw[j]
                    j+=1
                    print(res)
        
        
        pfinal=res*abc
        (print)
        print(pfinal)
        k+=1
        print()
        if(pfinal>0.5) :
         r+=1
        if(pfinal<0.5) :
         l+=1
        
        
        print(r)
        print(k-12900)
        print('------------')
#print(pdf_test2)
#         print()
#         print(pdf_test)
#         print()
#         print()
#         print()

  