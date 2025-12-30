code = """import json
import re

with open(locals()['var_function-call-9752705045220679725'], 'r') as f:
    docs = json.load(f)

debug_info = []

for doc in docs[:10]:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    
    header_text = text[:3000]
    
    copyright_match = re.search(r'Copyright\s+(?:©\s*)?(20\d{2})', header_text, re.IGNORECASE)
    conf_match = re.search(r"Conference\s+'(\d{2})", header_text, re.IGNORECASE)
    year_matches = re.findall(r'\b(20\d{2})\b', header_text)
    
    year = None
    source = "None"
    if copyright_match:
        year = int(copyright_match.group(1))
        source = "Copyright"
    elif conf_match:
        year = 2000 + int(conf_match.group(1))
        source = "Conference"
    elif year_matches:
        for y in year_matches:
            y_int = int(y)
            if 2000 <= y_int <= 2025:
                year = y_int
                source = "FirstMatch"
                break
    
    is_empirical = 'empirical' in text.lower()
    
    debug_info.append({
        "title": title,
        "year": year,
        "source": source,
        "is_empirical": is_empirical,
        "first_50_chars": text[:50]
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-17324318872041737699': 'file_storage/function-call-17324318872041737699.json', 'var_function-call-7414201362251444319': 'file_storage/function-call-7414201362251444319.json', 'var_function-call-9752705045220679725': 'file_storage/function-call-9752705045220679725.json', 'var_function-call-1938541816739605350': []}

exec(code, env_args)
