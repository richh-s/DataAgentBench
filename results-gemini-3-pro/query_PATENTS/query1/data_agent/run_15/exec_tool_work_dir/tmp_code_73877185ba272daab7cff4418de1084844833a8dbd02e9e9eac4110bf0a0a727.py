code = """import re
import json

dates = ["dated 5th March 2019", "March the 18th, 2019", "29th March 2019", "on March 29th, 2019"]
pattern = re.compile(r'\b(19|20)\d{2}\b')
simple_pattern = re.compile(r'(19|20)\d{2}')

results = []
for d in dates:
    m = pattern.search(d)
    m_simple = simple_pattern.search(d)
    results.append({
        "date": d,
        "match_b": m.group(0) if m else None,
        "match_simple": m_simple.group(0) if m_simple else None
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-1606092503254054957': ['cpc_definition'], 'var_function-call-1606092503254055080': ['publicationinfo'], 'var_function-call-49990340508428720': [{'count': '677'}], 'var_function-call-49990340508428761': 'file_storage/function-call-49990340508428761.json', 'var_function-call-11885506798250293123': [{'count(*)': '277813'}], 'var_function-call-4195696039592522231': 'file_storage/function-call-4195696039592522231.json', 'var_function-call-4195696039592525610': 'file_storage/function-call-4195696039592525610.json', 'var_function-call-937466644733390942': [], 'var_function-call-6650574053773001958': {'min_year': None, 'max_year': None, 'total_patents_with_year': 0, 'matched_patents': 0, 'sample_counts': {'B27G': {}, 'A62B': {}, 'H02J': {}, 'F21S': {}, 'A46D': {}}}, 'var_function-call-1359902107072342899': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th', 'April 26th, 2019', 'on April 30th, 2019', 'dated 1st May 2019', '2019, May 15th', 'May 15th, 2019', 'June the 6th, 2019', 'on June 7th, 2019', '14th of June, 2019', '2019 on Jun 14th', 'dated 18th June 2019', 'June the 19th, 2019']}

exec(code, env_args)
