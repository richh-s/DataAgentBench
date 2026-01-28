code = """import json

# Get the file path from the variable in locals()
file_path = locals()['var_function-call-15853476606945075848']

with open(file_path, 'r') as f:
    papers = json.load(f)

matching_titles = []

keyword_markers = ["Author Keywords", "Keywords", "Index Terms"]
nl = chr(10)
end_markers = ["ACM Classification", "INTRODUCTION", "ABSTRACT", "General Terms", nl+nl+nl]

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    start_idx = -1
    for marker in keyword_markers:
        idx = text.find(marker)
        if idx != -1:
            start_idx = idx + len(marker)
            break
            
    if start_idx != -1:
        end_idx = len(text)
        for marker in end_markers:
            idx = text.find(marker, start_idx)
            if idx != -1 and idx < end_idx:
                end_idx = idx
        
        if end_idx - start_idx > 1000:
            end_idx = start_idx + 1000
            
        keywords_section = text[start_idx:end_idx].lower()
        
        if 'food' in keywords_section:
            matching_titles.append(title)

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-2030052539716132653': ['paper_docs'], 'var_function-call-2030052539716130606': ['Citations', 'sqlite_sequence'], 'var_function-call-10436001229395050788': 'file_storage/function-call-10436001229395050788.json', 'var_function-call-14775446657247865324': 'file_storage/function-call-14775446657247865324.json', 'var_function-call-17848564962204727189': 'file_storage/function-call-17848564962204727189.json', 'var_function-call-15853476606945075848': 'file_storage/function-call-15853476606945075848.json'}

exec(code, env_args)
