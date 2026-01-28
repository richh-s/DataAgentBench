code = """import json, re
# Load MongoDB query result file
path = var_call_YsLRlcU3h7irQLHPdx5tyH09
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# citations list from previous SQL query
citations = var_call_GT5jRTuqRnlwfgTtlevj6DtI
cit_map = {rec['title']: int(rec['total_citations']) for rec in citations}

titles_of_interest = list(cit_map.keys())
patterns = [r"©\s*2016", r"\b2016\b", r"CHI\W?16", r"CHI\W?2016", r"DIS\W?2016", r"CHI'16", r"CHI 2016", r"ACM.*2016", r"2016 ACM"]

results = []
for d in docs:
    filename = d.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    if title in titles_of_interest:
        text = d.get('text','')
        text_low = text.lower()
        head = text[:3000]
        matches = []
        for pat in patterns:
            for m in re.finditer(pat, head, re.IGNORECASE):
                start = max(0, m.start()-60)
                end = min(len(text), m.end()+60)
                ctx = text[start:end].replace('\n',' ')
                matches.append({'pattern': pat, 'match': m.group(0), 'context': ctx})
        # also search whole text for year lines like 'CHI 2016' beyond head
        for pat in [r"CHI\W?2016", r"DIS\W?2016", r"CHI'16"]:
            for m in re.finditer(pat, text, re.IGNORECASE):
                start = max(0, m.start()-60)
                end = min(len(text), m.end()+60)
                ctx = text[start:end].replace('\n',' ')
                if all(ctx != ex['context'] for ex in matches):
                    matches.append({'pattern': pat, 'match': m.group(0), 'context': ctx})
        pa_matches = []
        for m in re.finditer(r'physical\s*activity', text, re.IGNORECASE):
            start = max(0, m.start()-60)
            end = min(len(text), m.end()+60)
            pa_matches.append(text[start:end].replace('\n',' '))
        results.append({'title': title, 'pub_2016_matches': matches, 'found_pub_2016': len(matches)>0, 'physical_activity_count': len(pa_matches), 'physical_activity_examples': pa_matches[:5], 'total_citations': cit_map.get(title)})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_H8MR8XiAJQcwfwjUzIUnvAZp': ['paper_docs'], 'var_call_abt9r2WlD9FlUNBcOscHzbCD': ['Citations', 'sqlite_sequence'], 'var_call_w2Nv7UgCjiHN6I6HYUjZ4I6P': 'file_storage/call_w2Nv7UgCjiHN6I6HYUjZ4I6P.json', 'var_call_riAVJQvz9VqLp676ohi9NTRg': {'titles': [], 'count': 0}, 'var_call_YsLRlcU3h7irQLHPdx5tyH09': 'file_storage/call_YsLRlcU3h7irQLHPdx5tyH09.json', 'var_call_5mYX0mpwlu8bYcXV637tyzmA': {'total_docs_returned': 5, 'filtered_count': 5, 'examples': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'has_physical': True, 'has_activity': True, 'years_found': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'has_physical': True, 'has_activity': True, 'years_found': []}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'has_physical': True, 'has_activity': True, 'years_found': []}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'has_physical': True, 'has_activity': True, 'years_found': []}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'has_physical': True, 'has_activity': True, 'years_found': []}]}, 'var_call_TK3JQI6Id2pLwK9jSQUsh30p': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'has_physical_activity': True, 'has_2016': False, 'snippets_2016': ['Guimbetiere, and Tanzeem Choudhury. 2016.', '2016 ACM International Joint Conference on P', '24. Akane Sano. 2016. Measuring college students’ sleep,'], 'snippets_phys': ['course of a day, including physical activity and sleep activity']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'has_physical_activity': True, 'has_2016': False, 'snippets_2016': ['Coninx. 2016. Back on bike: the BoB mobile cycling a', '2016.  A  longitudinal evaluation  of  the  ', ' James Clawson and Elizabeth D. Mynatt. 2016. A Cancer ', ',  Lynne  Baillie  and  Stephen  Uzor.  2016.  Time  to ', '[43]  My  pelvic  floor  Fitness.  2016.  http://www.lightsbytena.co.uk/my-'], 'snippets_phys': ['acceleration  for  the physical activity recognition of bipolar ']}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'has_physical_activity': False, 'has_2016': False, 'snippets_2016': ['DIS 2016, June 04 - 08, 2016, Brisbane, QLD, Australia ', 'Sensing, HealthDIS 2016, June 4–8, 2016, Brisbane, Australia700 ', 'Sensing, HealthDIS 2016, June 4–8, 2016, Brisbane, Australia701\x0cRESEARCH SETTIN', 'Sensing, HealthDIS 2016, June 4–8, 2016, Brisbane, Australia702\x0chis  hand.  I  ', "Sensing, HealthDIS 2016, June 4–8, 2016, Brisbane, Australia703\x0cthey don't "], 'snippets_phys': []}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'has_physical_activity': True, 'has_2016': False, 'snippets_2016': ["CHI'16, May 07-12, 2016, San Jose, CA, USA  ", '© 2016 ACM. ISBN 978-1-4503-3362-7/16/05…$15.0', 'Living Healthy#chi4good, CHI 2016, San Jose, CA, USA1109 ', 'Living Healthy#chi4good, CHI 2016, San Jose, CA, USA1110 ', 'Living Healthy#chi4good, CHI 2016, San Jose, CA, USA1111 '], 'snippets_phys': ['y 193 people who formerly tracked their physical \nactivity,  finances,  or  location,  conduct  12', ' addiction  [2].  In  the  domains  of  physical \nactivity and health and wellness more broadly, r', 'who had tracked their physical activity, finances, and location ', 'mpensation).  Of  people  who  tracked  physical \nactivity,  finances,  and  location,  64,  61,  ', 'my  physical  activity.”  Like  p55,  most  who  started  out ']}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'has_physical_activity': True, 'has_2016': False, 'snippets_2016': ['The interviews, held in spring 2016, were semi-structured, ', '\x0csession,  held  in  autumn  2016,  lasted  2  hours  and  was ', 'centers,  in  autumn  2016.  Two  clients,  recruited  by  the ', ' S.  Kirk,  and  Abigail  C.  Durrant.  2016.  A ', '[19]  Jordan  Etkin.  2016.  The  Hidden  Cost  of  Personal  Quan'], 'snippets_phys': ['goals,  by  focusing  on  diet,  physical  activity,  or  both.  We ', 'physical activity, nutrition, (…) and I only get half of ', '(e.g.,  nutrition,  physical  activity)  is  key  for  successful ', 'their  physical  activity  and  healthy  eating  behaviours:  the']}], 'var_call_cqfeyE6P6MT2FKyXiDOKMchy': {'selected_titles': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching"], 'all_candidates': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year_found': None, 'phys_activity': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year_found': None, 'phys_activity': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year_found': None, 'phys_activity': False}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'year_found': None, 'phys_activity': True}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'year_found': None, 'phys_activity': True}]}, 'var_call_GT5jRTuqRnlwfgTtlevj6DtI': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': '636'}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'total_citations': '271'}], 'var_call_vkk5DwU3mjXO5bAD2oOOydJ7': []}

exec(code, env_args)
