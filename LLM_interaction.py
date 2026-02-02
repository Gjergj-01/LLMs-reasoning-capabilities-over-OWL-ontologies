from google import genai
import json

tasks = ["query_answering", "inconsistency_checking", "instance_checking"]

def getLLM_feedback():

    # set up a connection

    client = genai.Client(api_key="YOUR-API-KEY")

    ## Read the knowledge base
    with open("tasks/knowledge_base.json") as f:
        file = json.load(f)
    
    knowledge_base = file['KB']

    ## Read the json files containing the instructions for the LLM

    with open("tasks/query_answering.json") as f:
        query_answering_task = json.load(f)

    with open("tasks/instance_checking.json") as f:
        instance_checking_task = json.load(f)

    with open("tasks/inconsistency_checking.json") as f:
        inconsistency_checking_task = json.load(f)

    ## For each task, we retrieve the answers from the LLM

    for task in tasks:

        task_instructions = ''
        output_format = ''

        if task == "query_answering": 
            task_instructions = query_answering_task['query_answering_task']
            output_format = query_answering_task['query_answering_format']

        elif task == "inconsistency_checking":
            task_instructions = inconsistency_checking_task['inconsistency_checking_task']
            output_format = inconsistency_checking_task['inconsistency_checking_format']

        else:
            task_instructions = instance_checking_task['instance_checking_task']
            output_format = instance_checking_task['instance_checking_format']

        prompt=f"""
            ### Task Description:
                You are given a knowledge base written in OWL DL functional syntax and a task to perform on it, together with some instructions on how to format your output.

            ### The knowledge base:
                {knowledge_base}

            ### The task:
                {task_instructions} 

            ### The format of your answer:
                {output_format}

            ### Response: 
        """

        print(f'Task: {task}\n Prompt: \n{prompt} \n\n')

        #response = client.models.generate_content(
        #    model="gemini-3-flash-preview", 
        #    # PROMPT
        #    contents=f"""
        #        ### Task Description:
        #            You are given a knowledge base written in OWL DL functional syntax and a task to perform on it, together with some instructions on how to format your output.
#
        #        ### The knowledge base:
        #            {knowledge_base}
#
        #        ### The task:
        #            {task_instructions} 
#
        #        ### The format of your answer:
        #            {output_format}
#
        #        ### Response: 
        #    """
        #)
    #print(f'Task: {task} \n {response.contents}\n\n')
    #print(response.text)


getLLM_feedback()