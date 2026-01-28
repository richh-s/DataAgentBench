code = """import json

# Sample from the UNIV CALIFORNIA patent
sample_uc_patent = {
    "Patents_info": "In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.",
    "citation": '[\\n  {\\n    "application_number": "",\\n    "category": "SEA",\\n    "filing_date": 0,\\n    "npl_text": "",\\n    "publication_number": "US-4599677-A",\\n    "type": ""\\n  },\\n  {\\n    "application_number": "",\\n    "category": "SEA",\\n    "filing_date": 0,\\n    "npl_text": "",\\n    "publication_number": "US-2015129765-A1",\\n    "type": ""\\n  },\\n  {\\n    "application_number": "",\\n    "category": "SEA",\\n    "filing_date": 0,\\n    "npl_text": "",\\n    "publication_number": "FR-3105380-A1",\\n    "type": ""\\n  },\\n  {\\n    "application_number": "",\\n    "category": "SEA",\\n    "filing_date": 0,\\n    "npl_text": "",\\n    "publication_number": "US-11466906-B2",\\n    "type": ""\\n  }\\n]'
}

print("__RESULT__:")
print(json.dumps({"sample_patent": sample_uc_patent}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}]}

exec(code, env_args)
