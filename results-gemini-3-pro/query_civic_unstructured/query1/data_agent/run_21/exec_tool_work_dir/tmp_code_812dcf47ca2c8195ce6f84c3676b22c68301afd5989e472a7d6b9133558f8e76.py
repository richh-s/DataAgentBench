code = """import json
import re

# Load funding data
with open(locals()['var_function-call-9362456295631069052']) as f:
    funding_data = json.load(f)

high_funding_projects = {item['Project_Name'] for item in funding_data}
print(f"DEBUG: High funding projects count: {len(high_funding_projects)}")
# print(f"DEBUG: Sample high funding: {list(high_funding_projects)[:5]}")

# Load civic docs
with open(locals()['var_function-call-12811906272455444713']) as f:
    docs = json.load(f)

matched_projects = set()
header_count = 0

for doc in docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    norm_text = re.sub(r'\s+', ' ', text)
    header = "Capital Improvement Projects (Design)"
    
    start_indices = [m.start() for m in re.finditer(re.escape(header), norm_text, re.IGNORECASE)]
    
    for start_idx in start_indices:
        header_count += 1
        content_start = start_idx + len(header)
        stoppers = [
            "Capital Improvement Projects (Construction)",
            "Capital Improvement Projects (Not Started)",
            "Disaster Recovery Projects",
            "Agenda Item"
        ]
        
        end_idx = len(norm_text)
        for stop in stoppers:
            match = re.search(re.escape(stop), norm_text[content_start:], re.IGNORECASE)
            if match:
                stop_idx = content_start + match.start()
                if stop_idx < end_idx:
                    end_idx = stop_idx
        
        section_text = norm_text[content_start:end_idx]
        # print(f"DEBUG: Section text len: {len(section_text)}")
        # print(f"DEBUG: Section text preview: {section_text[:100]}...")
        
        for proj in high_funding_projects:
            norm_proj = re.sub(r'\s+', ' ', proj)
            if norm_proj in section_text:
                matched_projects.add(proj)

print(f"DEBUG: Header found {header_count} times")
print("__RESULT__:")
print(json.dumps(list(matched_projects)))"""

env_args = {'var_function-call-9362456295631069052': 'file_storage/function-call-9362456295631069052.json', 'var_function-call-9362456295631066849': 'file_storage/function-call-9362456295631066849.json', 'var_function-call-12811906272455444713': 'file_storage/function-call-12811906272455444713.json', 'var_function-call-15515315888711680417': 1}

exec(code, env_args)
