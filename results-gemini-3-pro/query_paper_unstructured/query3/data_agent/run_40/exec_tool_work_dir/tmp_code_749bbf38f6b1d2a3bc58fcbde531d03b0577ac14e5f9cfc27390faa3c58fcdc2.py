code = """import json
import re

try:
    with open(locals()['var_function-call-1634184987777097794'], 'r') as f:
        papers = json.load(f)
except Exception as e:
    papers = []

debug_info = []
for paper in papers[:10]:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    header = text[:1000]
    years = re.findall(r'\b(20\d{2})\b', header)
    valid_years = [int(y) for y in years if 2000 <= int(y) <= 2024]
    short_years = re.findall(r"\b'([12]\d)\b", header)
    for sy in short_years:
        valid_years.append(2000 + int(sy))
    
    year = valid_years[0] if valid_years else None
    
    is_empirical = 'empirical' in text.lower()
    
    debug_info.append({
        "filename": filename,
        "extracted_year": year,
        "is_empirical": is_empirical,
        "header_snippet": header[:200]
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-4642845267965044101': ['paper_docs'], 'var_function-call-4642845267965042778': ['Citations', 'sqlite_sequence'], 'var_function-call-10467492128798022417': 'file_storage/function-call-10467492128798022417.json', 'var_function-call-1634184987777097794': 'file_storage/function-call-1634184987777097794.json', 'var_function-call-15997797269268972557': []}

exec(code, env_args)
