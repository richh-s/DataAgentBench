code = """# Check what's in the storage
try:
    papers = locals()['var_functions.query_db:2']
    print("Type of papers:", type(papers))
    print("Is string?", isinstance(papers, str))
    if isinstance(papers, str) and '.json' in papers:
        print("It's a file path:", papers)
    else:
        print("It's actual data, length:", len(papers))
except Exception as e:
    print("Error:", e)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence']}

exec(code, env_args)
