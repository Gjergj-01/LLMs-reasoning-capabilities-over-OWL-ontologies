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
Declaration(Class( :Team))

Declaration(ObjectProperty( :applies))
Declaration(ObjectProperty( :hasReferent))
Declaration(ObjectProperty( :interviews))
Declaration(ObjectProperty( :hires))
Declaration(ObjectProperty( :opensPosition))
Declaration(ObjectProperty( :worksIn))
Declaration(ObjectProperty( :manages))
Declaration(ObjectProperty( :composedBy))
Declaration(ObjectProperty( :headOf))

SubClassOf( :TeamManager :Manager)
SubClassOf( :CompanyManager :Manager)
SubClassOf( :Manager :Employee)
SubClassOf( :Recruiter :Employee)

SubClassOf(
    :Candidate
    ObjectSomeValuesFrom( :applies owl:Thing))

SubClassOf(
    :Employee
    ObjectSomeValuesFrom( :worksIn owl:Thing))

SubClassOf(
    :Team
    ObjectSomeValuesFrom( :composedBy owl:Thing))


DisjointClasses( :CompanyManager :TeamManager)
DisjointClasses( :Manager :Recruiter)
DisjointClasses( :Employee :Candidate)  
DisjointClasses( :Employee :Company)
DisjointClasses( :Employee :Job)
DisjointClasses( :Employee :Team)
DisjointClasses( :Candidate :Job)
DisjointClasses( :Candidate :Company)
DisjointClasses( :Candidate :Team)
DisjointClasses( :Company :Job)
DisjointClasses( :Company :Team)
DisjointClasses( :Job :Team)

ObjectPropertyDomain( :applies :Candidate)
ObjectPropertyRange( :applies :Job)

ObjectPropertyDomain( :interviews :Recruiter)
ObjectPropertyRange( :interviews :Candidate)

ObjectPropertyDomain( :hasReferent :Job)
ObjectPropertyRange( :hasReferent :Recruiter)

ObjectPropertyDomain( :opensPosition :Company)
ObjectPropertyRange( :opensPosition :Job)

ObjectPropertyDomain( :worksIn :Employee)
ObjectPropertyRange( :worksIn :Company)

ObjectPropertyDomain( :manages :CompanyManager)
ObjectPropertyRange( :manages :Company)
FunctionalObjectProperty( :manages)

ObjectPropertyDomain( :composedBy :Team)
ObjectPropertyRange( :composedBy :Employee)

ObjectPropertyDomain( :headOf :TeamManager)
ObjectPropertyRange( :headOf :Team)

SubObjectPropertyOf( :hires :interviews)

ClassAssertion( :Candidate :Ann)
ClassAssertion( :Candidate :Bob)
ClassAssertion( :Candidate :Luca)
ClassAssertion( :Candidate :Elena)

ClassAssertion( :Job :DataEngineer)
ClassAssertion( :Job :SoftwareEngineer)
ClassAssertion( :Job :Lawyer)

ClassAssertion( :Recruiter :Francesca)
ClassAssertion( :Recruiter :Matteo)

ObjectPropertyAssertion( :hasReferent :AIEngineer :Marco)
ObjectPropertyAssertion( :hasReferent :DataEngineer :Marco)
ObjectPropertyAssertion( :hasReferent :SoftwareEngineer :Matteo)
ObjectPropertyAssertion( :hasReferent :Lawyer :Francesca)

ObjectPropertyAssertion( :applies :Elena :Lawyer)
ObjectPropertyAssertion( :applies :Luca :DataEngineer)
ObjectPropertyAssertion( :applies :Luca :CloudEngineer)
ObjectPropertyAssertion( :applies :Ann :AIEngineer)

ObjectPropertyAssertion( :hires :Marco :Luca)
ObjectPropertyAssertion( :hires :Francesca :Elena)

ObjectPropertyAssertion( :interviews :Matteo :Ann)
ObjectPropertyAssertion( :interviews :Francesca :Bob)

ClassAssertion( :Company :Unicredit)
ClassAssertion( :Company :Google)

