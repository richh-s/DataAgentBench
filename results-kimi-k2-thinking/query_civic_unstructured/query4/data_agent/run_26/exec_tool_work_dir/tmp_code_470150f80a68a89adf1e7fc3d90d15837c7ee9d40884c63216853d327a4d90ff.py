code = """import json, os

print('=== START ===')

# Access the stored results
civic_docs_var = globals().get('var_functions.query_db:0') or locals().get('var_functions.query_db:0')
funding_var = globals().get('var_functions.query_db:5') or locals().get('var_functions.query_db:5')

print('civic_docs_var type:', type(civic_docs_var))
print('funding_var type:', type(funding_var))

# Load civic docs data
if isinstance(civic_docs_var, str) and os.path.exists(civic_docs_var):
    with open(civic_docs_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_var if civic_docs_var else []

# Load funding data  
if isinstance(funding_var, str) and os.path.exists(funding_var):
    with open(funding_var, 'r') as f:
        funding = json.load(f)
else:
    funding = funding_var if funding_var else []

print('Civic docs loaded:', len(civic_docs), 'documents')
print('Funding records loaded:', len(funding), 'records')

# Show structure of first records if available
if civic_docs:
    first_doc = civic_docs[0]
    print('\nFirst civic doc keys:', list(first_doc.keys()))
    print('First civic doc filename:', first_doc.get('filename'))
    print('First civic doc text preview:', str(first_doc.get('text', ''))[:200])
    
if funding:
    first_funding = funding[0]
    print('\nFirst funding record:', json.dumps(first_funding))

print('=== END ===')

print('__RESULT__:')
print(json.dumps({
    'civic_docs_count': len(civic_docs),
    'funding_count': len(funding),
    'success': True
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
