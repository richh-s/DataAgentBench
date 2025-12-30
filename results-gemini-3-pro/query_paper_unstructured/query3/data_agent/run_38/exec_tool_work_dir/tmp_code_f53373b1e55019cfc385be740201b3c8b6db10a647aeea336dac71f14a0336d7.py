code = """import json
import re

with open(locals()['var_function-call-10956757805883297717'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-5688695509175081780'], 'r') as f:
    citations_data = json.load(f)

# Build map: title -> total_citations
cit_map = {c['title']: int(c['total_citations']) for c in citations_data}

results = []

for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p['text']
    
    # Extract Year
    # 1. Look in first 2000 chars (Header)
    # 2. Look in last 2000 chars (Footer/Copyright)
    search_text = text[:2000] + "\n" + text[-2000:]
    
    # Regex for "Year 20xx" or "Copyright 20xx" or "Venue 'xx"
    # We are looking for > 2016, so 2017-2024
    
    # Check for 4-digit years in specific range
    years = [int(y) for y in re.findall(r'\b(201[7-9]|202[0-4])\b', search_text)]
    
    # Check for 2-digit years '17, '18...
    # Must be preceded by space or '
    years_2d = [int("20"+y) for y in re.findall(r"'\s*(1[7-9]|2[0-4])\b", search_text)]
    
    all_years = years + years_2d
    
    if not all_years:
        continue
    
    # Pick the most frequent year? Or the max?
    # Usually the publication year is consistent.
    # If we have 2017 and 2018 (e.g. copyright 2017, published 2018?), take the one that appears most or matches a venue?
    # Let's take the set of found years. If any is > 2016, we consider the paper.
    # But we must be sure it's the PUBLICATION year, not a reference.
    # Limiting to Header/Footer reduces reference noise.
    # Let's assume the Max year in Header/Footer is the publication year (or close enough).
    pub_year = max(all_years)
    
    if pub_year <= 2016:
        continue

    # Extract Contribution
    # Check for "empirical"
    if 'empirical' in text.lower():
        # Match found
        # Get citations
        total = cit_map.get(title, 0)
        results.append({
            "title": title,
            "total_citations": total
        })

# Sort
results.sort(key=lambda x: x['total_citations'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5688695509175081780': 'file_storage/function-call-5688695509175081780.json', 'var_function-call-5688695509175080773': 'file_storage/function-call-5688695509175080773.json', 'var_function-call-10956757805883297717': 'file_storage/function-call-10956757805883297717.json', 'var_function-call-12897874429475959915': [], 'var_function-call-10123482125703570852': [], 'var_function-call-4464588429009855954': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'years_4d': [], 'venue_year_2d': '15', 'has_empirical': False, 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'years_4d': [], 'venue_year_2d': '15', 'has_empirical': False, 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_4d': [], 'venue_year_2d': None, 'has_empirical': True, 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years_4d': [], 'venue_year_2d': None, 'has_empirical': True, 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'years_4d': [], 'venue_year_2d': None, 'has_empirical': False, 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation '}]}

exec(code, env_args)