ObjectPropertyAssertion( :opensPosition :Unicredit :Lawyer)
ObjectPropertyAssertion( :opensPosition :Unicredit :AIEngineer)
ObjectPropertyAssertion( :opensPosition :Google :JavaDeveloper)
ObjectPropertyAssertion( :opensPosition :Google :DataEngineer)

ObjectPropertyAssertion( :worksIn :Marco :Google)
ObjectPropertyAssertion( :worksIn :Francesca :Unicredit)

ObjectPropertyAssertion( :headOf :Alessio :CyberSecurityTeam)
ObjectPropertyAssertion( :composedBy :CyberSecurityTeam :Emanuela)
ObjectPropertyAssertion( :composedBy :CyberSecurityTeam :Fabio)

ObjectPropertyAssertion( :manages :Giulia :PosteItaliane)
ObjectPropertyAssertion( :manages :LarryPage :Google)

"""

# save the knowledge base in a json file
d = {"KB": knowledgeBase}
with open ("tasks/knowledge_base.json", "w") as f:
    json.dump(d, f)

### In the following I define the instructions to pass to the LLM for the three different tasks:
### Query answering, Instance checking, Inconsistency checking



####################
#   QUERY ANSWERING
####################


query_answering_task = """
Given the knowledge base that is provided, you are asked to answer the following queries (expressed in Manchester OWL syntax):
- Q1: Employee AND interviews VALUE Luca
- Q2: Employee (In natural language: Return all the employees)
- Q3: Employee AND interviwes VALUE Ann and hires SOME 
- Q4: worksIn VALUE Google

showing for each of them in detail the reasoning steps that led to the answers.
"""

query_answering_format = """
Structure your response as follows: 
Q1: (your reasoning steps) --- [answer].
Q2: (your reasoning steps) --- [answer].
Q3: (ypur reasoning steps) --- [answer].
Q4: (ypur reasoning steps) --- [answer].
Notice that the sequence "---" must be unique (and must always be present) in the response of each query, as it will be used as separator for the answer.
"""

d = {"query_answering_task": query_answering_task, "query_answering_format": query_answering_format}

## save the query answer task instructions
with open("tasks/query_answering.json", "w") as f:
    json.dump(d, f, indent=4)



#########################
# INCONSISTENCY CHECKING
#########################

inconsistent_KB = knowledgeBase + "\nClassAssertion( :Employee :Luca)"

inconsistency_checking_task = """
Given the knowledge base that is provided, your task is to tell whether it is consistent or not.
Explain in detail the reasoning steps that led to your answer (which must be YES or NO).
"""

inconsistency_checking_format = """
Structure your response as follows:
(your reasoning steps) --- [answer]
Notice that the sequence "---" must be unique (and always present) in the response, as it will be used as separator for the answer.
"""

d = {"KB": inconsistent_KB, "inconsistency_checking_task": inconsistency_checking_task, "inconsistency_checking_format": inconsistency_checking_format}

## save the inconsistency checking task instructions
with open("tasks/inconsistency_checking.json", "w") as f:
    json.dump(d, f, indent=4)



####################
# INSTANCE CHECKING
####################


instance_checking_task = """
Given the knowledge base that is provided, your task is to tell whether the following assertions hold:
A1: ObjectPropertyAssertion( :worksIn :LarryPage :Google)
A2: ObjectPropertyAssertion( :worksIn :Matteo :Unicredit)
A3: ClassAssertion( :Employee :Giulia)
A4: ObjectPropertyAssertion( :hasReferent :AIEngineer :Matteo)

showing for each of them in detail the reasoning steps that led to the answers (which must be YES or NO).
"""

instance_checking_format = """
Structure your response as follows:
A1: (your reasoning steps) --- [answer]
A2: (your reasoning steps) --- [answer]
A3: (your reasoning steps) --- [answer]
A4: (your reasoning steps) --- [answer]
Notice that the sequence "---" must be unique (and must always be present) in the response for each, as it will be used as separator for the answer.
"""

d = {"instance_checking_task": instance_checking_task, "instance_checking_format": instance_checking_format}

## save the instance checking task instructions
with open("tasks/instance_checking.json", "w") as f:
    json.dump(d, f, indent=4)

print("DONE")