code = """import json

# Load data
with open(locals()['var_function-call-17971925795973344162'], 'r') as f:
    docs = json.load(f)

extracted_keywords = []

newline = chr(10)
double_newline = newline + newline

for doc in docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    start_idx = -1
    keywords_headers = ['Author Keywords', 'Keywords', 'Index Terms']
    for kw_header in keywords_headers:
        idx = text.find(kw_header)
        if idx != -1:
            start_idx = idx
            break
    
    if start_idx != -1:
        subtext = text[start_idx:]
        end_idx = subtext.find(double_newline)
        if end_idx == -1:
            end_idx = 1000 
            
        keywords_block = subtext[:end_idx]
        extracted_keywords.append({"filename": filename, "keywords": keywords_block})

print('__RESULT__:')
print(json.dumps(extracted_keywords[:5]))"""

env_args = {'var_function-call-8748244462217434689': ['paper_docs'], 'var_function-call-8748244462217434842': ['Citations', 'sqlite_sequence'], 'var_function-call-10817664668211665430': 'file_storage/function-call-10817664668211665430.json', 'var_function-call-4112176734939169200': 'file_storage/function-call-4112176734939169200.json', 'var_function-call-17971925795973344162': 'file_storage/function-call-17971925795973344162.json', 'var_function-call-17971925795973342135': 'file_storage/function-call-17971925795973342135.json', 'var_function-call-5998872397712651256': {'food_titles': [], 'total_citations': 0, 'debug': []}}

exec(code, env_args)
