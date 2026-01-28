code = """import json, re
path = var_call_YsLRlcU3h7irQLHPdx5tyH09
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

candidates = []
for d in docs:
    filename = d.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text','')
    # detect physical activity domain: either exact phrase or physical and activity within 40 chars
    phys_act = bool(re.search(r'physical\s*activity', text, re.IGNORECASE) or re.search(r'physical.{0,40}activity', text, re.IGNORECASE))
    # find publication year: look in first 500 chars for 20xx or patterns like CHI'16 or CHI 2016
    head = text[:1000]
    year = None
    m = re.search(r"\b(20\d{2}|19\d{2})\b", head)
    if m:
        year = int(m.group(1))
    else:
        # search whole text
        m2 = re.search(r"\b(20\d{2}|19\d{2})\b", text)
        if m2:
            year = int(m2.group(1))
    # also handle patterns like CHI'16 or CHI 16
    if year is None:
        m3 = re.search(r"'?(\d{2})\b", head)
        if m3:
            yy = int(m3.group(1))
            if yy >= 90:
                year = 1900 + yy
            else:
                year = 2000 + yy
    candidates.append({'title': title, 'year_found': year, 'phys_activity': phys_act})

# filter for year==2016 and phys_activity True
selected = [c['title'] for c in candidates if c['year_found']==2016 and c['phys_activity']]
# If none found, try a relaxed match: year anywhere ==2016 and phys_activity True
if not selected:
    selected = [c['title'] for c in candidates if c['phys_activity'] and (c['year_found']==2016 or (c['year_found'] is None and re.search(r"\\b2016\\b", ''.join(d.get('text','') for d in docs))))]

output = {'selected_titles': selected, 'all_candidates': candidates}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_H8MR8XiAJQcwfwjUzIUnvAZp': ['paper_docs'], 'var_call_abt9r2WlD9FlUNBcOscHzbCD': ['Citations', 'sqlite_sequence'], 'var_call_w2Nv7UgCjiHN6I6HYUjZ4I6P': 'file_storage/call_w2Nv7UgCjiHN6I6HYUjZ4I6P.json', 'var_call_riAVJQvz9VqLp676ohi9NTRg': {'titles': [], 'count': 0}, 'var_call_YsLRlcU3h7irQLHPdx5tyH09': 'file_storage/call_YsLRlcU3h7irQLHPdx5tyH09.json', 'var_call_5mYX0mpwlu8bYcXV637tyzmA': {'total_docs_returned': 5, 'filtered_count': 5, 'examples': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'has_physical': True, 'has_activity': True, 'years_found': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'has_physical': True, 'has_activity': True, 'years_found': []}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'has_physical': True, 'has_activity': True, 'years_found': []}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'has_physical': True, 'has_activity': True, 'years_found': []}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'has_physical': True, 'has_activity': True, 'years_found': []}]}, 'var_call_TK3JQI6Id2pLwK9jSQUsh30p': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'has_physical_activity': True, 'has_2016': False, 'snippets_2016': ['Guimbetiere, and Tanzeem Choudhury. 2016.', '2016 ACM International Joint Conference on P', '24. Akane Sano. 2016. Measuring college students’ sleep,'], 'snippets_phys': ['course of a day, including physical activity and sleep activity']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'has_physical_activity': True, 'has_2016': False, 'snippets_2016': ['Coninx. 2016. Back on bike: the BoB mobile cycling a', '2016.  A  longitudinal evaluation  of  the  ', ' James Clawson and Elizabeth D. Mynatt. 2016. A Cancer ', ',  Lynne  Baillie  and  Stephen  Uzor.  2016.  Time  to ', '[43]  My  pelvic  floor  Fitness.  2016.  http://www.lightsbytena.co.uk/my-'], 'snippets_phys': ['acceleration  for  the physical activity recognition of bipolar ']}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'has_physical_activity': False, 'has_2016': False, 'snippets_2016': ['DIS 2016, June 04 - 08, 2016, Brisbane, QLD, Australia ', 'Sensing, HealthDIS 2016, June 4–8, 2016, Brisbane, Australia700 ', 'Sensing, HealthDIS 2016, June 4–8, 2016, Brisbane, Australia701\x0cRESEARCH SETTIN', 'Sensing, HealthDIS 2016, June 4–8, 2016, Brisbane, Australia702\x0chis  hand.  I  ', "Sensing, HealthDIS 2016, June 4–8, 2016, Brisbane, Australia703\x0cthey don't "], 'snippets_phys': []}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'has_physical_activity': True, 'has_2016': False, 'snippets_2016': ["CHI'16, May 07-12, 2016, San Jose, CA, USA  ", '© 2016 ACM. ISBN 978-1-4503-3362-7/16/05…$15.0', 'Living Healthy#chi4good, CHI 2016, San Jose, CA, USA1109 ', 'Living Healthy#chi4good, CHI 2016, San Jose, CA, USA1110 ', 'Living Healthy#chi4good, CHI 2016, San Jose, CA, USA1111 '], 'snippets_phys': ['y 193 people who formerly tracked their physical \nactivity,  finances,  or  location,  conduct  12', ' addiction  [2].  In  the  domains  of  physical \nactivity and health and wellness more broadly, r', 'who had tracked their physical activity, finances, and location ', 'mpensation).  Of  people  who  tracked  physical \nactivity,  finances,  and  location,  64,  61,  ', 'my  physical  activity.”  Like  p55,  most  who  started  out ']}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'has_physical_activity': True, 'has_2016': False, 'snippets_2016': ['The interviews, held in spring 2016, were semi-structured, ', '\x0csession,  held  in  autumn  2016,  lasted  2  hours  and  was ', 'centers,  in  autumn  2016.  Two  clients,  recruited  by  the ', ' S.  Kirk,  and  Abigail  C.  Durrant.  2016.  A ', '[19]  Jordan  Etkin.  2016.  The  Hidden  Cost  of  Personal  Quan'], 'snippets_phys': ['goals,  by  focusing  on  diet,  physical  activity,  or  both.  We ', 'physical activity, nutrition, (…) and I only get half of ', '(e.g.,  nutrition,  physical  activity)  is  key  for  successful ', 'their  physical  activity  and  healthy  eating  behaviours:  the']}]}

exec(code, env_args)
