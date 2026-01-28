code = """import json
import re

path_papers = locals()['var_function-call-13071401018580020986']
with open(path_papers, 'r') as f:
    papers = json.load(f)

path_citations = locals()['var_function-call-12503289098151716023']
with open(path_citations, 'r') as f:
    citations = json.load(f)

# Build citation stats
citation_stats = {}
for c in citations:
    t = c['title']
    y = int(c['citation_year'])
    count = int(c['citation_count'])
    if t not in citation_stats:
        citation_stats[t] = {'min_year': y, 'total_count': 0, 'years': []}
    citation_stats[t]['min_year'] = min(citation_stats[t]['min_year'], y)
    citation_stats[t]['total_count'] += count
    citation_stats[t]['years'].append(y)

results = []
for p in papers:
    title = p['filename'].replace('.txt', '')
    stats = citation_stats.get(title, {'min_year': 'N/A', 'total_count': 0})
    
    is_empirical = 'empirical' in p.get('text', '').lower()
    
    # Try to find year in text for confirmation
    text = p.get('text', '')
    copyright_match = re.search(r'Copyright (20\d\d)', text)
    copyright_year = copyright_match.group(1) if copyright_match else "N/A"
    
    results.append({
        'title': title,
        'is_empirical': is_empirical,
        'min_citation_year': stats['min_year'],
        'total_citations': stats['total_count'],
        'copyright_year': copyright_year
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-6267193881023352391': 'file_storage/function-call-6267193881023352391.json', 'var_function-call-6267193881023352398': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-13071401018580018055': ['paper_docs'], 'var_function-call-13071401018580020986': 'file_storage/function-call-13071401018580020986.json', 'var_function-call-5244719068911348439': {'error': "[Errno 2] No such file or directory: 'var_function-call-13071401018580020986'"}, 'var_function-call-9288955964106777218': 'file_storage/function-call-9288955964106777218.json', 'var_function-call-12503289098151716023': 'file_storage/function-call-12503289098151716023.json', 'var_function-call-12161952385795619877': [], 'var_function-call-18122560194841091265': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 0, 'is_empirical': False, 'years_found': []}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 0, 'is_empirical': False, 'years_found': []}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 0, 'is_empirical': True, 'years_found': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 0, 'is_empirical': True, 'years_found': []}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 0, 'is_empirical': False, 'years_found': []}], 'var_function-call-13896871467980812711': {'title': 'A Lived Informatics Model of Personal Informatics.txt', 'text_start_repr': '"UBICOMP \'15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\\n\\nA Lived Informatics Model of Personal Informatics \\n\\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \\n1Computer Science & Engineering, 2Hu"', 'match': "<re.Match object; span=(29, 33), match='2015'>", 'p4_title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'p4_text_start': "'A Wee Bit More Interaction: Designing and Evaluating  \\nan Overactive Bladder App\\n\\nAna-Maria Salai \\n Heriot-Watt University \\n Edinburgh, UK \\n as152@hw.ac.uk \\n\\nLynne Baillie \\n Heriot-Watt University \\n E'", 'p4_match': 'None'}}

exec(code, env_args)
