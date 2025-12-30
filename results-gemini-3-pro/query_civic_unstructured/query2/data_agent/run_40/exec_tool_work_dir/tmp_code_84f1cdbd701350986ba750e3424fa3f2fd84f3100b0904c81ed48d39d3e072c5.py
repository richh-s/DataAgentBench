code = """import json
import re

civic_docs_key = locals()['var_function-call-13888598528909911574']
with open(civic_docs_key, 'r') as f:
    civic_docs = json.load(f)

print("Completed Projects Analysis:")

for doc in civic_docs:
    text = doc['text']
    lines = text.split(chr(10))
    for i, line in enumerate(lines):
        if 'Updates:' in line:
            name = ''
            for k in range(i-1, -1, -1):
                if lines[k].strip():
                    name = lines[k].strip()
                    break
            
            block_lines = []
            for j in range(i, len(lines)):
                if j > i and 'Updates:' in lines[j]:
                    break
                block_lines.append(lines[j])
            block_text = ' '.join(block_lines).lower()
            
            # Check Completed 2022
            completed_2022 = False
            if '2022' in block_text and 'completed' in block_text:
                if re.search('completed.{0,30}2022', block_text):
                    completed_2022 = True
            
            if completed_2022:
                print(f"Project: {name}")
                print(f"Block: {block_text[:200]}...")
                is_park = 'park' in name.lower() or 'playground' in name.lower() or 'recreation' in name.lower()
                print(f"Is Park: {is_park}")
                print("-" * 20)"""

env_args = {'var_function-call-18388695237617749918': ['civic_docs'], 'var_function-call-18388695237617747301': ['Funding'], 'var_function-call-18388695237617748780': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-18388695237617746163': 'file_storage/function-call-18388695237617746163.json', 'var_function-call-13888598528909911574': 'file_storage/function-call-13888598528909911574.json', 'var_function-call-13888598528909910147': 'file_storage/function-call-13888598528909910147.json', 'var_function-call-12370353349400384531': {'total': 80000, 'matches': [['Bluffs Park Shade Structure', 21000], ['Point Dume Walkway Repairs', 59000]]}}

exec(code, env_args)
