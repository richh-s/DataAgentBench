code = """import json

cites_path = var_call_W8cOEzND1SanxVZ9MIkWkbzn
with open(cites_path, 'r') as f:
    citations = json.load(f)

# Inspect the raw Python representation of the first element and keys
first = citations[0]
keys = list(first.keys())

out = json.dumps({'first_record': first, 'keys': keys})
print("__RESULT__:")
print(out)"""

env_args = {'var_call_S0PTExgxghOnm3uoZgX1mD5E': 'file_storage/call_S0PTExgxghOnm3uoZgX1mD5E.json', 'var_call_W8cOEzND1SanxVZ9MIkWkbzn': 'file_storage/call_W8cOEzND1SanxVZ9MIkWkbzn.json', 'var_call_SAYRfjpWGTl0eNagZVqFmlhb': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'total_citations': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'total_citations': '313'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'total_citations': '368'}, {'title': 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'total_citations': '277'}]}

exec(code, env_args)
