code = """import json
from collections import defaultdict

# Load metadata
file_path = locals()['var_function-call-344482854029373658']
# Note: the previous file 'var_function-call-344482854029373658' contains only IDs (list of ints).
# I need the file with publication dates.
# That was 'var_function-call-5463793062581898541'.
file_path_meta = locals()['var_function-call-5463793062581898541']

with open(file_path_meta, 'r') as f:
    metadata_list = json.load(f)

ids_by_year = defaultdict(list)
for item in metadata_list:
    # item is {'article_id': '...', 'publication_date': 'YYYY-MM-DD'}
    year = item['publication_date'][:4]
    ids_by_year[year].append(int(item['article_id']))

# Output the counts per year to verify
counts = {y: len(ids) for y, ids in ids_by_year.items()}
print("__RESULT__:")
print(json.dumps(counts))"""

env_args = {'var_function-call-5463793062581898541': 'file_storage/function-call-5463793062581898541.json', 'var_function-call-344482854029373658': 'file_storage/function-call-344482854029373658.json', 'var_function-call-8270661288261401404': 14860, 'var_function-call-15074060882240908165': [{'COUNT(*)': '127600'}], 'var_function-call-11601952591179263792': {'min': 3, 'max': 127583}}

exec(code, env_args)
