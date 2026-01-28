code = """import json

# Load papers
with open(locals()['var_function-call-12774124181016147194'], 'r') as f:
    papers_data = json.load(f)

# Find papers with 'food' in text
count = 0
for p in papers_data:
    if 'food' in p['text'].lower():
        count += 1
        if count <= 5:
            print(f"--- Match in: {p['filename']} ---")
            # Find all occurrences of 'food' in the first 2000 chars (likely header/abstract/keywords)
            text_head = p['text'][:3000].lower()
            start = 0
            while True:
                idx = text_head.find('food', start)
                if idx == -1:
                    break
                # Print context
                print(f"Context: ...{p['text'][idx-20:idx+30].replace(chr(10), ' ')}...")
                start = idx + 1

print(f"Total papers containing 'food': {count}")
print("__RESULT__:")
print(json.dumps("done"))"""

env_args = {'var_function-call-2229407460365091455': 'file_storage/function-call-2229407460365091455.json', 'var_function-call-12774124181016146207': 'file_storage/function-call-12774124181016146207.json', 'var_function-call-12774124181016147194': 'file_storage/function-call-12774124181016147194.json', 'var_function-call-12375458960310420055': '0'}

exec(code, env_args)
