import os
import pandas as pd
import numpy as np


"""
plink --tfile try --recode
plink --file try --make-bed
plink2 --bfile try --export vcf-iid --out try_vcf.vcf
java -jar beagle.28Jun21.220.jar impute=true gt=try_vcf.vcf map=plink.chr1.GRCh38.map out=out iterations=12 ref=chr1.1kg.phase3.v5a.b37.bref3 chrom=1
"""

# setting up working directory
os.chdir("C:/Users/91809/Desktop/genebox/plink-1.07-dos/Haplotype calling")

#### keep all files in a folder 
py_file_path = os.path.dirname(os.path.abspath(__file__))
print("file path = ",py_file_path)
os.chdir(py_file_path)



## this code test if python reads internal files in working directory folder
"""
for file in os.listdir():
    print(file)
"""



# 1 -24 chr   
for i in range(1,24):
    print("Counter i ================================================================-========",i)
    command1  = "plink --tfile try"+str(i)+" --recode"
    os.system(command1)
    print("command1 success ----------------")
    source1 = "plink.PED"
    source2 = "plink.MAP"
    dest1="try"+str(i)+".PED"
    dest2="try"+str(i)+".MAP"
    os.rename('plink.PED', dest1)
    os.rename('plink.MAP', dest2)
    print("files renamed for i= ",i)
    command2  = "plink --file try"+str(i)+" --make-bed"
    os.system(command2)
    print("command2 success ----------------")
    source1 = "plink.BED"
    source2 = "plink.BIM"
    source3 = "plink.FAM"
    dest1="try"+str(i)+".BED"
    dest2="try"+str(i)+".BIM"
    dest3="try"+str(i)+".FAM"
    os.rename('plink.BED', dest1)
    os.rename('plink.BIM', dest2)
    os.rename('plink.FAM',dest3)
    print("command 2 files changed")
    command3 = "plink2 --bfile try"+str(i)+" --export vcf-iid --out try"+str(i)+".vcf"
    os.system(command3)
    print("command3 success ----------------")
    #source1 = "plink.vcf"
    #dest1="try"+str(i)+".vcf"
    #os.rename('plink.vcf', dest1)   
#os.system("plink command3")
    new_name = "out_"+str(i)
#os.rename("out.log",new_name+".log")
# os.rename("out.vcf",new_name+".vcf")
    print("######################      Done with PLINK    ################################################################################################################")
    command4 = "java -jar beagle.28Jun21.220.jar impute=true gt=try"+str(i)+".vcf.vcf map=plink.chr"+str(i)+".GRCh38.map out=out iterations=12 ref=chr"+str(i)+".1kg.phase3.v5a.b37.bref3 chrom="+str(i)
    os.system(command4)
    print("command4 success ----------------------------------")
    new_name = "try"+str(i)
    os.rename("out.log",new_name+".log")
    os.rename("out.vcf.gz",new_name+".vcf.gz")
    print("done ################################################################################################################")
    ### X chr
    print(" =====================  X Chr ===============================")
    command5  = "java -jar beagle.28Jun21.220.jar impute=true gt=try"+str(i)+".vcf.vcf map=plink.chrX.GRCh38.map out=out iterations=12 ref=chrX.1kg.phase3.v5a.b37.bref3 chrom=X"
    os.system(command5)
    new_name = "tryX"
    os.rename("out.log",new_name+".log")
    os.rename("out.vcf.gz",new_name+".vcf.gz")
