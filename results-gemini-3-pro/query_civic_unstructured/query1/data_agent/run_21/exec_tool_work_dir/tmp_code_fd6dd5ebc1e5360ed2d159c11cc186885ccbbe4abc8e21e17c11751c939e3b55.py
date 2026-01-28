code = """import json
import re

# Load funding data
with open(locals()['var_function-call-11698490353194121893']) as f:
    funding_data = json.load(f)

high_funding_projects = {item['Project_Name'] for item in funding_data}

# Load civic docs
with open(locals()['var_function-call-12811906272455444713']) as f:
    docs = json.load(f)

matched_projects = set()

for doc in docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Normalize whitespace
    norm_text = re.sub(r'\s+', ' ', text)
    
    # Find start of "Capital - Design"
    header = "Capital Improvement Projects (Design)"
    
    start_indices = [m.start() for m in re.finditer(re.escape(header), norm_text, re.IGNORECASE)]
    
    for start_idx in start_indices:
        content_start = start_idx + len(header)
        
        # Stoppers
        stoppers = [
            "Capital Improvement Projects (Construction)",
            "Capital Improvement Projects (Not Started)",
            "Disaster Recovery Projects"
        ]
        
        end_idx = len(norm_text)
        
        for stop in stoppers:
            match = re.search(re.escape(stop), norm_text[content_start:], re.IGNORECASE)
            if match:
                stop_idx = content_start + match.start()
                if stop_idx < end_idx:
                    end_idx = stop_idx
        
        section_text = norm_text[content_start:end_idx]
        section_text_lower = section_text.lower()
        
        for proj in high_funding_projects:
            norm_proj = re.sub(r'\s+', ' ', proj)
            if norm_proj.lower() in section_text_lower:
                matched_projects.add(proj)

print("__RESULT__:")
print(json.dumps(len(matched_projects)))"""

env_args = {'var_function-call-9362456295631069052': 'file_storage/function-call-9362456295631069052.json', 'var_function-call-9362456295631066849': 'file_storage/function-call-9362456295631066849.json', 'var_function-call-12811906272455444713': 'file_storage/function-call-12811906272455444713.json', 'var_function-call-15515315888711680417': 1, 'var_function-call-2728401049196914947': ['PCH Median Improvements Project'], 'var_function-call-17738664664704783316': 12, 'var_function-call-11698490353194121893': 'file_storage/function-call-11698490353194121893.json'}

exec(code, env_args)
