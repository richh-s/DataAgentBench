code = """import json
import re
import pandas as pd

# Load Funding Data
with open(locals()['var_function-call-9061716743711808369'], 'r') as f:
    funding_data = json.load(f)

# Load Civic Docs
with open(locals()['var_function-call-12561724733303725061'], 'r') as f:
    civic_docs = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(int)

def get_base_name(name):
    name = re.sub(r'\s*\(FEMA.*?\)', '', name)
    name = re.sub(r'\s*\(CalOES.*?\)', '', name)
    name = re.sub(r'\s*\(CalJPIA.*?\)', '', name)
    name = re.sub(r'\s*\(FEMA\)', '', name)
    return name.strip()

funding_df['base_name'] = funding_df['Project_Name'].apply(get_base_name)
unique_base_names = funding_df['base_name'].unique()

project_details = {}

for doc in civic_docs:
    text = doc.get('text', '')
    # simple normalization without using backslash n
    text = " ".join(text.splitlines())
    
    for base_name in unique_base_names:
        if base_name.lower() in ['discussion', 'agenda', 'item', 'subject', 'report']:
            continue
            
        if base_name in project_details and project_details[base_name].get('start_year'):
            continue
            
        if base_name in text:
            pattern = re.escape(base_name)
            for match in re.finditer(pattern, text):
                start_idx = match.end()
                snippet = text[start_idx : start_idx + 2000]
                
                start_year = None
                
                # Check for "Begin Construction"
                date_match = re.search(r'Begin [Cc]onstruction:?\s*([A-Za-z0-9, ]+)', snippet)
                if date_match:
                    date_str = date_match.group(1)
                    y_match = re.search(r'20\d{2}', date_str)
                    if y_match:
                        start_year = int(y_match.group(0))
                
                # Check for Disaster keywords
                is_disaster_text = False
                keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Woolsey Fire', 'Disaster', 'Emergency']
                for kw in keywords:
                    if kw.lower() in snippet.lower():
                        is_disaster_text = True
                        break
                
                if start_year or is_disaster_text:
                    if base_name not in project_details:
                         project_details[base_name] = {'start_year': start_year, 'is_disaster_text': is_disaster_text}
                    else:
                        if start_year:
                            project_details[base_name]['start_year'] = start_year
                        if is_disaster_text:
                            project_details[base_name]['is_disaster_text'] = True
                
                if start_year:
                    break

total_funding = 0
debug_list = []

for _, row in funding_df.iterrows():
    base_name = row['base_name']
    if base_name.lower() in ['discussion', 'agenda', 'item', 'subject', 'report']:
        continue

    amount = row['Amount']
    orig_name = row['Project_Name']
    
    is_disaster_name = any(x in orig_name for x in ['FEMA', 'CalOES', 'CalJPIA'])
    
    details = project_details.get(base_name, {})
    is_disaster_text = details.get('is_disaster_text', False)
    start_year = details.get('start_year')
    
    is_disaster = is_disaster_name or is_disaster_text
    
    if is_disaster and start_year == 2022:
        total_funding += amount
        debug_list.append({'Project': orig_name, 'Amount': amount, 'Year': start_year})

print("__RESULT__:")
print(json.dumps({'total_funding': total_funding, 'debug': debug_list}))"""

env_args = {'var_function-call-836211722748550531': ['civic_docs'], 'var_function-call-836211722748548546': ['Funding'], 'var_function-call-9061716743711809176': 'file_storage/function-call-9061716743711809176.json', 'var_function-call-9061716743711808369': 'file_storage/function-call-9061716743711808369.json', 'var_function-call-12561724733303725061': 'file_storage/function-call-12561724733303725061.json'}

exec(code, env_args)
