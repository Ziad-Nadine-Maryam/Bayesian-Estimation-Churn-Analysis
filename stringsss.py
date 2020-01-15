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
Stringnew=df.select_dtypes(include=['object'])


#y=String.CreditRating.value_counts(normalize=True)
#print(y)
fg=[]
y1=Stringnew.ServiceArea.value_counts(normalize=True)
y2=Stringnew.ChildrenInHH.value_counts(normalize=True)
y3=Stringnew.HandsetRefurbished.value_counts(normalize=True)
y4=Stringnew.HandsetWebCapable.value_counts(normalize=True)
y5=Stringnew.TruckOwner.value_counts(normalize=True)
y6=Stringnew.RVOwner.value_counts(normalize=True)
y7=Stringnew.Homeownership.value_counts(normalize=True)
y8=Stringnew.BuysViaMailOrder.value_counts(normalize=True)
y9=Stringnew.RespondsToMailOffers.value_counts(normalize=True)
y10=Stringnew.OptOutMailings.value_counts(normalize=True)
y11=Stringnew.NonUSTravel.value_counts(normalize=True)
y12=Stringnew.OwnsComputer.value_counts(normalize=True)
y13=Stringnew.HasCreditCard.value_counts(normalize=True)
y14=Stringnew.NewCellphoneUser.value_counts(normalize=True)
y15=Stringnew.NotNewCellphoneUser.value_counts(normalize=True)
y16=Stringnew.OwnsMotorcycle.value_counts(normalize=True)
y17=Stringnew.HandsetPrice.value_counts(normalize=True)
y18=Stringnew.MadeCallToRetentionTeam.value_counts(normalize=True)
y19=Stringnew.CreditRating.value_counts(normalize=True)
y20=Stringnew.PrizmCode.value_counts(normalize=True)
y21=Stringnew.Occupation.value_counts(normalize=True)
y22=Stringnew.MaritalStatus.value_counts(normalize=True)





Stringnew2=Stringnew.loc[df.Churn=='Yes']

q1=Stringnew2.ServiceArea.value_counts(normalize=True)
q2=Stringnew2.ChildrenInHH.value_counts(normalize=True)
q3=Stringnew2.HandsetRefurbished.value_counts(normalize=True)
q4=Stringnew2.HandsetWebCapable.value_counts(normalize=True)
q5=Stringnew2.TruckOwner.value_counts(normalize=True)
q6=Stringnew2.RVOwner.value_counts(normalize=True)
q7=Stringnew2.Homeownership.value_counts(normalize=True)
q8=Stringnew2.BuysViaMailOrder.value_counts(normalize=True)
q9=Stringnew2.RespondsToMailOffers.value_counts(normalize=True)
q10=Stringnew2.OptOutMailings.value_counts(normalize=True)
q11=Stringnew2.NonUSTravel.value_counts(normalize=True)
q12=Stringnew2.OwnsComputer.value_counts(normalize=True)
q13=Stringnew2.HasCreditCard.value_counts(normalize=True)
q14=Stringnew2.NewCellphoneUser.value_counts(normalize=True)
q15=Stringnew2.NotNewCellphoneUser.value_counts(normalize=True)
q16=Stringnew2.OwnsMotorcycle.value_counts(normalize=True)
q17=Stringnew2.HandsetPrice.value_counts(normalize=True)
q18=Stringnew2.MadeCallToRetentionTeam.value_counts(normalize=True)
q19=Stringnew2.CreditRating.value_counts(normalize=True)
q20=Stringnew2.PrizmCode.value_counts(normalize=True)
q21=Stringnew2.Occupation.value_counts(normalize=True)
q22=Stringnew2.MaritalStatus.value_counts(normalize=True)

    