code = """# Check available variables from previous tool calls
import json

print("=== Checking Available Variables ===")

# Get the two key variables
try:
    q5 = var_functions.query_db:5
    print("Found var_functions.query_db:5")
    print("Type:", type(q5))
    if isinstance(q5, str):
        print("It's a string (likely file path)")
        print("Value:", q5)
except NameError:
    print("var_functions.query_db:5 not found")

try:
    q6 = var_functions.query_db:6
    print("Found var_functions.query_db:6")
    print("Type:", type(q6))
    if isinstance(q6, str):
        print("It's a string (likely file path)")
        print("Value:", q6)
        # Try to load the data
        if".json" in q6:
            try:
                with open(q6, 'r') as f:
                    data = json.load(f)
                print("Records loaded:", len(data))
                print("First record:", data[0])
            except Exception as e:
                print("Error loading file:", str(e))
except NameError:
    print("var_functions.query_db:6 not found")

print("__RESULT__:")
print('"Variable check completed"')"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.list_db:2': ['Mutation_Data', 'RNASeq_Expression'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
