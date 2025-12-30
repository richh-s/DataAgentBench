code = """import json

path = locals()['var_function-call-2585691326327215227']
with open(path, 'r') as f:
    papers = json.load(f)

titles = []
for p in papers:
    # We trust the Mongo filter for "food"
    titles.append(p['filename'].replace('.txt', ''))

# Prepare SQL query
escaped_titles = [t.replace("'", "''") for t in titles]
# Filter empty titles if any
escaped_titles = [t for t in escaped_titles if t]

if not escaped_titles:
    sql_query = "SELECT 0"
else:
    titles_str = "', '".join(escaped_titles)
    sql_query = f"SELECT citation_count FROM Citations WHERE title IN ('{titles_str}')"

print("__RESULT__:")
print(json.dumps(sql_query))"""

env_args = {'var_function-call-13604834933233695573': 'file_storage/function-call-13604834933233695573.json', 'var_function-call-13672825597397015902': 'file_storage/function-call-13672825597397015902.json', 'var_function-call-2585691326327215227': 'file_storage/function-call-2585691326327215227.json', 'var_function-call-4981003287102314854': [], 'var_function-call-13805358010662920095': "SELECT citation_count FROM Citations WHERE title IN ('')", 'var_function-call-2766234641160202705': "SELECT citation_count FROM Citations WHERE title IN ('')", 'var_function-call-10201737980555806332': {'count': 5, 'keys': ['_id', 'filename', 'text'], 'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'text_len': 68339, 'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n", 'has_food_substring': True}}

exec(code, env_args)
