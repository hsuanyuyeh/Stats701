
# coding: utf-8

# In[ ]:


from pyspark import SparkConf, SparkContext
import sys

if len(sys.argv) != 3:
    print('Usage:' + sys.argv[0] + '<in><out>')
    sys.exit(1)
inputlocation = sys.argv[1]
outputlocation = sys.argv[2]
 
# set up configuration and jon context
conf = SparkConf().setAppName('Test')
sc = SparkContext(conf = conf)

# load the data
data = sc.textFile(inputlocation)
data = data.map(lambda line: line.split())

def pair(l):
    pa = [tuple(sorted((l[0],l[i],l[j]))) for i in range(1, len(l)) for j in range(i+1, len(l))]
    return(pa)


data_new = data.flatMap(lambda row: pair(row))
data_new1 = data_new.map(lambda ele: (ele, 1))
data_new2 = data_new1.reduceByKey(lambda x,y: x+y)
data_new3 = data_new2.filter(lambda x: x[1]>=2)
output = data_new3.map(lambda x: x[0])

output.saveAsTextFile(outputlocation)
sc.stop()

