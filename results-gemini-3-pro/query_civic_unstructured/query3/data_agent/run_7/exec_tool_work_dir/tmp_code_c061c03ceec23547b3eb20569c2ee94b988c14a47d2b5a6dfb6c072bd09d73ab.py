code = """import json
import pandas as pd

# Load Funding Data
with open(locals()['var_function-call-16505334197824858844'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load Civic Docs
with open(locals()['var_function-call-5478402608851220705'], 'r') as f:
    civic_docs = json.load(f)

# Combine text
text_list = [doc.get('text', '') for doc in civic_docs]
full_text = chr(10).join(text_list)

# Prepare Project Names for searching (Sort by length desc to match longest first)
project_names = funding_df['Project_Name'].unique().tolist()
project_names.sort(key=len, reverse=True)

# Parsing Text
lines = full_text.split(chr(10))
current_status = 'unknown'
project_map = {} # Name -> {status, context}

# Keywords for Status Headers
status_headers = {
    'Capital Improvement Projects (Design)': 'design',
    'Capital Improvement Projects (Construction)': 'construction_section',
    'Capital Improvement Projects (Not Started)': 'not started'
}

current_project = None
current_project_context = []

def save_current_project():
    if current_project:
        # Determine status
        final_status = current_status
        context_str = ' '.join(current_project_context).lower()
        
        if current_status == 'construction_section':
            if 'completed' in context_str or 'notice of completion' in context_str:
                final_status = 'completed'
            else:
                final_status = 'under construction'
        
        # Check topic relevance in context
        is_relevant_topic = False
        keywords = ['fema', 'emergency', 'fire', 'disaster']
        if any(k in context_str for k in keywords):
            is_relevant_topic = True
            
        project_map[current_project] = {
            'status': final_status,
            'relevant_topic': is_relevant_topic
        }

for line in lines:
    clean_line = line.strip()
    if not clean_line:
        continue
        
    # Check for Headers
    is_header = False
    for header, status in status_headers.items():
        if header in clean_line:
            save_current_project()
            current_project = None
            current_project_context = []
            current_status = status
            is_header = True
            break
    if is_header:
        continue

    # Check for Project Name match
    found_project = None
    if current_status != 'unknown':
        for name in project_names:
            if clean_line == name:
                found_project = name
                break
            if name in clean_line and len(clean_line) < len(name) + 10:
                 found_project = name
                 break
    
    if found_project:
        save_current_project()
        current_project = found_project
        current_project_context = []
    else:
        if current_project:
            current_project_context.append(clean_line)

save_current_project() # Save last one

# Merge and Filter
results = []
for index, row in funding_df.iterrows():
    p_name = row['Project_Name']
    
    # Relevance Check
    name_relevant = 'fema' in p_name.lower() or 'emergency' in p_name.lower()
    
    # Status/Topic from Text
    p_data = project_map.get(p_name)
    
    if p_data:
        status = p_data['status']
        topic_relevant = p_data['relevant_topic']
    else:
        status = 'unknown' # Not found in text
        topic_relevant = False
        
    if (name_relevant or topic_relevant) and status != 'unknown':
        results.append({
            'Project_Name': p_name,
            'Funding_Source': row['Funding_Source'],
            'Amount': row['Amount'],
            'Status': status
        })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_function-call-16505334197824856773': 'file_storage/function-call-16505334197824856773.json', 'var_function-call-16505334197824858844': 'file_storage/function-call-16505334197824858844.json', 'var_function-call-5478402608851220705': 'file_storage/function-call-5478402608851220705.json'}

exec(code, env_args)
