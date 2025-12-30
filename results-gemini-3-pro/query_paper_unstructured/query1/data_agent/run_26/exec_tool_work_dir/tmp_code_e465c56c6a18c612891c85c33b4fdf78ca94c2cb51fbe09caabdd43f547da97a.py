code = """import json

# Load data
with open(locals()['var_function-call-17971925795973344162'], 'r') as f:
    docs = json.load(f)

with open(locals()['var_function-call-17971925795973342135'], 'r') as f:
    citations = json.load(f)

food_titles = []
debug_info = []

newline = chr(10)
double_newline = newline + newline

for doc in docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
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
            
        keywords_block = subtext[:end_idx].lower()
        
        if 'food' in keywords_block:
            food_titles.append(title)
            if len(debug_info) < 5:
                debug_info.append({'title': title, 'keywords': keywords_block})

total_citations = 0
for cit in citations:
    if cit['title'] in food_titles:
        try:
            total_citations += int(cit['citation_count'])
        except:
            pass

print('__RESULT__:')
print(json.dumps({'food_titles': food_titles, 'total_citations': total_citations, 'debug': debug_info}))"""

env_args = {'var_function-call-8748244462217434689': ['paper_docs'], 'var_function-call-8748244462217434842': ['Citations', 'sqlite_sequence'], 'var_function-call-10817664668211665430': 'file_storage/function-call-10817664668211665430.json', 'var_function-call-4112176734939169200': 'file_storage/function-call-4112176734939169200.json', 'var_function-call-17971925795973344162': 'file_storage/function-call-17971925795973344162.json', 'var_function-call-17971925795973342135': 'file_storage/function-call-17971925795973342135.json'}

exec(code, env_args)
