code = """import json
import re

# Load the data
file_path = 'var_function-call-15853476606945075848'
with open(file_path, 'r') as f:
    papers = json.load(f)

matching_titles = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Regex to find Author Keywords or Keywords
    match = re.search(r'(?:Author Keywords|Keywords|Index Terms)[:\s\n]+(.*?)(?:\n\n\n|ACM Classification|INTRODUCTION|ABSTRACT|General Terms)', text, re.DOTALL | re.IGNORECASE)
    
    if match:
        keywords = match.group(1).lower()
        if 'food' in keywords:
            matching_titles.append(title)
    else:
        # Fallback: Search for "Key words" or similar if the first regex missed
        match2 = re.search(r'(?:Key words)[:\s\n]+(.*?)(?:\n\n\n|ACM Classification|INTRODUCTION|ABSTRACT)', text, re.DOTALL | re.IGNORECASE)
        if match2:
            keywords = match2.group(1).lower()
            if 'food' in keywords:
                matching_titles.append(title)

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-2030052539716132653': ['paper_docs'], 'var_function-call-2030052539716130606': ['Citations', 'sqlite_sequence'], 'var_function-call-10436001229395050788': 'file_storage/function-call-10436001229395050788.json', 'var_function-call-14775446657247865324': 'file_storage/function-call-14775446657247865324.json', 'var_function-call-17848564962204727189': 'file_storage/function-call-17848564962204727189.json', 'var_function-call-15853476606945075848': 'file_storage/function-call-15853476606945075848.json'}

exec(code, env_args)
