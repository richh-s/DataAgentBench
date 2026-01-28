code = """import json
import pandas as pd

path_civic = locals()['var_function-call-16246873831533624735']
path_funding = locals()['var_function-call-7325626147316931914']

with open(path_civic, 'r') as f:
    civic_docs = json.load(f)
    
with open(path_funding, 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
project_names = df_funding['Project_Name'].unique().tolist()
project_names.sort(key=len, reverse=True)

projects_started_spring_2022 = set()

spring_tokens = [
    "spring 2022", "2022-spring", "spring, 2022",
    "march 2022", "april 2022", "may 2022",
    "03/2022", "04/2022", "05/2022",
    "03-2022", "04-2022", "05-2022",
    "2022-03", "2022-04", "2022-05",
    "march, 2022", "april, 2022", "may, 2022"
]

for doc in civic_docs:
    text = doc['text']
    occurrences = []
    for name in project_names:
        start = 0
        while True:
            idx = text.find(name, start)
            if idx == -1:
                break
            occurrences.append((idx, name))
            start = idx + len(name)
            
    occurrences.sort(key=lambda x: (x[0], -len(x[1])))
    
    final_occurrences = []
    last_end = -1
    for occ in occurrences:
        start, name = occ
        end = start + len(name)
        if start >= last_end:
            final_occurrences.append(occ)
            last_end = end
    
    for i in range(len(final_occurrences)):
        idx, name = final_occurrences[i]
        
        if i < len(final_occurrences) - 1:
            next_idx = final_occurrences[i+1][0]
        else:
            next_idx = len(text)
            
        segment = text[idx+len(name):next_idx]
        seg_lines = segment.splitlines()
        
        found = False
        for line in seg_lines:
            line_lower = line.lower()
            if "begin construction" in line_lower or "start date" in line_lower:
                for token in spring_tokens:
                    if token in line_lower:
                        projects_started_spring_2022.add(name)
                        found = True
                        break
            if found:
                break

matched_projects = []
total_funding = 0
for index, row in df_funding.iterrows():
    f_name = row['Project_Name'].strip()
    if f_name in projects_started_spring_2022:
        matched_projects.append(f_name)
        total_funding += int(row['Amount'])

result = {
    "count": len(matched_projects),
    "total_funding": total_funding,
    "projects": matched_projects
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-16246873831533624735': 'file_storage/function-call-16246873831533624735.json', 'var_function-call-7325626147316931914': 'file_storage/function-call-7325626147316931914.json', 'var_function-call-15565346498784014435': {'count': 0, 'total_funding': 0, 'projects': []}, 'var_function-call-13755215421253914261': 'debug done', 'var_function-call-16513209548295068093': {'projects_count': 268, 'spring_hits_in_docs': 4, 'dates_found_sample': [{'project': 'project and will submit to the County for review.', 'line': '(cid:131) Begin Construction: Fall 2023'}, {'project': 'or phasing out the project', 'line': '(cid:131) Begin Construction: Fall 2023'}, {'project': '(cid:131) City working with consultant on the design of the shoulder repairs', 'line': '(cid:131) Begin Construction: Fall 2023'}, {'project': 'cleared the project.', 'line': '(cid:131) Begin Construction: Fall 2023'}, {'project': 'to finalize plans and specifications', 'line': '(cid:131) Begin Construction: Fall 2023'}, {'project': '(cid:131) Awaiting final FEMA/CalOES approval for scope modification', 'line': '(cid:131) Begin Construction: Summer 2023'}, {'project': '(cid:131) Plans and specifications are being finalized by consultant', 'line': '(cid:131) Begin Construction: Summer 2023'}, {'project': 'project', 'line': '(cid:131) Begin Construction: Winter 2024'}, {'project': 'the Spring 2023.', 'line': '(cid:131) Begin Construction: Fall 2023'}, {'project': 'Engineering, Inc.', 'line': '(cid:131) Begin construction: April 2023'}], 'advertise_sample': [{'project': 'project and will submit to the County for review.', 'line': '(cid:131) Advertise: Fall 2023'}, {'project': 'or phasing out the project', 'line': '(cid:131) Advertise: Fall 2023'}, {'project': '(cid:131) City working with consultant on the design of the shoulder repairs', 'line': '(cid:131) Advertise: Summer 2023'}, {'project': 'cleared the project.', 'line': '(cid:131) Advertise: Summer 2023'}, {'project': 'to finalize plans and specifications', 'line': '(cid:131) Advertise: Summer 2023'}]}}

exec(code, env_args)
