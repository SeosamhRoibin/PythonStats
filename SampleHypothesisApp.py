import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

def dataOutput():
    limit = int(input("Enter the step of each data you wish to see"))
    UpperLimitOfDataSet = int(input("Nums to be generated for dataset1"))
    UpperLimitOfDataSet1 = int(input("Nums to be generated for dataset2"))
    DataSet = np.random.randn(UpperLimitOfDataSet)
    DataSet1 = np.random.randn(UpperLimitOfDataSet1)
    print("EVERY 10th NUMBER IN FIRST DATASET")
    for i in range(0, len(DataSet)):
        if (i % limit == 0):
            print(i, DataSet[i])
    print("EVERY 10th NUMBER IN SECOND DATASET")
    for j in range(0, len(DataSet1)):
        if (j % limit == 0):
            print(j, DataSet[j])
            
    DataSet_mean = np.mean(DataSet)
    DataSet1_mean = np.mean(DataSet1)
    print("The mean for data set is:")
    print(DataSet_mean)
    print("The mean for the second data set is:")
    print(DataSet1_mean)
    DataSet_std = np.std(DataSet) 
    DataSet1_std = np.std(DataSet1)
    print("The standard deviation from the mean is:")
    print(DataSet_std)
    print("The standard deviation from the mean for the second data set is:")
    print(DataSet1_std)
    print("These are the histograms")
    hypothesisTestGen(DataSet, DataSet1)
    plotHist(DataSet)
    plotHist(DataSet1)
  
    
def plotHist(x):
    plt.hist(x)
    plt.title('histogram')
    plt.xlabel('value')
    plt.ylabel('data')

def hypothesisTestGen(y, z):
    print("Results of hypothesis test")
    ttest, pval = ttest_ind(y, z)
    print("The p-value is")
    print(pval)
    if (pval < 0.05):
        print("As the pvalue is less than 0.05, we have sufficieint evidence to reject the \
              null hypothesis")
    else:
        print("The pvalue is greater than 0.05, therefore we do not have sufficient evidence \
              to reject the null hypothesis")
 
dataOutput()

