code = """import json
import re

with open(locals()['var_function-call-8977914089601309835'], 'r') as f:
    docs = json.load(f)

projects_2022_mention = []

for doc in docs:
    text = doc['text']
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    
    i = 0
    while i < len(lines):
        line = lines[i]
        if i + 1 < len(lines) and lines[i+1].startswith('(cid:190)'):
            project_name = line
            project_block = []
            j = i + 1
            while j < len(lines):
                if j + 1 < len(lines) and lines[j+1].startswith('(cid:190)'):
                    break
                project_block.append(lines[j])
                j += 1
            full_text = " ".join(project_block)
            lower_text = full_text.lower()
            
            if "2022" in lower_text:
                 projects_2022_mention.append({"name": project_name, "text": full_text})
            
            i = j
        else:
            i += 1

print("__RESULT__:")
print(json.dumps(projects_2022_mention))"""

env_args = {'var_function-call-14070122848874409329': ['civic_docs'], 'var_function-call-2375620709415017457': ['Funding'], 'var_function-call-15365523151233485332': 'file_storage/function-call-15365523151233485332.json', 'var_function-call-8977914089601309835': 'file_storage/function-call-8977914089601309835.json', 'var_function-call-5412922098617405934': ['Bluffs Park Shade Structure'], 'var_function-call-11008207917599906957': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}], 'var_function-call-17472290710313514127': [{'name': 'Bluffs Park Shade Structure', 'text': '(cid:190) Updates: Construction was completed November 2022. Notice of completion filed January 2023 Page 4 of 6 Agenda Item # 4.B.'}, {'name': 'Broad Beach Road Water Quality Repair', 'text': '(cid:190) Updates: (cid:131) Construction was completed, November 2022 (cid:131) Notice of completion filed January 2023'}, {'name': 'Point Dume Walkway Repairs', 'text': '(cid:190) Updates: (cid:131) Construction was completed, November 2022 (cid:131) Notice of completion filed January 2023 Capital Improvement Projects (Not Started)'}], 'var_function-call-13481005743254189109': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '79', 'Project_Name': 'Point Dume Walkway Repairs', 'Funding_Source': 'International Aid', 'Amount': '59000'}]}

exec(code, env_args)
