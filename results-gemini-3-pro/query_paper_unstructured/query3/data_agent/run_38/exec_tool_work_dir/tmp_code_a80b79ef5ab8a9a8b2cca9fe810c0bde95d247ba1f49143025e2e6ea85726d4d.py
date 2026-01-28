code = """import json
import re

with open(locals()['var_function-call-10956757805883297717'], 'r') as f:
    papers = json.load(f)

print("__DEBUG__")
for p in papers[:10]:
    title = p['filename']
    text = p['text']
    header = text[:1000]
    
    # Check Year
    years_4d = re.findall(r'\b(20\d\d)\b', header)
    years_2d = re.findall(r"'\d\d", header) # Matches '15
    
    # Check Empirical
    has_empirical = 'empirical' in text.lower()
    
    print(f"Title: {title}")
    print(f"  Years (4d): {years_4d}")
    print(f"  Years (2d): {years_2d}")
    print(f"  Has Empirical: {has_empirical}")
    print(f"  Header Start: {header[:50]}...")
    print("-" * 20)
print("__RESULT__:")
print("[]")"""

env_args = {'var_function-call-5688695509175081780': 'file_storage/function-call-5688695509175081780.json', 'var_function-call-5688695509175080773': 'file_storage/function-call-5688695509175080773.json', 'var_function-call-10956757805883297717': 'file_storage/function-call-10956757805883297717.json', 'var_function-call-12897874429475959915': []}

exec(code, env_args)
