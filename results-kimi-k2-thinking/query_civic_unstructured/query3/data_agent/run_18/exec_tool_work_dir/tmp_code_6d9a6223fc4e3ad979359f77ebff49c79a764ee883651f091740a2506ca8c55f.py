code = """# Access the data from the stored variables
funding_data = locals()['var_functions.query_db:2']
civic_docs = locals()['var_functions.query_db:0']

print(f"Number of funding records: {len(funding_data)}")
print(f"Number of civic documents: {len(civic_docs)}")
print(f"First few funding records:")
print(funding_data[:3])
print(f"\nFirst civic document structure:")
print(json.dumps(civic_docs[0], indent=2)[:500])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
