#Import Libraries
import pandas as pd

tfile = input("Enter the tfile name: \n")

#Reading Tped
print("reading tped")
a = pd.read_csv(tfile+".tped",sep='\s+',header = None, engine='python')
a = a.astype(str)
print("done")

##Merging the columns of the tped allele to one
print("merging cols")
x=3
for i in range(4,a.shape[1],2):
    a[(x+1)]= a[(i)]+a[(i+1)]
    x=x+2

print("done")

#Dropping the extra Columns
print("dropping cols")
columns = [(i+1) for i in range(4,a.shape[1],2)]
a.drop(columns, inplace=True, axis=1)

#Getting the samples name from Tfam
print("reading tfam")
b=pd.read_csv(tfile+".tfam",sep='\s+',names=['fam id','sam ID ','pat id','mat id','sex','affected'],engine='python')
print("done")

#Creating a proper data Frame
print("creating df")
li=['chrom','rs ID','cM','Map']
for i in b['sam ID ']:
    li.append(i)

s = pd.DataFrame([li] + a.values.tolist(), columns=a.columns)
new_header = s.iloc[0] 
s = s[1:] 
s.columns = new_header
print("done")
print(s.head())

sample_type= input("Enter the sample type: \n")

#Saving the samples as individual
for i in range(4,len(s.columns)):
    che_1 = s.iloc[:,[0,1,3]]
    che_2 = s.loc[:,s.columns[i]]
    che = pd.concat([che_1,che_2],axis = 1)
    name = che.columns[3]
    che['Allele1'] = che[che.columns[3]].str[0]
    che['Allele2'] = che[che.columns[3]].str[1]
    che.to_csv(str(name)+"-"+str(sample_type)+".csv")
    print(name, " Done")
