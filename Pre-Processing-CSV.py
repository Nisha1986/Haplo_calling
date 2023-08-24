#Importing Libraries
import pandas as pd 
import glob

#Getting Raw Sam for current batch
files = glob.glob("*_final_ordered.csv")
leng=len('_final_ordered.csv')

#Loop
for i in files:
    print(i)
    #Reading Raw
    final = pd.read_csv(i, low_memory=False)
    print("--Raw File--")
    print(final.head())
    
    #Changing Column names and orders
    final = final.rename(columns={"Position":"position","RsID":"rsid","Chr":"chromosome",final.columns[-3]:'Allele1...Plus',final.columns[-2]:'Allele2...Plus',final.columns[-1]:'genotype'})
    #print(final.head())
    final = final[["rsid","chromosome","position",'genotype','Allele1...Plus','Allele2...Plus']]
    final = final.astype(str)

    #Clean the alleles having NA 
    final['position'] = final['position'].fillna(0)
    final["position"] = final["position"].astype(int)
    final['chromosome'] = final['chromosome'].str.split('.',expand=True)[0]
    final['chromosome'] = final['chromosome'].astype(str)
    final["genotype"] = final["genotype"].replace("00","--")
    final["genotype"] = final["genotype"].fillna("--")
    final["Allele1...Plus"] = final["Allele1...Plus"].replace("0","-")
    final["Allele2...Plus"] = final["Allele2...Plus"].replace("0","-")
    final["Allele1...Plus"] = final["Allele1...Plus"].fillna("-")
    final["Allele2...Plus"] = final["Allele2...Plus"].fillna("-")
    
    #Converted File
    print("--CONVERTED File--")
    print(final.head())
    
    #Saving
    final.to_csv(str(i[:-leng])+"-Pro.csv",index=False)
    print(i[:-leng]+'_done')

