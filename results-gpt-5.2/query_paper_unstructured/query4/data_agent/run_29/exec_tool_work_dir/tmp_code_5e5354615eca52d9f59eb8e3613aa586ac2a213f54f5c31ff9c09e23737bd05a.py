code = """import json, re
import pandas as pd

def load_large(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path

filenames = var_call_vMmY3iW5Gn8iLDAQd00p2F7D
citations = load_large(var_call_2vHF50rivPHk1kUoUp21jfPJ)

cit_rows=[]
for r in citations:
    if isinstance(r, dict) and 'title' in r:
        cit_rows.append({'title': r['title'], 'total_citations': r.get('total_citations')})

cit_df=pd.DataFrame(cit_rows)
if not cit_df.empty:
    cit_df['total_citations']=pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

paper_titles=[re.sub(r'\.txt$','',d['filename']) for d in filenames]
paper_df=pd.DataFrame({'title': paper_titles}).drop_duplicates()

out=paper_df.merge(cit_df, on='title', how='left')
out['total_citations']=out['total_citations'].fillna(0).astype(int)
out=out.sort_values(['total_citations','title'], ascending=[False, True])

print('__RESULT__:')
print(json.dumps(out[['title','total_citations']].to_dict('records')))"""

env_args = {'var_call_BW98amLhBde79shV1uZfDXuX': 'file_storage/call_BW98amLhBde79shV1uZfDXuX.json', 'var_call_2vHF50rivPHk1kUoUp21jfPJ': 'file_storage/call_2vHF50rivPHk1kUoUp21jfPJ.json', 'var_call_2nJKYCMhuHeRaPulVH626vn4': [], 'var_call_vMmY3iW5Gn8iLDAQd00p2F7D': [{'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt'}, {'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt"}, {'filename': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt'}, {'filename': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt'}, {'filename': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure.txt"}, {'filename': 'Technologies for Everyday Life Reflection: Illustrating a Design Space.txt'}, {'filename': 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating.txt'}]}

exec(code, env_args)
