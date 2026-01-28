code = """import json
# Read the filenames from the last mongo query result
var = var_call_CqKkYYQCnIyT2aKnCLF0jaPL
filenames = [d['filename'] for d in var]

# Read citations
with open(var_call_sMdGCvUlKzwNoJJjCix29a0p, 'r', encoding='utf-8') as f:
    citations = json.load(f)
lookup = {rec['title']: int(rec['total_citations']) for rec in citations}

results = []
for fn in filenames:
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if title in lookup:
        results.append({'title': title, 'total_citations': lookup[title]})

output = {'results': results}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_U1Ff80T1kKXuRvdhRUjUwawe': ['paper_docs'], 'var_call_8Hby2Sk3LnewtJQJZ7U1h8GG': ['Citations', 'sqlite_sequence'], 'var_call_ymVAAUnYUlW5BmI2odMZ75wC': 'file_storage/call_ymVAAUnYUlW5BmI2odMZ75wC.json', 'var_call_sMdGCvUlKzwNoJJjCix29a0p': 'file_storage/call_sMdGCvUlKzwNoJJjCix29a0p.json', 'var_call_vb4EwbOIJIafyvfDhCj7lric': {'citations_count': 259}, 'var_call_CqKkYYQCnIyT2aKnCLF0jaPL': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings.txt'}, {'filename': 'Communicating Uncertainty in Fertility Prognosis.txt'}, {'filename': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt'}]}

exec(code, env_args)
