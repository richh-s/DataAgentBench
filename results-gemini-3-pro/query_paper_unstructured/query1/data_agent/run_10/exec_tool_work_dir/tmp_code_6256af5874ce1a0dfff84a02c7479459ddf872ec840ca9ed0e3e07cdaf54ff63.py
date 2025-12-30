code = """import json

file_path = 'var_function-call-15853476606945075848'
with open(file_path, 'r') as f:
    papers = json.load(f)

matching_titles = []

keyword_markers = ["Author Keywords", "Keywords", "Index Terms"]
# avoid explicit newlines in string literals to prevent parsing errors
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
        # Scan for the nearest end marker
        for marker in end_markers:
            idx = text.find(marker, start_idx)
            # We want the nearest end marker that is after start_idx
            if idx != -1 and idx < end_idx:
                end_idx = idx
        
        # Limit the search to a reasonable length (e.g., 500 chars) to avoid reading the whole text if end marker missing
        if end_idx - start_idx > 1000:
            end_idx = start_idx + 1000
            
        keywords_section = text[start_idx:end_idx].lower()
        
        # Check for 'food'
        # To be safe, check for 'food' as a word or component of a phrase
        # But 'food' is a common substring (e.g. 'flood'?). No.
        # But 'seafood'? Maybe. The domain is likely "food".
        # Let's check simply for 'food' first.
        if 'food' in keywords_section:
            matching_titles.append(title)

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-2030052539716132653': ['paper_docs'], 'var_function-call-2030052539716130606': ['Citations', 'sqlite_sequence'], 'var_function-call-10436001229395050788': 'file_storage/function-call-10436001229395050788.json', 'var_function-call-14775446657247865324': 'file_storage/function-call-14775446657247865324.json', 'var_function-call-17848564962204727189': 'file_storage/function-call-17848564962204727189.json', 'var_function-call-15853476606945075848': 'file_storage/function-call-15853476606945075848.json'}

exec(code, env_args)
