code = """import re
import json

dates = ["dated 5th March 2019", "March the 18th, 2019"]

pattern = re.compile(r'\d+')

results = {}
for d in dates:
    results[d] = pattern.findall(d)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-16849742418819018650': 'file_storage/function-call-16849742418819018650.json', 'var_function-call-2105601753514837134': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_function-call-15924435190051233990': [{'symbol': 'A62B', 'level': '5.0'}, {'symbol': 'A63G', 'level': '5.0'}, {'symbol': 'A63K', 'level': '5.0'}, {'symbol': 'A63B', 'level': '5.0'}, {'symbol': 'C13B50/00', 'level': '7.0'}, {'symbol': 'H04Q2213/296', 'level': '8.0'}, {'symbol': 'A63J', 'level': '5.0'}, {'symbol': 'A63C', 'level': '5.0'}, {'symbol': 'A63D', 'level': '5.0'}, {'symbol': 'A63F', 'level': '5.0'}, {'symbol': 'C25D', 'level': '5.0'}, {'symbol': 'A63H', 'level': '5.0'}, {'symbol': 'A99Z', 'level': '5.0'}, {'symbol': 'B01J', 'level': '5.0'}, {'symbol': 'B01B', 'level': '5.0'}, {'symbol': 'B01D', 'level': '5.0'}, {'symbol': 'B01L', 'level': '5.0'}, {'symbol': 'C13B40/00', 'level': '7.0'}, {'symbol': 'B01F', 'level': '5.0'}, {'symbol': 'B02C', 'level': '5.0'}], 'var_function-call-14819640206453325990': [{'len': '4', 'cnt': '677'}], 'var_function-call-11747405801204171974': 'file_storage/function-call-11747405801204171974.json', 'var_function-call-6610964282860133498': 'file_storage/function-call-6610964282860133498.json', 'var_function-call-14715050367573468631': [], 'var_function-call-15796831424419617426': {'debug': {'min_year': None, 'max_year': None, 'total_cpcs': 0, 'sample_years': []}, 'best_years_sample': {}}, 'var_function-call-11140428547165836367': [], 'var_function-call-3511093510252264699': {'min_year': None, 'max_year': None}, 'var_function-call-8917065771742920071': {'count': 277813, 'sample_dates': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019', 'on April 8th, 2019', '15th April 2019', 'April 19th, 2019', '2019, April 24th', 'April 26th, 2019']}, 'var_function-call-11907245405186178896': {'dated 5th March 2019': [], 'March the 18th, 2019': [], '29th March 2019': [], 'on March 29th, 2019': [], '2nd April 2019': [], 'on April 8th, 2019': [], '15th April 2019': [], 'April 19th, 2019': [], '2019, April 24th': [], 'April 26th, 2019': []}}

exec(code, env_args)
