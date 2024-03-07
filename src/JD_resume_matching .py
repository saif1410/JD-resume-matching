#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 
import pandas as pd
from fuzzywuzzy import fuzz
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import re 
sw = stopwords.words('english') 


# In[2]:


#JD Parsing 

#get the skills from the JD after uploading 
import resume_parser_src.matcher as skxt   #this module is imported from resume parser project

#jd_skills=skxt.extract_skills() function is used for extracting skills from JD

jd_skills=["Computer Vision", "Image Processing","Eye Tracking", "Gaze Tracking", 
                        "Machine Learning", "C", "C++", "Python"]  #list for demo 

jd_skills=[element.lower() for element in jd_skills]



#candidate_skills=skxt.extract_skills() function can be imported from resume parser src for extracting candidate's skills 

candidate_skills=["Image Processing",  
                        "Machine Learning", "Python"]  #list for demo purpose

candidate_skills=[element.lower() for element in candidate_skills]


# In[3]:


# creating class for making a master vector set inside default constructor
# create_vector function is for creating future vectors based on the master set 
# cosine_similarity is for comparing those two vectors

class vectorize:
    
    def __init__(self):
        global theset
        theset=set()   #master vector set
        #path to db skills
        path="/home/mirafra/projects/resume_parser-main/src/corpus_creation/db_csv/skills" 
        for files in os.listdir(path):  #path to skills corpus 
            df=pd.read_csv(path+"/"+files)
            for row in df.iloc:
                theset.add((row.ABB).lower())
                theset.add((row.FF).lower())
        #the set is used as an n-dimensional vector space with each skills being a dimension
            
    def create_vector (self,skills):
       
        self.skills=skills
        created_vector=[]
        for w in theset: 
          if w in skills:
             created_vector.append(1) # create a vector 
          else:
             created_vector.append(0)
                
        return ((created_vector))
    
    def cosine_similarity (self,jd_vector, candidate_vector):
        self.jd_vector=jd_vector 
        self.candidate_vector=candidate_vector
        c=0
        for i in range(len(theset)): 
            c+= ((jd_vector[i])*(candidate_vector[i]))
        y=float((sum(jd_vector)*sum(candidate_vector))**0.5) 
        if y==0:
            return 0
        else:
            cosine = c / y
        return(cosine*100)


# In[4]:


g=vectorize() #object of the class 

#make vectors for both jd and extracted skills 
jd_vector=g.create_vector((jd_skills))  #vector creation for jd
candidate_vector=g.create_vector(candidate_skills) #vector creation for candidate
cosine_score=g.cosine_similarity(jd_vector,candidate_vector) 


# In[5]:


print(cosine_score)


# In[ ]:




