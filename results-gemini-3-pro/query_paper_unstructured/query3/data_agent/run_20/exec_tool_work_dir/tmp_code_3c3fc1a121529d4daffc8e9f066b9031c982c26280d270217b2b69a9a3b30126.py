code = """import json
import re

with open(locals()['var_function-call-389901141376174398'], 'r') as f:
    citations_data = json.load(f)

with open(locals()['var_function-call-389901141376172653'], 'r') as f:
    papers_data = json.load(f)

debug_info = []
debug_info.append(f"Num citations: {len(citations_data)}")
debug_info.append(f"Num papers: {len(papers_data)}")

for i, paper in enumerate(papers_data[:5]):
    filename = paper.get('filename', '')
    title = filename[:-4] if filename.endswith('.txt') else filename
    text = paper.get('text', '')
    match = re.search(r'20\d{2}', text[:1000])
    year = int(match.group(0)) if match else 0
    has_empirical = 'empirical' in text.lower()
    
    debug_info.append({
        "title": title,
        "year": year,
        "has_empirical": has_empirical,
        "snippet": text[:100]
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-11261961701334828073': ['paper_docs'], 'var_function-call-11261961701334829364': 'file_storage/function-call-11261961701334829364.json', 'var_function-call-11261961701334830655': ['Citations', 'sqlite_sequence'], 'var_function-call-11261961701334827850': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-8802837961524065341': 'file_storage/function-call-8802837961524065341.json', 'var_function-call-389901141376174398': 'file_storage/function-call-389901141376174398.json', 'var_function-call-389901141376172653': 'file_storage/function-call-389901141376172653.json', 'var_function-call-8584235094798493494': [], 'var_function-call-10819417574072414189': []}

exec(code, env_args)
