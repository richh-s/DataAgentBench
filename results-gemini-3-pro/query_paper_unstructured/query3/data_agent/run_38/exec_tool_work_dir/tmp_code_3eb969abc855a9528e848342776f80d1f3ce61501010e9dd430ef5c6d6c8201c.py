code = """import json
import re

with open(locals()['var_function-call-10956757805883297717'], 'r') as f:
    papers = json.load(f)

debug_info = []
for p in papers[:20]:
    title = p['filename']
    text = p['text']
    header = text[:1000]
    
    years_4d = re.findall(r'\b(20\d\d)\b', header)
    
    # Check for specific patterns like "CHI '17"
    venue_year_match = re.search(r"[A-Z]+\s*'?(\d\d)", header)
    venue_year = venue_year_match.group(1) if venue_year_match else None
    
    has_empirical = 'empirical' in text.lower()
    
    debug_info.append({
        "title": title,
        "years_4d": years_4d,
        "venue_year_2d": venue_year,
        "has_empirical": has_empirical,
        "header_snippet": header[:100]
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-5688695509175081780': 'file_storage/function-call-5688695509175081780.json', 'var_function-call-5688695509175080773': 'file_storage/function-call-5688695509175080773.json', 'var_function-call-10956757805883297717': 'file_storage/function-call-10956757805883297717.json', 'var_function-call-12897874429475959915': [], 'var_function-call-10123482125703570852': []}

exec(code, env_args)
