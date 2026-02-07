import json


tasks = ["query_answering", "inconsistency_checking", "instance_checking"]

def generate_ChatGPT_prompts():
     ## Read the knowledge base
    with open("tasks/knowledge_base.json") as f:
        file = json.load(f)

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
        knowledge_base = file['KB']

        if task == "query_answering": 
            task_instructions = query_answering_task['query_answering_task']
            output_format = query_answering_task['query_answering_format']
            knowledge_base = file['KB']

        elif task == "inconsistency_checking":
            task_instructions = inconsistency_checking_task['inconsistency_checking_task']
            output_format = inconsistency_checking_task['inconsistency_checking_format']
            knowledge_base = inconsistency_checking_task['KB']

        else:
            task_instructions = instance_checking_task['instance_checking_task']
            output_format = instance_checking_task['instance_checking_format']
            knowledge_base = file['KB']


        prompt=f"""
            ### Task Description:
                You are given a knowledge base written in OWL DL functional syntax and a task to perform on it, together with some instructions on how to format your output.

            ### The knowledge base:
                {knowledge_base}

            ### The task instructions:
                {task_instructions} 

            ### The format of your answer:
                {output_format}

            ### Response: 
        """

        path = "GPT_prompts/" + task + ".txt"
        with open(path, "w") as f:
            f.write(prompt)


    return 

generate_ChatGPT_prompts()