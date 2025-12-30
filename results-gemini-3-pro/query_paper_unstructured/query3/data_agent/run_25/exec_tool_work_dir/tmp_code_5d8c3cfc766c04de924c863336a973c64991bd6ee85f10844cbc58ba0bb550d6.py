code = """import json
import re

with open(locals()['var_function-call-15606477523093127544'], 'r') as f:
    docs = json.load(f)

matching_titles = []

for doc in docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    
    # Year Extraction
    # 1. Look for Copyright line
    copyright_year = 0
    copyright_matches = re.findall(r"(?:Copyright|©)\s*(?:19|20)(\d{2})", text, re.IGNORECASE)
    if copyright_matches:
        # Take the last one found? Or first? usually copyright is at start or end.
        # But references might have copyright notices? unlikely.
        # Let's take the year that appears in the context of "ACM" or "IEEE" if possible?
        # Simple approach: max year found in copyright? No, might be 2024 if re-published.
        # Usually the publication year is the one in "Copyright 20xx ACM".
        # Let's use the year from the first Copyright match found in first/last 2000 chars.
        candidates = []
        snippets = text[:2000] + "\n" + text[-2000:]
        c_matches = re.findall(r"(?:Copyright|©|ACM|IEEE)\s+(?:19|20)(\d{2})", snippets, re.IGNORECASE)
        if c_matches:
            copyright_year = int("20" + c_matches[0])
    
    # 2. Look for Conference Year patterns like "CHI '17", "CHI 2017"
    conf_year = 0
    conf_matches = re.findall(r"(?:CHI|UbiComp|CSCW|DIS|IUI)\s*'?(\d{2})", text[:1000], re.IGNORECASE)
    if conf_matches:
        conf_year = int("20" + conf_matches[0])
    
    # 3. Look for just "20xx" in the first 200 chars (header)
    header_year = 0
    h_matches = re.findall(r"20(\d{2})", text[:300])
    if h_matches:
        header_year = int("20" + h_matches[0])

    # Decision logic for year
    if conf_year > 0:
        year = conf_year
    elif copyright_year > 0:
        year = copyright_year
    elif header_year > 0:
        year = header_year
    else:
        # Fallback: check footer for year
        footer_matches = re.findall(r"20(\d{2})", text[-500:])
        if footer_matches:
            year = int("20" + footer_matches[-1]) # take the last one
        else:
            year = 0

    # Empirical Check
    text_lower = text.lower()
    is_empirical = False
    
    # Heuristics
    keywords = ["empirical", "user study", "field study", "participants", "interviews", "surveys", "experiment"]
    # Check if any keyword is present
    # But "participants" is very common.
    # The prompt says "empirical" is a contribution type.
    # Let's be reasonably strict: "empirical" OR ("study" AND "participants") OR "user study".
    
    if "empirical" in text_lower:
        is_empirical = True
    elif "user study" in text_lower:
        is_empirical = True
    elif "study" in text_lower and ("participant" in text_lower or "interview" in text_lower or "recruit" in text_lower):
        is_empirical = True
    
    # Filter
    if year > 2016 and is_empirical:
        matching_titles.append(title)

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-4403390195297864469': 'file_storage/function-call-4403390195297864469.json', 'var_function-call-5079307557547688021': ['paper_docs'], 'var_function-call-3097430276196367090': 'file_storage/function-call-3097430276196367090.json', 'var_function-call-5206321841837773326': {'has_empirical': False, 'has_survey': True, 'has_interview': True, 'has_study': True}, 'var_function-call-3687296208506163854': [], 'var_function-call-5857355116469077971': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-4539730163481461020': 'file_storage/function-call-4539730163481461020.json', 'var_function-call-10637637580937536300': {'total_docs': 5, 'docs_after_2016': 0, 'docs_after_2016_with_empirical': 0, 'docs_after_2016_with_study': 0, 'examples_empirical': []}, 'var_function-call-15606477523093127544': 'file_storage/function-call-15606477523093127544.json', 'var_function-call-6095849557644838005': [], 'var_function-call-835920876180923776': 'file_storage/function-call-835920876180923776.json'}

exec(code, env_args)
