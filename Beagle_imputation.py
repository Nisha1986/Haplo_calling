import os
import pandas as pd
import numpy as np




"""
java -jar beagle.28Jun21.220.jar impute=true gt=try_vcf.vcf map=plink.chr1.GRCh38.map out=out iterations=12 ref=chr1.1kg.phase3.v5a.b37.bref3 chrom=1
"""

# setting up working directory
#os.chdir("/home/aadhya19/pipeline")

#### keep all files in a folder 
py_file_path = os.path.dirname(os.path.abspath(__file__))
print("file path = ",py_file_path)
os.chdir(py_file_path)


## this code test if python reads internal files in working directory folder
"""
for file in os.listdir():
    print(file)
"""

# 1 -23 chr   
for i in range(1,23):
    print("Counter i ================================================================-========",i)
    command  = "java -jar beagle.28Jun21.220.jar impute=true gt=try_vcf.vcf map=plink.chr"+str(i)+".GRCh38.map out=out iterations=12 ref=chr"+str(i)+".1kg.phase3.v5a.b37.bref3 chrom="+str(i)
    os.system(command)
    new_name = "out_"+str(i)
    os.rename("out.log",new_name+".log")
    os.rename("out.vcf.gz",new_name+".vcf.gz")
 
### X chr
print(" =====================  X Chr ===============================")
command1  = "java -jar beagle.28Jun21.220.jar impute=true gt=try_vcf.vcf map=plink.chrX.GRCh38.map out=out iterations=12 ref=chrX.1kg.phase3.v5a.b37.bref3 chrom=X"
os.system(command1)
new_name = "out_X"
os.rename("out.log",new_name+".log")
os.rename("out.vcf.gz",new_name+".vcf.gz")


