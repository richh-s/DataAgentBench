code = """import json

with open(locals()['var_function-call-1637746451261953747'], 'r') as f:
    papers_data = json.load(f)

# Find "A Lived Informatics Model..."
for p in papers_data:
    if "A Lived Informatics Model" in p['filename']:
        print(f"--- TEXT START ({p['filename']}) ---")
        print(p['text'][:500])
        print("--- TEXT END ---")
        break"""

env_args = {'var_function-call-1625983961919980332': 'file_storage/function-call-1625983961919980332.json', 'var_function-call-1625983961919980937': 'file_storage/function-call-1625983961919980937.json', 'var_function-call-603899956623293996': 'file_storage/function-call-603899956623293996.json', 'var_function-call-10661397933404745766': [], 'var_function-call-11800293491939370274': {'count': 5, 'years': [None, None, None, None, None], 'empirical_count': 2, 'gt_2016_count': 0}, 'var_function-call-1637746451261953747': 'file_storage/function-call-1637746451261953747.json', 'var_function-call-14546405968583665070': [{'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citation_count': 278}], 'var_function-call-16887723569607349610': 'file_storage/function-call-16887723569607349610.json'}

exec(code, env_args)
