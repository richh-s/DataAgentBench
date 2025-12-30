code = """import json

file_path = locals()['var_function-call-2784456045421474973']
with open(file_path, 'r') as f:
    papers = json.load(f)

matches = []
keyword_samples = []

for paper in papers:
    text = paper.get('text', '')
    text_lower = text.lower()
    
    # Check if food is in text
    if 'food' in text_lower:
        matches.append(paper['filename'])
        
    # Debug keyword extraction
    start_idx = text_lower.find('author keywords')
    if start_idx != -1:
        chunk = text[start_idx:start_idx+200] # Get original case for display
        keyword_samples.append(chunk)

print("__RESULT__:")
print(json.dumps({"food_in_text_count": len(matches), "food_in_text_samples": matches[:5], "keyword_samples": keyword_samples[:3]}))"""

env_args = {'var_function-call-16691690145892377259': 'file_storage/function-call-16691690145892377259.json', 'var_function-call-2784456045421474973': 'file_storage/function-call-2784456045421474973.json', 'var_function-call-6442636259754716830': []}

exec(code, env_args)
