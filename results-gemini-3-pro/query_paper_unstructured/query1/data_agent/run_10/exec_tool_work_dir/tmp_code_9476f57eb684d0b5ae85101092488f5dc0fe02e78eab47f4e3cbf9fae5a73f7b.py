code = """import json

file_path = locals()['var_function-call-15853476606945075848']
with open(file_path, 'r') as f:
    papers = json.load(f)

debug_output = []
food_in_text_count = 0

keyword_markers = ["Author Keywords", "Keywords", "Index Terms"]
nl = chr(10)
end_markers = ["ACM Classification", "INTRODUCTION", "ABSTRACT", "General Terms", nl+nl+nl]

for i, paper in enumerate(papers):
    text = paper.get('text', '')
    title = paper.get('filename', '')
    
    if 'food' in text.lower():
        food_in_text_count += 1
        if food_in_text_count <= 3:
             debug_output.append(f"Paper '{title}' has 'food' in text.")
    
    start_idx = -1
    marker_found = ""
    for marker in keyword_markers:
        idx = text.find(marker)
        if idx != -1:
            start_idx = idx + len(marker)
            marker_found = marker
            break
            
    if start_idx != -1:
        end_idx = len(text)
        for marker in end_markers:
            idx = text.find(marker, start_idx)
            if idx != -1 and idx < end_idx:
                end_idx = idx
        
        extracted = text[start_idx:end_idx].strip()
        # Log first 5 extractions
        if i < 5:
            debug_output.append(f"Paper: {title}, Marker: {marker_found}, Extracted: {extracted[:100]}...")
    else:
        if i < 5:
             debug_output.append(f"Paper: {title}, No keyword marker found.")

final_res = {
    "food_in_text_count": food_in_text_count,
    "debug_output": debug_output
}

print("__RESULT__:")
print(json.dumps(final_res))"""

env_args = {'var_function-call-2030052539716132653': ['paper_docs'], 'var_function-call-2030052539716130606': ['Citations', 'sqlite_sequence'], 'var_function-call-10436001229395050788': 'file_storage/function-call-10436001229395050788.json', 'var_function-call-14775446657247865324': 'file_storage/function-call-14775446657247865324.json', 'var_function-call-17848564962204727189': 'file_storage/function-call-17848564962204727189.json', 'var_function-call-15853476606945075848': 'file_storage/function-call-15853476606945075848.json', 'var_function-call-16520379867273674583': []}

exec(code, env_args)
