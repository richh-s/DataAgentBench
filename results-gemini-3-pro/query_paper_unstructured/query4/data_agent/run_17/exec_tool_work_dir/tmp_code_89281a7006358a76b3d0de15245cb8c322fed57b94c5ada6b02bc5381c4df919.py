code = """import json
import re

papers_file = locals()['var_function-call-3120307728303997294']

with open(papers_file, 'r') as f:
    papers_data = json.load(f)

debug_info = []
count_2016 = 0
count_phy_act = 0

for i, paper in enumerate(papers_data):
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    header = text[:500]
    
    has_2016 = bool(re.search(r'\b2016\b', header))
    has_phy_act = 'physical activity' in text.lower()
    
    if has_2016:
        count_2016 += 1
    if has_phy_act:
        count_phy_act += 1
        
    if i < 5:
        debug_info.append({
            "filename": filename,
            "header_preview": header.replace('\n', ' ')[:100],
            "has_2016": has_2016,
            "has_phy_act": has_phy_act
        })

print("__RESULT__:")
print(json.dumps({
    "total_papers": len(papers_data),
    "count_2016_header": count_2016,
    "count_phy_act": count_phy_act,
    "samples": debug_info
}))"""

env_args = {'var_function-call-14316968101871802559': ['paper_docs'], 'var_function-call-14316968101871802262': ['Citations', 'sqlite_sequence'], 'var_function-call-637640979100223299': 'file_storage/function-call-637640979100223299.json', 'var_function-call-1625396781395039115': 'file_storage/function-call-1625396781395039115.json', 'var_function-call-3120307728303997294': 'file_storage/function-call-3120307728303997294.json', 'var_function-call-14472908731975527772': []}

exec(code, env_args)
