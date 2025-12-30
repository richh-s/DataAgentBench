code = """import json
import re

funding_path = locals()['var_function-call-2978529979761584874']
civic_path = locals()['var_function-call-18353548758763023349']

funding_data = json.load(open(funding_path))
civic_docs = json.load(open(civic_path))

newline = chr(10)
full_text = newline.join([doc['text'] for doc in civic_docs])
lines = [line.strip() for line in full_text.split(newline) if line.strip()]

projects = []
current_project = {}

for i, line in enumerate(lines):
    if line.startswith("(cid:190)") or line.startswith("Updates:") or line.startswith("Project Description:"):
        if i > 0:
            potential_name = lines[i-1]
            if not (potential_name.startswith("(cid:190)") or potential_name.startswith("Updates:") or potential_name.startswith("Project Description:")):
                if current_project and current_project.get('name') != potential_name:
                    projects.append(current_project)
                    current_project = {}
                if not current_project:
                    current_project = {"name": potential_name, "text_block": ""}
    
    if current_project:
        current_project["text_block"] += line + newline

if current_project:
    projects.append(current_project)

# Print summary of all projects found
summary = []
for p in projects:
    name = p["name"]
    text = p["text_block"].lower()
    
    # Extract dates/status
    dates = re.findall(r"(completed|construction|design|advertise|begin).*?(\d{4})", text)
    
    is_park = "park" in name.lower() or "park" in text or "playground" in name.lower()
    
    summary.append({
        "name": name,
        "is_park": is_park,
        "dates_found": dates[:5], # Limit
        "snippet": text[:100]
    })

print("__RESULT__:")
print(json.dumps(summary))"""

env_args = {'var_function-call-2978529979761584874': 'file_storage/function-call-2978529979761584874.json', 'var_function-call-18353548758763023349': 'file_storage/function-call-18353548758763023349.json', 'var_function-call-17154176344544213090': {'total_funding': 214000, 'matched_projects': [{'name': 'Marie Canyon Green Streets', 'amount': '50000', 'extracted_name': 'Marie Canyon Green Streets'}, {'name': 'Birdview Avenue Improvements', 'amount': '79000', 'extracted_name': 'Birdview Avenue Improvements (CalOES Project)'}, {'name': 'Birdview Avenue Improvements (CalOES Project)', 'amount': '85000', 'extracted_name': 'Birdview Avenue Improvements (CalOES Project)'}], 'extracted_park_projects': ['Marie Canyon Green Streets', 'Metro.', 'Birdview Avenue Improvements (CalOES Project)', '(cid:190) Updates: Project is currently under construction']}, 'var_function-call-6018647821410521570': {'total_funding': 21000, 'matched_projects': [{'name': 'Bluffs Park Shade Structure', 'amount': '21000', 'extracted_name': 'Bluffs Park Shade Structure'}], 'extracted_park_projects': ['Bluffs Park Shade Structure']}}

exec(code, env_args)
