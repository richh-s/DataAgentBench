code = """import json

# Load papers
with open(locals()['var_function-call-12774124181016147194'], 'r') as f:
    papers_data = json.load(f)

print(f"Total papers: {len(papers_data)}")
print("Sample titles:")
for p in papers_data[:5]:
    print(p['filename'])

print("\nChecking for 'food' in titles:")
food_titles = [p['filename'] for p in papers_data if 'food' in p['filename'].lower()]
print(food_titles)

print("\nChecking for 'food' in text of first 5 papers:")
for p in papers_data[:5]:
    if 'food' in p['text'].lower():
        print(f"Found 'food' in {p['filename']}")
        # Print context
        idx = p['text'].lower().find('food')
        print(p['text'][max(0, idx-50):min(len(p['text']), idx+50)])
    else:
        print(f"No 'food' in {p['filename']}")
        
print("__RESULT__:")
print(json.dumps("debug"))"""

env_args = {'var_function-call-2229407460365091455': 'file_storage/function-call-2229407460365091455.json', 'var_function-call-12774124181016146207': 'file_storage/function-call-12774124181016146207.json', 'var_function-call-12774124181016147194': 'file_storage/function-call-12774124181016147194.json', 'var_function-call-12375458960310420055': '0'}

exec(code, env_args)
