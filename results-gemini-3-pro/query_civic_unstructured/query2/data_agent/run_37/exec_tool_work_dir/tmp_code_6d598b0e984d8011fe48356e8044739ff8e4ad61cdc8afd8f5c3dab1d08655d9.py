code = """import json
import re

docs = json.load(open(locals()['var_function-call-10596372274131674166']))

candidates = []

for doc in docs:
    text = doc['text']
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    
    # Simple iteration to find blocks
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.startswith('(cid:190)') and 'Updates:' not in line:
            if i + 1 < len(lines) and lines[i+1].startswith('(cid:190)'):
                project_name = line
                project_text = ""
                i += 1
                while i < len(lines):
                    if not lines[i].startswith('(cid:190)') and \
                       (i + 1 < len(lines) and lines[i+1].startswith('(cid:190)')):
                        break
                    project_text += lines[i] + " "
                    i += 1
                
                # Check criteria
                is_park = False
                if 'park' in project_name.lower() or 'playground' in project_name.lower() or 'recreation' in project_name.lower():
                    is_park = True
                
                # Check for "completed" and "2022"
                # using simple string check first
                is_completed_2022 = False
                if '2022' in project_text and 'completed' in project_text.lower():
                     # Verify closely
                     if re.search(r'completed,?\s+(?:in\s+)?([A-Za-z]+)\s+2022', project_text, re.IGNORECASE) or \
                        re.search(r'Complete Construction:\s+([A-Za-z]+)\s+2022', project_text, re.IGNORECASE) or \
                        re.search(r'Construction completed\s+([A-Za-z]+)\s+2022', project_text, re.IGNORECASE):
                        is_completed_2022 = True
                
                if is_park and is_completed_2022:
                    candidates.append(project_name)
        i += 1

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-15461874300401161107': ['civic_docs'], 'var_function-call-15461874300401161542': ['Funding'], 'var_function-call-10596372274131677177': 'file_storage/function-call-10596372274131677177.json', 'var_function-call-10596372274131674166': 'file_storage/function-call-10596372274131674166.json', 'var_function-call-14690968047652835103': {'total_funding': 21000, 'projects': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000}]}, 'var_function-call-8365704528830104402': [{'name': 'Bluffs Park Shade Structure', 'text': '(cid:190) Updates: Construction was completed November 2022. Notice of completion filed January 2023 Page 4 of 6 Agenda Item # 4.B. '}, {'name': 'Broad Beach Road Water Quality Repair', 'text': '(cid:190) Updates: (cid:131) Construction was completed, November 2022 (cid:131) Notice of completion filed January 2023 '}, {'name': 'Point Dume Walkway Repairs', 'text': '(cid:190) Updates: (cid:131) Construction was completed, November 2022 (cid:131) Notice of completion filed January 2023 Capital Improvement Projects (Not Started) '}, {'name': 'amenities such as trash cans, benches, tables, and restrooms.', 'text': '(cid:190) Updates: (cid:131) In May 2021, the Council approved funding for additional engineering work related to the project. Staff has worked with the consultant over the past several months to comp'}, {'name': 'amenities such as trash cans, benches, tables, and restrooms.', 'text': '(cid:190) Updates: (cid:131) In May 2021, the Council approved funding for additional engineering work related to the project. Staff has worked with the consultant over the past several months to comp'}], 'var_function-call-14709870099802064251': [{'name': 'Bluffs Park Shade Structure', 'amount': '21000'}, {'name': 'Point Dume Walkway Repairs', 'amount': '59000'}], 'var_function-call-16223230875150387963': ['Legacy Park Paver Repair Project ||  || (cid:190) Project Description: This project will consist of removing and repairing a large || section of pavers in Legacy Park. The pavers have become uneven and || damaged in several areas ||  || Malibu Bluffs Park South Walkway ||  || (cid:190) Project Description: This project will include replacing the existing sidewalk ||  || located on the south side of Malibu Bluffs Park. ||  || Trancas Playground Resurfacing ||  || (cid:190) Project Description: The project will include removing and replacing the upper', 'section of pavers in Legacy Park. The pavers have become uneven and || damaged in several areas ||  || Malibu Bluffs Park South Walkway ||  || (cid:190) Project Description: This project will include replacing the existing sidewalk ||  || located on the south side of Malibu Bluffs Park. ||  || Trancas Playground Resurfacing ||  || (cid:190) Project Description: The project will include removing and replacing the upper ||  || layer of the playground surfacing at Trancas Canyon Park. || ', 'Legacy Park Paver Repair Project ||  || (cid:190) Project Description: This project will consist of removing and repairing a large || section of pavers in Legacy Park. The pavers have become uneven and || damaged in several areas ||  || Malibu Bluffs Park South Walkway ||  || (cid:190) Project Description: This project will include replacing the existing sidewalk ||  || located on the south side of Malibu Bluffs Park. ||  || Trancas Playground Resurfacing ||  || (cid:190) Project Description: The project will include removing and replacing the upper', 'section of pavers in Legacy Park. The pavers have become uneven and || damaged in several areas ||  || Malibu Bluffs Park South Walkway ||  || (cid:190) Project Description: This project will include replacing the existing sidewalk ||  || located on the south side of Malibu Bluffs Park. ||  || Trancas Playground Resurfacing ||  || (cid:190) Project Description: The project will include removing and replacing the upper ||  || layer of the playground surfacing at Trancas Canyon Park. || ']}

exec(code, env_args)
