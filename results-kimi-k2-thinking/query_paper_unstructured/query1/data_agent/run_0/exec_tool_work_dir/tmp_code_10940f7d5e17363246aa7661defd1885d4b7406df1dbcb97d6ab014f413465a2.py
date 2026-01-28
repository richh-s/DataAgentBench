code = """# Check what variables are available
import json

# List available variables
available_vars = [var for var in dir() if var.startswith('var_')]
print(f"Available variables: {available_vars}")

# Check the result from the MongoDB query
if 'var_functions.query_db:4' in dir():
    paper_docs = var_functions.query_db:4
    print(f"Type of paper_docs: {type(paper_docs)}")
    print(f"Length: {len(paper_docs) if hasattr(paper_docs, '__len__') else 'N/A'}")
    print(f"First item preview: {str(paper_docs)[:300] if paper_docs else 'None'}")
else:
    print("var_functions.query_db:4 not found")

# Also check var_functions.query_db:2
if 'var_functions.query_db:2' in dir():
    paper_docs2 = var_functions.query_db:2
    print(f"\nType of paper_docs2: {type(paper_docs2)}")
    print(f"Length: {len(paper_docs2) if hasattr(paper_docs2, '__len__') else 'N/A'}")
    print(f"First item preview: {str(paper_docs2)[:300] if paper_docs2 else 'None'}")
else:
    print("var_functions.query_db:2 not found")

# Check list_db results
if 'var_functions.list_db:6' in dir():
    tables = var_functions.list_db:6
    print(f"\nTables in citations_database: {tables}")
else:
    print("var_functions.list_db:6 not found")

#print('__RESULT__:')
#print(json.dumps("test"))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence']}

exec(code, env_args)
