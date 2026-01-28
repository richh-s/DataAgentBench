code = """import json
import re

# Load the data from the file
file_path = var_functions.query_db:6
results = []
try:
    with open(file_path, 'r') as f:
        results = json.load(f)
except:
    # Try direct value if not a file
    results = var_functions.query_db:6

print(f"Total UNIV CALIFORNIA patents: {len(results)}")

# Let's look at the structure of Patents_info
if results:
    print("Sample Patents_info structures:")
    for i in range(min(5, len(results))):
        info_str = results[i].get('Patents_info', '')
        print(f"  {i}: {info_str[:200]}...")
        
        # Try to extract assignee
        # Looking for patterns like "owned by", "assigned to", "assigned to", "holds" followed by assignee name
        patterns = [
            r'(?:owned by|assigned to|assigned to|holds|is owned by|is assigned to)\s+([A-Z][A-Z0-9\s\.\,&\(\)\-]+?)(?:\.|,|\sand\s|\sor\s|\swith\s|\swhich\s)',
            r'by\s+([A-Z][A-Z0-9\s\.\,&\(\)\-]+?)\s+(?:holds|owns|is assigned)'
        ]
        
        assignee = None
        for pattern in patterns:
            matches = re.findall(pattern, info_str, re.IGNORECASE)
            if matches:
                assignee = matches[0].strip()
                if assignee:
                    print(f"    Extracted assignee: {assignee}")
                    break
        
        if not assignee:
            print(f"    Could not extract assignee from: {info_str}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:11': ['cpc_definition']}

exec(code, env_args)
