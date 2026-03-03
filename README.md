### Testing LLMs reasoning capabilities over OWL DL ontologies
This is a project done in the context of the Knowledge Representation and Semantic Technologies course with the aim of comparing the reasoning capabilities of LLMs over OWL ontologies against [Protégé](https://protege.stanford.edu). 

The idea of the project is that of testing **ChatGPT-5.2** and **Google gemini-3-flash-preview** in the following three tasks:
- Query answering
- Instance checking 
- Consistency checking

and then compare the results with **Protégé**.

We do so considering two different ontologies: 
1. Representing a typical company scenario with **classes** as *Employee*, *Recruiter*, *Job* etc. and **properties** as *wroksIn*, *applies*, *hires* and so on. In other words we have an onotlogy with meaningful classes and properties. This onotlogy is implemented in the `StaffManagement.rdf` file. 
2. Then we consider the "*Charachter Onotlogy*" (implemented in the file `Character_ontology.rdf`) where classes and properties have no meaning but are simple letters.

The idea here is to test whether LLMs are **Symbolic Reasoners** or they reasoning is mainly driven by thei natural language understanding.