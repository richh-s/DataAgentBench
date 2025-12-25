code = """import json
from collections import defaultdict

file_path_meta = locals()['var_function-call-5463793062581898541']
with open(file_path_meta, 'r') as f:
    metadata_list = json.load(f)

ids_2010 = [int(item['article_id']) for item in metadata_list if item['publication_date'].startswith('2010')]

query = {
    "collection": "articles",
    "filter": {
        "article_id": {"$in": ids_2010}
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-5463793062581898541': 'file_storage/function-call-5463793062581898541.json', 'var_function-call-344482854029373658': 'file_storage/function-call-344482854029373658.json', 'var_function-call-8270661288261401404': 14860, 'var_function-call-15074060882240908165': [{'COUNT(*)': '127600'}], 'var_function-call-11601952591179263792': {'min': 3, 'max': 127583}, 'var_function-call-14130855968382315111': {'2020': 1366, '2016': 1364, '2015': 1357, '2017': 1391, '2013': 1354, '2010': 1306, '2018': 1351, '2019': 1328, '2014': 1372, '2011': 1316, '2012': 1355}}

exec(code, env_args)
