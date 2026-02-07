from google import genai
import json


def getLLM_evaluations():

    # set up a connection

    client = genai.Client(api_key="YOUR-API-KEY")

    ## Read the knowledge base
    with open("../tasks/knowledge_base.json") as f:
        file = json.load(f)


    # Here we focus only on query answering
    knowledge_base = file['KB']

    with open("../tasks/query_answering.json") as f:
        file = json.load(f)

    task_instructions = file['query_answering_task']

    with open("../results/ChatGPT-query_answering.txt", "r") as f:
        model_answers = f.read()


    response = client.models.generate_content(
        model="gemini-3-flash-preview", 
        # PROMPT
        contents=f"""
            ### Task Description:
                You are given a knowledge base written in OWL DL functional syntax, some queries performed on it, 
                together with the answers provided to each query, the reasoning steps that led to such answers, 
                and the reference answers (the correct ones) .
                Note: Your are not provided with the correct reasoning steps, just the final correct answer.

                Your task is to:
                1. Based on the reference answer and the knowledge base that is provided, evaluate, for each query, the reasoning steps
                   that led to the answer, according to the given evaluation criteria and scoring rubric.
                2. Output the result as follows:
                    Q1: (your short explanation) --- [SCORE] (a number from 1 to 5)
                    Q2: (your short explanation) --- [SCORE] (a number from 1 to 5)
                    Q3: (your short explanation) --- [SCORE] (a number from 1 to 5)
                    Q4: (your short explanation) --- [SCORE] (a number from 1 to 5)
                
            ### The knowledge base:
                {knowledge_base}

            ### The task instructions:
                {task_instructions} 

            ### Reasoning steps to eavluate:
                {model_answers}

            ### Reference Answer
                Q1: [Marco]
                Q2: [Alessio, Emanuela, Fabio, Francesca, Giulia, LarryPage, Marco, Matteo]
                Q3: []
                Q4: [Marco]

            ### Score Rubric:
                Score 1: The reasoning steps are wrong and the answer is wrong.
                Score 2: The reasoning steps are wrong but the answer is correct.
                Score 3: The reasoning steps are correct but not well logically formalized; the answer is correct.
                Score 4: The reasoning steps are correct and well logically formalized but could be more exhaustive; the answer is correct.
                Score 5: The reasoning steps are correct, well logically formalized and exhaustive; the answer is correct.

            ### Response: 
        """
    )
    print("LLM Response: ", response.text)

    with open("../eval_results/Gemini_evaluations_QA.txt", "w") as f:
        f.write(response.text)

    return 


getLLM_evaluations()
