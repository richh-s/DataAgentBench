code = """import re, json
import pandas as pd

mongo_path = var_call_9c8KG0T3EbdOXzTs9FF7LNJP
sql_path = var_call_d2ZdtbKgYAqkTDQT3dG7Moav

with open(mongo_path, 'r') as f:
    mongo_records = json.load(f)
with open(sql_path, 'r') as f:
    sql_records = json.load(f)

records = []
for doc in mongo_records:
    text = doc.get('text', '')
    years = re.findall(r'(20[1-2][0-9])', text)
    year_val = None
    for y in years:
        yi = int(y)
        if 2010 <= yi <= 2025:
            year_val = yi
            break
    contrib = 'empirical' if re.search(r'empirical', text, re.IGNORECASE) else None
    if contrib == 'empirical' and year_val is not None and year_val > 2016:
        filename = doc.get('filename', '')
        title = re.sub(r'\.txt$', '', filename)
        records.append({'title_paper': title, 'year': year_val})

papers_df = pd.DataFrame(records).drop_duplicates(subset=['title_paper'])

cit_df = pd.DataFrame(sql_records)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

cit_df['title_clean'] = cit_df['title'].str.strip('"')
papers_df['title_clean'] = papers_df['title_paper']

merged = pd.merge(papers_df, cit_df, on='title_clean', how='left')

result = merged[['title_paper', 'total_citations']].dropna(subset=['total_citations']).sort_values('title_paper').to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_9c8KG0T3EbdOXzTs9FF7LNJP': 'file_storage/call_9c8KG0T3EbdOXzTs9FF7LNJP.json', 'var_call_d2ZdtbKgYAqkTDQT3dG7Moav': 'file_storage/call_d2ZdtbKgYAqkTDQT3dG7Moav.json', 'var_call_pS4DSyYrxOtq7l0xAIxepVOz': {'papers_count': 20, 'cit_cols': ['title', 'total_citations']}, 'var_call_mGVhBbF7o9F0TIRxpvRJr99N': {'merged_cols': ['title_paper', 'year', 'title_clean', 'title_cit', 'total_citations'], 'sample': [{'title_paper': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'title_clean': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'title_cit': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}, {'title_paper': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'title_clean': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'title_cit': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title_paper': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'year': 2018, 'title_clean': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'title_cit': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'total_citations': 402}, {'title_paper': 'Communicating Uncertainty in Fertility Prognosis', 'year': 2019, 'title_clean': 'Communicating Uncertainty in Fertility Prognosis', 'title_cit': 'Communicating Uncertainty in Fertility Prognosis', 'total_citations': 264}, {'title_paper': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'year': 2018, 'title_clean': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'title_cit': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'total_citations': 362}, {'title_paper': 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game', 'year': 2018, 'title_clean': 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game', 'title_cit': 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game', 'total_citations': 97}, {'title_paper': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'year': 2019, 'title_clean': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'title_cit': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citations': 133}, {'title_paper': 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'year': 2018, 'title_clean': 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'title_cit': 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'total_citations': 153}, {'title_paper': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'year': 2018, 'title_clean': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'title_cit': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'total_citations': 316}, {'title_paper': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'year': 2017, 'title_clean': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'title_cit': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'total_citations': 327}]}}

exec(code, env_args)
