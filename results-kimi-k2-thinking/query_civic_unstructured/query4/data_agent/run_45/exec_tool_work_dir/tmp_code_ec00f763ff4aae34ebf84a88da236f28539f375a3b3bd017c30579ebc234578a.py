code = """import json
import os

# Read the file path from the result
docs_file = var_functions.query_db:2
print('Loading data from:', docs_file)

if os.path.exists(docs_file):
    with open(docs_file, 'r') as f:
        civic_docs = json.load(f)
    print('Successfully loaded', len(civic_docs), 'documents')
    
    # Examine documents for Spring 2022
    spring_2022_refs = []
    for i, doc in enumerate(civic_docs[:3]):  # Check first 3 docs
        text = doc.get('text', '')
        filename = doc.get('filename', '')
        
        # Look for any Spring 2022 references
        spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May', '2022-03', '2022-04', '2022-05']
        for pattern in spring_patterns:
            idx = text.find(pattern)
            if idx != -1:
                context = text[max(0, idx-100):min(len(text), idx+100)].replace('\n', ' ')
                spring_2022_refs.append({
                    'doc': i,
                    'filename': filename,
                    'pattern': pattern,
                    'context': context
                })
    
    print('\nFound Spring 2022 references:')
    for ref in spring_2022_refs:
        print(f"Doc {ref['doc']} ({ref['filename']}): Found '{ref['pattern']}'")
        print(f"  Context: {ref['context']}")
        print()
    
    result = {
        'total_docs': len(civic_docs),
        'spring_2022_refs': spring_2022_refs
    }
    
    __RESULT__:
    print('__RESULT__:')
    print(json.dumps(result))
else:
    print('File not found')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
