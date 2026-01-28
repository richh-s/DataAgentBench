code = """import json
import pandas as pd

# Load citations
with open(locals()['var_function-call-12153821661542533629'], 'r') as f:
    citations_data = json.load(f)
citations_df = pd.DataFrame(citations_data)

# Load papers (IDs only is fine, but I need filenames)
# Actually I need to reload the full papers or just trust previous step. 
# I'll use the file from call-12153821661542534380
with open(locals()['var_function-call-12153821661542534380'], 'r') as f:
    papers_data = json.load(f)

paper_titles = [p['filename'].replace('.txt', '') for p in papers_data]

# Check intersection
matched_citations = citations_df[citations_df['title'].isin(paper_titles)]

print("__RESULT__:")
print(json.dumps({
    "paper_titles": paper_titles,
    "matched_titles": matched_citations['title'].tolist(),
    "matched_counts": matched_citations['citation_count'].tolist(),
    "average": matched_citations['citation_count'].astype(float).mean()
}))"""

env_args = {'var_function-call-12153821661542533629': 'file_storage/function-call-12153821661542533629.json', 'var_function-call-12153821661542534380': 'file_storage/function-call-12153821661542534380.json', 'var_function-call-7412265948695005483': 68.5, 'var_function-call-17202161529416673267': {'avg_loose': 68.5, 'avg_strict': 68.5, 'count_loose': 5, 'count_strict': 5}, 'var_function-call-11151052884622916441': {'citations_count': 158, 'papers_count': 5, 'sample_titles_citation': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Sundroid: Solar Radiation Awareness with Smartphones', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set'], 'sample_filenames_paper': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt']}, 'var_function-call-1480742075555364436': ['paper_docs'], 'var_function-call-1480742075555364811': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}]}

exec(code, env_args)
