
# coding: utf-8

# In[ ]:


from mrjob.job import MRJob
import re

WORD_RE = re.compile(r'[\w]+') 
class MRSummaryStats(MRJob):

    def mapper(self, _, line):
        numb = line.split()
        yield numb[0], (float(numb[1]), 1)
        
    def reducer(self, key, values):
        count = []
        count2 = []
        numb = []
        for value in values:
            count.append(value[0])
            count2.append(value[0]**2)
            numb.append(value[1])
        yield key, (sum(numb), sum(count)/sum(numb), (sum(count2)-(sum(count))**2/sum(numb))/sum(numb))


if __name__ == '__main__':
    MRSummaryStats.run()

