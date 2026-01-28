code = """import json
import re

with open(locals()['var_function-call-8978544678357083899'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-9130584372251179173'], 'r') as f:
    citations = json.load(f)

print(f"Total papers: {len(papers)}")

def extract_year_robust(text):
    head = text[:2000]
    matches = re.findall(r'(20\d{2})', head)
    valid_years = [int(y) for y in matches if 2010 <= int(y) <= 2025]
    if valid_years:
        return valid_years[0]
    # Fallback to full text search if header is missing
    all_matches = re.findall(r'(20\d{2})', text)
    valid_all = [int(y) for y in all_matches if 2010 <= int(y) <= 2025]
    if valid_all:
        from collections import Counter
        return Counter(valid_all).most_common(1)[0][0]
    return None

relevant_titles = set()
for p in papers:
    title = p['filename'].replace('.txt', '')
    year = extract_year_robust(p['text'])
    is_emp = "empirical" in p['text'].lower()
    
    # print(f"Checking: {title}, Year: {year}, Emp: {is_emp}")
    
    if year and year > 2016 and is_emp:
        relevant_titles.add(title)

print(f"Relevant titles: {list(relevant_titles)}")

results = []
for t in relevant_titles:
    count = 0
    for c in citations:
        if c['title'] == t:
            count += int(c['citation_count'])
    results.append({"title": t, "citation_count": count})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-15050569047067534700': 'file_storage/function-call-15050569047067534700.json', 'var_function-call-3142892684795704503': 'file_storage/function-call-3142892684795704503.json', 'var_function-call-8978544678357083899': 'file_storage/function-call-8978544678357083899.json', 'var_function-call-9130584372251179173': 'file_storage/function-call-9130584372251179173.json', 'var_function-call-5001071914055655965': [], 'var_function-call-15001692400345327096': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'has_empirical': False}], 'var_function-call-684904427441614468': {'A Lived Informatics Model of Personal Informatics.txt': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, 'var_function-call-14593112564340639024': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 2010, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 2016, 'has_empirical': False}]}

exec(code, env_args)
