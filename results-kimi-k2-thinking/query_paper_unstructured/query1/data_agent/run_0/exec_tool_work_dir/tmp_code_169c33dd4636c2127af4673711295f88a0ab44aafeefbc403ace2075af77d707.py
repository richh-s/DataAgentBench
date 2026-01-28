code = """# First, let's see what variables are available
import json
import os

print('Checking available variables...')
available = [v for v in dir() if v.startswith('var_')]
print('Available variables:', available)

# Load the MongoDB results
# The results should be in var_functions.query_db:2 or var_functions.query_db:4
mongo_result = None

if 'var_functions.query_db:4' in dir():
    result_var = var_functions.query_db:4
    print('var_functions.query_db:4 type:', type(result_var))
    if isinstance(result_var, str) and os.path.exists(result_var):
        with open(result_var, 'r') as f:
            mongo_result = json.load(f)
        print('Loaded data from file, count:', len(mongo_result))

if not mongo_result and 'var_functions.query_db:2' in dir():
    result_var = var_functions.query_db:2
    print('var_functions.query_db:2 type:', type(result_var))
    if isinstance(result_var, str) and os.path.exists(result_var):
        with open(result_var, 'r') as f:
            mongo_result = json.load(f)
        print('Loaded data from file, count:', len(mongo_result))

print('Mongo result loaded:', mongo_result is not None)

# Extract paper titles and identify food domain papers
if mongo_result:
    food_titles = []
    for doc in mongo_result:
        filename = doc.get('filename', '')
        text = doc.get('text', '')
        
        # Extract title from filename
        title = filename.replace('.txt', '')
        
        # Check if it's a food domain paper
        # Look for food-related keywords in context
        text_lower = text.lower()
        food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'calorie', 'dietary']
        
        for keyword in food_keywords:
            if keyword in text_lower:
                # Check if it appears in research context
                if 'domain' in text_lower or 'track' in text_lower:
                    food_titles.append(title)
                    break
    
    print('Found food domain papers:', len(food_titles))
    print('Sample titles:', food_titles[:5])
else:
    food_titles = []
    print('No MongoDB data found')

# Prepare result
output = {'food_paper_titles': food_titles, 'count': len(food_titles)}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence']}

exec(code, env_args)
