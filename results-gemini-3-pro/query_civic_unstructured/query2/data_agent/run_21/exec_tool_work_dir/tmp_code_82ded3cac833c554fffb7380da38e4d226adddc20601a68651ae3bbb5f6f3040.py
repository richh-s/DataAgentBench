code = """import json
import re

funding_path = locals()['var_function-call-2809487722948638107']
civic_docs_path = locals()['var_function-call-2809487722948637720']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

project_names = set(item['Project_Name'] for item in funding_data)
sorted_project_names = sorted(list(project_names), key=len, reverse=True)

# Strict completion regex
completion_pattern = re.compile(r'(construction was completed|construction completed|project completed|project was completed|notice of completion).*?2022', re.IGNORECASE | re.DOTALL)

completed_candidates = set()
candidate_segments = {}

for doc in civic_docs:
    text = doc['text']
    
    found_projects = []
    for name in sorted_project_names:
        start = 0
        while True:
            idx = text.find(name, start)
            if idx == -1: break
            found_projects.append((idx, name))
            start = idx + len(name)
    found_projects.sort(key=lambda x: x[0])
    
    for i in range(len(found_projects)):
        start_idx, name = found_projects[i]
        if i + 1 < len(found_projects):
            end_idx = found_projects[i+1][0]
        else:
            end_idx = len(text)
        segment = text[start_idx:end_idx]
        
        if completion_pattern.search(segment):
             completed_candidates.add(name)
             candidate_segments[name] = segment[:300] # Store preview

# Now check if they are park related
results = []
for name in completed_candidates:
    # Check name
    is_park = False
    lower_name = name.lower()
    if 'park' in lower_name or 'playground' in lower_name or 'recreation' in lower_name:
        is_park = True
    else:
        # Check segment for keywords
        seg = candidate_segments[name].lower()
        if 'park' in seg or 'playground' in seg:
            is_park = True
            
    if is_park:
        results.append(name)
    else:
        # Print non-park completed projects to verify I'm not missing anything obvious
        print(f"Non-park completed project: {name}")

# Sum
total = 0
details = []
for p in results:
    recs = [r for r in funding_data if r['Project_Name'] == p]
    p_total = sum(int(r['Amount']) for r in recs)
    total += p_total
    details.append({"name": p, "amount": p_total})

print("__RESULT__:")
print(json.dumps({"total_funding": total, "projects": details}))"""

env_args = {'var_function-call-2809487722948638107': 'file_storage/function-call-2809487722948638107.json', 'var_function-call-2809487722948637720': 'file_storage/function-call-2809487722948637720.json', 'var_function-call-2577172791415288121': {'total_funding': 118000, 'projects': [{'name': 'Permanent Skate Park', 'amount': 97000}, {'name': 'Bluffs Park Shade Structure', 'amount': 21000}]}, 'var_function-call-4627848368768369547': [{'project': 'Permanent Skate Park', 'segment': 'Permanent Skate Park\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2023\n(cid:131) Begin Construction: Winter 2024\n\n'}, {'project': 'Bluffs Park Shade Structure', 'segment': 'Bluffs Park Shade Structure\n\n(cid:190) Updates: Construction was completed November 2022. Notice of completion\n\nfiled January 2023\n\nPage 4 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\n'}, {'project': 'Bluffs Park Shade Structure', 'segment': 'Bluffs Park Shade Structure\n\n(cid:190) Project Description: This project consists of the installation of four single-post\n\nshade structures at Malibu Bluffs Park.\n\n(cid:190) Updates:\n\n(cid:131) Staff is currently working on the design of the project and anticipates\n\nsending this project out to bid during the Spring of 2022.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Spring 2022\n\n'}, {'project': 'Permanent Skate Park', 'segment': 'Permanent Skate Park\n\n(cid:190) Project Description: This project includes the designing and constructing a\npermanent skate park located on the Crummer/Case Court parcel adjacent\nto Malibu Bluffs Park. The project would include parking and additional site\namenities such as trash cans, benches, tables, and restrooms.\n\n(cid:190) Updates:\n(cid:131)\n\nIn May 2021, the Council approved funding for additional engineering\nwork related to the project. Staff has worked with the consultant over\nthe past several months to complete the engineering work, and the final\ndraft plans are expected to be completed in early 2022. The Planning\nCommission will then review the project in Spring 2022 before final\nreview by the Council.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: To be determined\n\n'}, {'project': 'Bluffs Park Shade Structure', 'segment': 'Bluffs Park Shade Structure\n\n(cid:190) Project Description: This project consists of the installation of four single-\n\npost shade structures at Malibu Bluffs Park\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Summer 2021\n(cid:131) Begin Construction: Fall 2021\n\n'}, {'project': 'Bluffs Park Shade Structure', 'segment': 'Bluffs Park Shade Structure\n\n(cid:190) Project Description: This project consists of the installation of four single-\n\npost shade structures at Malibu Bluffs Park\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Summer 2021\n(cid:131) Begin Construction: Fall 2021\n\n'}, {'project': 'Bluffs Park Shade Structure', 'segment': 'Bluffs Park Shade Structure\n\n(cid:190) Project Description: This project consists of the installation of four single-post\n\nshade structures at Malibu Bluffs Park.\n\n(cid:190) Updates:\n\n(cid:131) Staff received bids on February 24, 2022. Award of contract is\n\nscheduled for the April 11, 2022 Council meeting.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: February 2022\n(cid:131) Begin Construction: Spring 2022\n\n'}, {'project': 'Permanent Skate Park', 'segment': 'Permanent Skate Park\n\n(cid:190) Project Description: This project includes designing and constructing a\npermanent skate park located on the Crummer/Case Court parcel adjacent\nto Malibu Bluffs Park. The project would include parking and additional site\namenities such as trash cans, benches, tables, and restrooms.\n\n(cid:190) Updates:\n(cid:131)\n\nIn May 2021, the Council approved funding for additional engineering\nwork related to the project. Staff has worked with the consultant over\nthe past several months to complete the engineering work, and the final\ndraft plans are expected to be completed in early 2022. The Planning\nCommission will then review the project in Spring 2022 before final\nreview by the Council.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: To be determined\n\nPage 3 of 8\n\nAgenda Item # 4.A.\n\n\n\n\n\n\n\n\n\n'}], 'var_function-call-320445436804476579': {'total_funding': 21000, 'projects': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000}]}}

exec(code, env_args)
