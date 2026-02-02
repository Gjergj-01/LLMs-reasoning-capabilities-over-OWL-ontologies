from google import genai
import json
import re

def retrieve_result(text, task):

    '''
    Auxiliary function for organizing and cleaning the result
    '''

    text = text.strip()

    if task == "query_answering":
        groups = re.split('Q', text)

        results = {}
        i = 1
        for elem in groups:
            if len(elem) < 2:
                # skip groups containing only special characters
                continue

            reasoning_steps, answer = elem.split('---')
            key = 'Q' + str(i)
            results[key] = {'reasoning_steps': reasoning_steps.split(':')[1].strip(), 'answer': answer.strip()}

            i += 1

        return results
        
    elif task == "inconsistency_checking":
        reasoning_steps, answer = text.split('---')
        results = {'reasoning_steps': reasoning_steps.strip(), 'answer': answer.strip()}

        return results


    elif task == "instance_checking":
        groups = re.split('A', text)

        results = {}
        i = 1
        for elem in groups:
            if len(elem) < 2:
                continue

            reasoning_steps, answer = elem.split('---')
            key = 'A' + str(i)
            results[key] = {'reasoning_steps': reasoning_steps.split(':')[1].strip(), 'answer': answer.strip()}

            i += 1
        
        return results

    else:
        raise Exception("No task found!!")
    



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


        response = client.models.generate_content(
            model="gemini-3-flash-preview", 
            # PROMPT
            contents=f"""
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
        )
        print("LLM Response: ", response.text)


        # save raw feedback

        feedback = {task: response.text}
        with open("results/gemini_raw_feedback.jsonl", "a") as f:
            f.write(json.dumps(feedback, indent=2) + '\n')

        organized_output = retrieve_result(response.text, task)

        # save the cleaned output
        path = "results/gemini_" + task + ".json"

        with open(path, 'w') as f:
            json.dump(organized_output, f, indent=4)



getLLM_feedback()

