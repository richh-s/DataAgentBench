code = """import json

file_path = locals()['var_function-call-2017477155051187807']
with open(file_path, 'r') as f:
    papers_data = json.load(f)

physical_activity_2016_titles = []
for paper in papers_data:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']

    if '2016' in text and 'physical activity' in text.lower():
        physical_activity_2016_titles.append(title)

print('__RESULT__:')
print(json.dumps(physical_activity_2016_titles))"""

env_args = {'var_function-call-17798319154585505742': ['paper_docs'], 'var_function-call-12002591806772645320': 'file_storage/function-call-12002591806772645320.json', 'var_function-call-13349807814290358084': [], 'var_function-call-976136314626732420': 'file_storage/function-call-976136314626732420.json', 'var_function-call-12719539591056404857': 'file_storage/function-call-12719539591056404857.json', 'var_function-call-12927970392808823710': [], 'var_function-call-2017477155051187807': 'file_storage/function-call-2017477155051187807.json'}

exec(code, env_args)
