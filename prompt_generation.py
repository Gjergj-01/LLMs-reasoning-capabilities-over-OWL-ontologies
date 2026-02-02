import json

'''
In the follwoing script I prepare the json files with the prompt for the LLMs
'''


### Knowledge Base written in OWL functional syntax

knowledgeBase = """
Declaration(Class( :Candidate))
Declaration(Class( :Job))
Declaration(Class( :Recruiter))
Declaration(Class( :Employee))
Declaration(Class( :Manager))
Declaration(Class( :CompanyManager))
Declaration(Class( :TeamManager))
Declaration(Class( :Company))

Declaration(ObjectProperty( :applies))
Declaration(ObjectProperty( :hasReferent))
Declaration(ObjectProperty( :interviews))
Declaration(ObjectProperty( :hires))
Declaration(ObjectProperty( :opensPosition))
Declaration(ObjectProperty( :worksIn))
Declaration(ObjectProperty( :manages))

SubClassOf( :TeamManager :Manager)
SubClassOf( :CompanyManager :Manager)
SubClassOf( :Manager :Employee)
SubClassOf( :Recruiter :Employee)

SubClassOf(
    :Candidate
    :ObjectSomeValuesFrom( :applies owl:Thing))

SubClassOf(
    :Employee
    :ObjectSomeValuesFrom( :worksIn owl:Thing))

DisjointClasses( :CompanyManager :TeamManager)
DisjointClasses( :Manager :Recruiter)
DisjointClasses( :Employee :Candidate)
DisjointClasses( :Employee :Company)
DisjointClasses( :Employee :Job)
DisjointClasses( :Candidate :Job)
DisjointClasses( :Candidate :Company)
DisjointClasses( :Company :Job)

ObjectPropertyDomain( :applies :Candidate)
ObjectPropertyRange( :applies :Job)

ObjectPropertyDomain( :interviews :Recruiter)
ObjectPropertyRange( :interviews :Candidate)

ObjectPropertyDomain( :hires :Recruiter)
ObjectPropertyRange( :hires :Candidate)

ObjectPropertyDomain( :hasReferent :Job)
ObjectPropertyRange( :hasReferent :Recruiter)

ObjectPropertyDomain( :opensPosition :Company)
ObjectPropertyRange( :opensPosition :Job)

ObjectPropertyDomain( :worksIn :Employee)
ObjectPropertyRange( :worksIn :Company)

ObjectPropertyDomain( :manages :CompanyManager)
ObjectPropertyRange( :manages :Company)

SubObjectPropertyOf( :hires :interviews)
subObjectPropertyOf( :hires :worksIn)
"""

# save the knowledge base in a json file
d = {"KB": knowledgeBase}
with open ("tasks/knowledge_base.json", "w") as f:
    json.dump(d, f)


### In the following I define the instructions to pass to the LLM for the three different tasks:
### Query answering, Instance checking, Inconsistency checking



#########################
#   QUERY ANSWERING TASK 
#########################


query_answering_task = """
Given the knowledge base that is provided, you are asked to answer the following queries:
- Q1: 
- Q2: 
- Q3:

showing for each of them in detail the reasoning steps that led to the answers.
"""

query_answering_format = """
Structure your response as follows: 
Response: 
Q1: (your reasoning steps) --- [answer].
Q2: (your reasoning steps) --- [answer].
Q3: (ypur reasoning steps) --- [answer].
Notice that the sequence "---" must be unique (and must always be present) in the response of each query, as it will be used as separator for the answer.
"""

d = {"query_answering_task": query_answering_task, "query_answering_format": query_answering_format}

## save the query answer task instructions
with open("tasks/query_answering.json", "w") as f:
    json.dump(d, f)


#########################
# INCONSISTENCY CHECKING
#########################

inconsistency_checking_task = """
Given the knowledge base that is provided, your task is to tell whether it is consistent or not.
Explain in detail the reasoning steps that led to your answer (which must be YES or NO).
"""

inconsistency_checking_format = """
Structure your response as follows:
Response: (your reasoning steps) --- [answer] (YES or NO)
Notice that the sequence "---" must be unique (and always present) in the response, as it will be used as separator for the answer.
"""

d = {"inconsistency_checking_task": inconsistency_checking_task, "inconsistency_checking_format": inconsistency_checking_format}

## save the inconsistency checking task instructions
with open("tasks/inconsistency_checking.json", "w") as f:
    json.dump(d, f)


####################
# INSTANCE CHECKING
####################

instance_checking_task = """
Given the knowledge base that is provided, your task is to tell whether the following assertions hold:
A1:
A2:
A3:

showing for each of them in detail the reasoning steps that led to the answers.
"""

instance_checking_format = """
Structure your response as follows:
Response:
A1: (your reasoning steps) --- [answer] (YES or NO)
A2: (your reasoning steps) --- [answer] (YES or NO)
A3: (your reasoning steps) --- [answer] (YES or NO)
Notice that the sequence "---" must be unique (and must always be present) in the response for each, as it will be used as separator for the answer.
"""

d = {"instance_checking_task": instance_checking_task, "instance_checking_format": instance_checking_format}

## save the instance checking task instructions
with open("tasks/instance_checking.json", "w") as f:
    json.dump(d, f)

print("DONE")