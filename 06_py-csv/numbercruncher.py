"""
TeOrtiz: Vivian Teo, Emily Ortiz 
SoftDev
K06 -- Random Jobs
2022-09-30
time spent: 1 hour

DISCO: Discovered the weighted parameter in random.choices

QCC: What other methods are there to tackle weighted random without the built in function?
"""

import random

#open file and read it into a string
file = open("occupations.csv", 'r')
content = file.read()
#splitting the file's info by line and making it a list
total_list = content.split('\n')
# getting rid of first and last line
total_list = total_list[1:-2]
#create empty dict for jobs
job_dict = {}

for job in total_list:
    # for each job in the list, split it by the last comma once
    job_list = job.rsplit(',',1)
    # read the occupation title into dict as key, read the percentage into dict as value
    job_dict[job_list[0]] = float(job_list[1]) # typecast percentage from string to float
    
# print(job_dict)    

def weighted_random(job_dict):
    #use python's built-in weighted random choice function to get a job title
    random_job = random.choices(list(dict.keys(job_dict)), weights=list(dict.values(job_dict)))
    # since random_job is a list consisting of one element, we can print the first element
    print(random_job[0])
    
# weighted_random(job_dict)

# print("Pick 10 random jobs:")
# for i in range(10):
#     weighted_random(job_dict)
