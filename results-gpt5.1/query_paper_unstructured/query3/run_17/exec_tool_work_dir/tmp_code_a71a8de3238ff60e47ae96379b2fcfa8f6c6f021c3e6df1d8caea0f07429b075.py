code = """import re, json

with open(var_call_KnqHJJ9V657Bwgo93MPhPsCQ, 'r') as f:
    mongo_records = json.load(f)

papers = []
for doc in mongo_records[:50]:
    text = doc.get('text', '') or ''
    filename = doc.get('filename', '') or ''
    title = filename.replace('.txt', '')

    m = re.search(r'(19|20)\d{2}', text[:1500])
    year = int(m.group(0)) if m else None

    is_empirical = bool(re.search(r'\bempirical\b', text, re.I))

    papers.append({'title': title, 'year': year, 'is_empirical': is_empirical})

print("__RESULT__:")
print(json.dumps(papers))"""

env_args = {'var_call_KnqHJJ9V657Bwgo93MPhPsCQ': 'file_storage/call_KnqHJJ9V657Bwgo93MPhPsCQ.json', 'var_call_ljjyHD8mSS5ZOtYJgynOZbj8': 'file_storage/call_ljjyHD8mSS5ZOtYJgynOZbj8.json', 'var_call_UbgQ5PLo7vO1fKKU1cd3NlHv': {'cols': ['title', 'total_citations'], 'sample': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'total_citations': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'total_citations': '313'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}]}, 'var_call_rHGF0g4Glvc94eTwoC1oqkkH': {'cols': ['title', 'total_citations'], 'n': 259}}

exec(code, env_args)
