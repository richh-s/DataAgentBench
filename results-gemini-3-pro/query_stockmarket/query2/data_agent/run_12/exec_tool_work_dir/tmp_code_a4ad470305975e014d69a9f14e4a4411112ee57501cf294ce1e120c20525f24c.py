code = """import json

k1 = "var_function-call-13379061347181110174"
k2 = "var_function-call-6559325847238713717"

path1 = locals()[k1]
path2 = locals()[k2]

with open(path1, "r") as f:
    d1 = json.load(f)
with open(path2, "r") as f:
    d2 = json.load(f)

s1 = set(x["Symbol"] for x in d1)
s2 = set(d2)
valid = sorted(list(s1.intersection(s2)))

# Generate ONE giant query
parts = []
for s in valid:
    # Escape double quotes in table name if needed? 
    # Usually symbols don't have quotes.
    # But checking if s contains double quote would be safe.
    # If s has ", escape it as "".
    tbl = s.replace('"', '""')
    
    # Python string: ' ... '
    q = 'SELECT \'' + s + '\' as Symbol FROM "' + tbl + '" WHERE "Adj Close" > 200 AND Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' LIMIT 1'
    parts.append(q)

full_query = " UNION ALL ".join(parts)

print("__RESULT__:")
print(json.dumps({"query": full_query}))"""

env_args = {'var_function-call-13379061347181110174': 'file_storage/function-call-13379061347181110174.json', 'var_function-call-6559325847238713717': 'file_storage/function-call-6559325847238713717.json', 'var_function-call-14816739761886936635': ['var_function-call-13379061347181110174', 'var_function-call-6559325847238713717', '__builtins__', 'json'], 'var_function-call-11850539345965912126': {'count': 1435}}

exec(code, env_args)
