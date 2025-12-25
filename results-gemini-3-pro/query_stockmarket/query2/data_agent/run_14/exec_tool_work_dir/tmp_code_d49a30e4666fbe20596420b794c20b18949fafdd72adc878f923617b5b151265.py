code = """import json

path = locals()['var_function-call-795890950430017818']
with open(path, 'r') as f:
    symbols = json.load(f)

# Group by letter
by_letter = {}
for sym in symbols:
    letter = sym[0]
    if letter not in by_letter:
        by_letter[letter] = []
    by_letter[letter].append(sym)

# Generate queries
queries = {}
q = chr(39)
qq = chr(34)
for letter, syms in by_letter.items():
    parts = []
    for sym in syms:
        part = "SELECT " + q + sym + q + " as Symbol FROM " + qq + sym + qq + " WHERE " + qq + "Adj Close" + qq + " > 200 AND Date LIKE " + q + "2015%" + q + " LIMIT 1"
        parts.append(part)
    query = " UNION ALL ".join(parts)
    queries[letter] = query

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-3949593977033921261': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-12916805806640155023': 'file_storage/function-call-12916805806640155023.json', 'var_function-call-118847342532788354': 'file_storage/function-call-118847342532788354.json', 'var_function-call-795890950430017818': 'file_storage/function-call-795890950430017818.json', 'var_function-call-14536564358681273316': 1435, 'var_function-call-8889034498850713553': 'test', 'var_function-call-12910800544588247316': 1435, 'var_function-call-17086037818106034107': 'file_storage/function-call-17086037818106034107.json', 'var_function-call-12029157764372185238': 'file_storage/function-call-12029157764372185238.json', 'var_function-call-3474506765428153084': 'file_storage/function-call-3474506765428153084.json', 'var_function-call-15935806625743756606': 'file_storage/function-call-15935806625743756606.json', 'var_function-call-11704360634435536959': 'file_storage/function-call-11704360634435536959.json', 'var_function-call-15141616485534470237': 'file_storage/function-call-15141616485534470237.json', 'var_function-call-4626988011822015578': 'file_storage/function-call-4626988011822015578.json', 'var_function-call-17892634750962232910': 9933, 'var_function-call-5309851501269620060': [{'Letter': 'A', 'Count': '42'}, {'Letter': 'B', 'Count': '36'}, {'Letter': 'C', 'Count': '52'}, {'Letter': 'D', 'Count': '84'}, {'Letter': 'E', 'Count': '106'}, {'Letter': 'F', 'Count': '125'}, {'Letter': 'G', 'Count': '51'}, {'Letter': 'H', 'Count': '55'}, {'Letter': 'I', 'Count': '124'}, {'Letter': 'J', 'Count': '54'}, {'Letter': 'K', 'Count': '29'}, {'Letter': 'L', 'Count': '25'}, {'Letter': 'M', 'Count': '42'}, {'Letter': 'N', 'Count': '19'}, {'Letter': 'O', 'Count': '21'}, {'Letter': 'P', 'Count': '75'}, {'Letter': 'Q', 'Count': '29'}, {'Letter': 'R', 'Count': '75'}, {'Letter': 'S', 'Count': '151'}, {'Letter': 'T', 'Count': '45'}, {'Letter': 'U', 'Count': '56'}, {'Letter': 'V', 'Count': '55'}, {'Letter': 'W', 'Count': '20'}, {'Letter': 'X', 'Count': '46'}, {'Letter': 'Y', 'Count': '9'}, {'Letter': 'Z', 'Count': '9'}]}

exec(code, env_args)
