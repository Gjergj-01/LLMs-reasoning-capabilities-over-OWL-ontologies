import json 

''' 
In this file I generate a new ontology where intead of "Employee", "Company", "worksIn" etc, 
we have only characters such as "A", "B", "C", ..., for concepts and "p1", "p2", ... for properties. 
'''

knowledge_base = """
Declaration(Class( :A))
Declaration(Class( :B))
Declaration(Class( :C))
Declaration(Class( :D))
Declaration(Class( :E))
Declaration(Class( :F))
Declaration(Class( :G))
Declaration(Class( :H))
Declaration(Class( :I))
Declaration(Class( :K))
Declaration(Class( :L))
Declaration(Class( :M))
Declaration(Class( :N))

Declaration(ObjectProperty( :P1))
Declaration(ObjectProperty( :P2))
Declaration(ObjectProperty( :P3))
Declaration(ObjectProperty( :P4))
Declaration(ObjectProperty( :P5))
Declaration(ObjectProperty( :P6))
Declaration(ObjectProperty( :P7))
Declaration(ObjectProperty( :P8))
Declaration(ObjectProperty( :P9))
Declaration(ObjectProperty( :P10))
Declaration(ObjectProperty( :P11))
Declaration(ObjectProperty( :P12))
Declaration(ObjectProperty( :P13))

SubClassOf( :B :A)
SubClassOf( :H :A)
SubClassOf( :C :B)
SubClassOf( :D :B)

DisjointClasses( :A :K)
DisjointClasses( :A :E)
DisjointClasses( :A :F)
DisjointClasses( :A :L)
DisjointClasses( :A :G)
DisjointClasses( :A :I)
DisjointClasses( :A :M)
DisjointClasses( :A :N)
DisjointClasses( :K :E)
DisjointClasses( :K :F)
DisjointClasses( :K :L)
DisjointClasses( :K :G)
DisjointClasses( :K :I)
DisjointClasses( :K :M)
DisjointClasses( :K :N)
DisjointClasses( :E :F)
DisjointClasses( :E :L)
DisjointClasses( :E :G)
DisjointClasses( :E :I)
DisjointClasses( :E :M)
DisjointClasses( :E :N)
DisjointClasses( :F :L)
DisjointClasses( :F :G)
DisjointClasses( :F :I)
DisjointClasses( :F :M)
DisjointClasses( :F :N)
DisjointClasses( :L :G)
DisjointClasses( :L :I)
DisjointClasses( :L :M)
DisjointClasses( :L :N)
DisjointClasses( :G :I)
DisjointClasses( :G :M)
DisjointClasses( :G :N)
DisjointClasses( :I :M)
DisjointClasses( :I :N)
DisjointClasses( :M :N)


ObjectPropertyDomain( :P1 :A)
ObjectPropertyRange( :P1 :F)

ObjectPropertyDomain( :P2 :C)
ObjectPropertyRange( :P2 :E)

ObjectPropertyDomain( :P3 :E)
ObjectPropertyRange( :P3 :A)

ObjectPropertyDomain( :P4 :D)
ObjectPropertyRange( :P4 :F)

ObjectPropertyDomain( :P5 :F)
ObjectPropertyRange( :P5 :G)

ObjectPropertyDomain( :P6 :G)
ObjectPropertyRange( :P6 :H)

ObjectPropertyDomain( :P7 :I)
ObjectPropertyRange( :P7 :G)

ObjectPropertyDomain( :P8 :H)
ObjectPropertyRange( :P8 :I)

ObjectPropertyDomain( :P10 :A)
ObjectPropertyRange( :P10 :K)

ObjectPropertyDomain( :P11 :F)
ObjectPropertyRange( :P11 :L)

ObjectPropertyDomain( :P12 :I)
ObjectPropertyRange( :P12 :M)

ObjectPropertyDomain( :P13 :M)
ObjectPropertyRange( :P13 :N)

SubObjectPropertyOf( :P9 :P8)


ClassAssertion( :A :a1)
ClassAssertion( :A :a2)
ClassAssertion( :C :b1)
ClassAssertion( :C :c1)
ClassAssertion( :D :d1)
ClassAssertion( :D :d2)
ClassAssertion( :E :e1)
ClassAssertion( :F :f1)
ClassAssertion( :F :f2)
ClassAssertion( :G :g1)
ClassAssertion( :G :g2)
ClassAssertion( :H :h1)
ClassAssertion( :H :h2)
ClassAssertion( :I :i1)
ClassAssertion( :I :i2)
ClassAssertion( :L :l1)
ClassAssertion( :M :m1)
ClassAssertion( :N :n1)
ClassAssertion( :K :k1)
ClassAssertion( :K :k2)

ObjectPropertyAssertion( :P1 :a1 :f2)
ObjectPropertyAssertion( :P1 :a2 :w)
ObjectPropertyAssertion( :P1 :z :w)
ObjectPropertyAssertion( :P1 :r1 :z2)

ObjectPropertyAssertion( :P2 :b1 :e1)
ObjectPropertyAssertion( :P2 :z :e2)

ObjectPropertyAssertion( :P3 :e1 :y1)
ObjectPropertyAssertion( :P3 :e1 :a2)
ObjectPropertyAssertion( :P3 :e2 :y)

ObjectPropertyAssertion( :P4 :d1 :o)
ObjectPropertyAssertion( :P4 :s1 :f1)
ObjectPropertyAssertion( :P4 :s2 :f2)

ObjectPropertyAssertion( :P5 :w :j1)
ObjectPropertyAssertion( :P5 :f2 :g2)
ObjectPropertyAssertion( :P5 :f2 :j2)

ObjectPropertyAssertion( :P6 :j1 :h2)
ObjectPropertyAssertion( :P6 :j :r1)
ObjectPropertyAssertion( :P6 :g2 :q)

ObjectPropertyAssertion( :P7 :i1 :g1)
ObjectPropertyAssertion( :P7 :i2 :j)
ObjectPropertyAssertion( :P7 :ca :j2)

ObjectPropertyAssertion( :P8 :r2 :i1)
ObjectPropertyAssertion( :P8 :q :ca)
ObjectPropertyAssertion( :P8 :h1 :a3)

ObjectPropertyAssertion( :P9 :r3 :w2)
ObjectPropertyAssertion( :P9 :h2 :i2)

ObjectPropertyAssertion( :P10 :k3 :k1)
ObjectPropertyAssertion( :P10 :z :k2)

ObjectPropertyAssertion( :P11 :z2 :l1)
ObjectPropertyAssertion( :P11 :w :z3)

ObjectPropertyAssertion( :P12 :m3 :m1)
ObjectPropertyAssertion( :P12 :i2 :m2)
ObjectPropertyAssertion( :P12 :i2 :n2)

ObjectPropertyAssertion( :P13 :n2 :n1)

"""


