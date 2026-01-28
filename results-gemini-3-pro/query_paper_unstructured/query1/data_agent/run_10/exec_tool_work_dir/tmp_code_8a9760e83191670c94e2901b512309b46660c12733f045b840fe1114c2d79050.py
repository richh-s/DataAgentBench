code = """import json
import re

# Load the data
file_path = 'var_function-call-15853476606945075848'
with open(file_path, 'r') as f:
    papers = json.load(f)

matching_titles = []
debug_info = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Try to find keywords
    # Regex to find Author Keywords or Keywords, followed by text until double newline or next section
    # Common headers: "Author Keywords", "Keywords", "Index Terms"
    # End markers: "ACM Classification", "INTRODUCTION", "ABSTRACT", "General Terms"
    
    # We will search for the keyword header and then grab reasonable amount of text
    match = re.search(r'(?:Author Keywords|Keywords|Index Terms)[:\s\n]+(.*?)(?:\n\n\n|ACM Classification|INTRODUCTION|ABSTRACT|General Terms)', text, re.DOTALL | re.IGNORECASE)
    
    if match:
        keywords = match.group(1).lower()
        if 'food' in keywords:
            matching_titles.append(title)
            # debug_info.append(f"Found 'food' in {title}: {keywords[:50]}...")
        else:
            # Check if maybe we missed it or it's formatted differently
            pass
            
    else:
        # If regex failed, maybe try a simpler search or look at the first page
        # Some papers might not have explicit keywords section or it's named differently
        # Let's check first 2000 chars for "food" appearing in a list-like context?
        # That's risky. Let's rely on the keywords section first.
        pass

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-2030052539716132653': ['paper_docs'], 'var_function-call-2030052539716130606': ['Citations', 'sqlite_sequence'], 'var_function-call-10436001229395050788': 'file_storage/function-call-10436001229395050788.json', 'var_function-call-14775446657247865324': 'file_storage/function-call-14775446657247865324.json', 'var_function-call-17848564962204727189': 'file_storage/function-call-17848564962204727189.json', 'var_function-call-15853476606945075848': 'file_storage/function-call-15853476606945075848.json'}

exec(code, env_args)
