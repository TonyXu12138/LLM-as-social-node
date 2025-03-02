from datasets import load_dataset
import torch
from tqdm import tqdm
import os
import json
import argparse
from utils import generate_template, answer_extraction
from math import ceil
from volcenginesdkarkruntime import Ark
# from utils import class_6_lst, law_6_lst, Fina_6_lst,med_6_lst
from role_description import class_6_lst,law_6_lst, Fina_6_lst,med_6_lst

def main(ds, domain,  group_name, group, resume = False):
    ds_domain = ds.filter(lambda x: x['category'] == domain)
    result_lst = []
    total_answer_lst = []
    correct = 0
    result_path = result_path_prefix + f'{domain}_{group_name}.json'
    answer_path = result_path_prefix + f'{domain}_{group_name}_answer.json'
    if resume == True:
        with open(result_path,'r') as f:
            pre_result = json.load(f)
            pre_result_len = len(pre_result)
            result_lst = pre_result
        with open(answer_path,'r') as f:
            total_answer_lst = json.load(f)
        ##resume from break point, recover index, correct and split data
        pre_data_index = pre_result_len*100
        correct = ceil(result_lst[-1]*pre_data_index)
        ds_domain = ds_domain.select(range(pre_data_index,len(ds_domain)))
    ###question preparation
    for question_id, row in tqdm(enumerate(ds_domain),total = len(ds_domain)):
        answer_lst = []
        question,options,label = row['question'],row['options'],row['answer_index']
        for option_id, option in enumerate(options):
            question += f'\n {option_id}: {option}'
        if (question_id+1) % 100 == 0:
            result_lst.append(correct/(question_id+1))
            with open(result_path, 'w') as f:
                json.dump(result_lst, f)
            with open(answer_path, 'w') as f:
                json.dump(total_answer_lst, f)
        for id, role in enumerate(group):
            message_hist = ''
            if len(answer_lst) == 0:
                message_hist = ''
            else:
                for ans_id,ans in enumerate(answer_lst):
                    if ans_id < len(answer_lst)-1:
                        message_hist+= f'The collaborator with role of {group[id][1]} and the responsibility of {group[id][2]} in your group answered: {ans["role_answer"]} \n'
                    else:
                        message_hist+= f'The collaborator with role of {group[id][1]} and the responsibility of {group[id][2]} in your group answered: {ans["role_answer"]} \n\
                            The rationale of the answer is {ans["agent_answer"]} \n'    
                                        
            messages = generate_template(role_resp_lst = group, message_hist = message_hist, turn = id, problem = question, mode = 'RR')
            output = client.chat.completions.create(
                                model="ep-20250227211204-2dsf9",
                                messages=messages,
                        )              
            if hasattr(output.choices[0].message, 'reasoning_content'):
                reasoning_steps = output.choices[0].message.reasoning_content
            else:
                reasoning_steps = 'No reasoning provided'
            role_answer = answer_extraction(output.choices[0].message.content)
            answer_dict = {'question':question,'agent_role':group[id][1],'agent_answer':output.choices[0].message.content,'agent_reasoning':reasoning_steps,'role_answer':role_answer}
            answer_lst.append(answer_dict)
            # message_hist += f'The collaborator with role of {group[id][1]} and the responsibility of {group[id][2]} in your group answered: {role_answer} \n' ###############
        total_answer_lst.append(answer_lst)
        if str(label) == role_answer:
            correct += 1
    result_lst.append(correct/len(ds_domain))
    with open(result_path, 'w') as f:
        json.dump(result_lst, f)
    with open(answer_path, 'w') as f:
        json.dump(total_answer_lst, f)
    print(f'{domain} {id} done')
    
    
group_lst = [class_6_lst,law_6_lst, Fina_6_lst,med_6_lst]
group_str_lst = ['class','law','Fina','Med']
group_dict = dict(zip(group_str_lst,group_lst))
domain_lst = ['math','law','finance','health','other'] #'engineering'
domain_lst = ['math']
result_path_prefix = './result/MMLU_Pro_Llama_r1_8b/'
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
ds = load_dataset("TIGER-Lab/MMLU-Pro")['test']
client = Ark(
    api_key=os.environ.get("ARK_API_KEY"), 
    timeout=1800,
    )
###qwen-7b


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    # Add arguments
    parser.add_argument("--domain", type=str, help="domain name",choices=['math','law','finance','health','other'], required=True)
    parser.add_argument("--group", type=str, help="group name",choices=['class','law','Fina','Med'], required=True)
    parser.add_argument("--resume", type=bool, help="resume from break point", default = False)
    # Parse arguments
    args = parser.parse_args()
    
    main(ds, args.domain, args.group, group_dict[args.group],args.resume)