d = {"KB": knowledge_base}
with open("tasks/char_knowledge_base.json", "w") as f:
    json.dump(d, f)


##################
#  QUERY ANSWERING
##################

query_answering_task = """
Given the knowledge base that is provided, you are asked to answer the following queries (expressed in Manchester OWL syntax):
- Q1: C and P1 some (P11 value z3) and P2 some (P3 value y) and P10 value k2
- Q2: I and P12 some (P13 value n1) and P7 some (P6 some (P1 some (P11 value l1)))
- Q3: A (In natural language: return all instances of class A)

showing for each of them in detail the reasoning steps that led to the answers.
"""

query_answering_format = """
Structure your response as follows: 
Q1: (your reasoning steps) --- [answer].
Q2: (your reasoning steps) --- [answer].
Q3: (your reasoning steps) --- [answer].
Notice that the sequence "---" must be unique (and must always be present) in the response of each query, as it will be used as separator for the answer.
"""

d = {"query_answering_task": query_answering_task, "query_answering_format": query_answering_format}

## save the query answer task instructions
with open("tasks/char_query_answering.json", "w") as f:
    json.dump(d, f, indent=4)


######################
# CONSISTENCY CHECKING
######################

inconsistent_KB = knowledge_base + "\nClassAssertion( :A :r3)"

consistency_checking_task = """
Given the knowledge base that is provided, your task is to tell whether it is consistent or not.
Explain in detail the reasoning steps that led to your answer (which must be YES or NO).
"""

consistency_checking_format = """
Structure your response as follows:
(your reasoning steps) --- [answer]
Notice that the sequence "---" must be unique (and always present) in the response, as it will be used as separator for the answer.
"""

d = {"KB": inconsistent_KB, "consistency_checking_task": consistency_checking_task, "consistency_checking_format": consistency_checking_format}

## save the inconsistency checking task instructions
with open("tasks/char_inconsistency_checking.json", "w") as f:
    json.dump(d, f, indent=4)



####################
# INSTANCE CHECKING
####################

instance_checking_task = """
Given the knowledge base that is provided, your task is to tell whether the following assertions hold:
A1: ClassAssertion( :A :z)
A2: ObjectPropertyAssertion( :P8 :r1 :i2)

showing for each of them in detail the reasoning steps that led to the answers (which must be YES or NO).
"""

instance_checking_format = """
Structure your response as follows:
A1: (your reasoning steps) --- [answer]
A2: (your reasoning steps) --- [answer]

Notice that the sequence "---" must be unique (and must always be present) in the response for each, as it will be used as separator for the answer.
"""

d = {"instance_checking_task": instance_checking_task, "instance_checking_format": instance_checking_format}

## save the instance checking task instructions
with open("tasks/char_instance_checking.json", "w") as f:
    json.dump(d, f, indent=4)

print("DONE")