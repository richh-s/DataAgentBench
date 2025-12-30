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

# Normalize project names to find base names
def get_base_name(name):
    # Remove common suffixes
    name = re.sub(r'\s*\(FEMA.*?\)', '', name)
    name = re.sub(r'\s*\(CalOES.*?\)', '', name)
    name = re.sub(r'\s*\(CalJPIA.*?\)', '', name)
    name = re.sub(r'\s*\(FEMA\)', '', name)
    return name.strip()

funding_df['base_name'] = funding_df['Project_Name'].apply(get_base_name)
unique_base_names = funding_df['base_name'].unique()

# Process Text to find project details
project_details = {} # base_name -> {'start_date': str, 'text_snippet': str}

# Concatenate all text for searching (or search doc by doc)
# Doc by doc is better to keep context, but project names are unique enough.
# Let's search each doc.

for doc in civic_docs:
    text = doc.get('text', '')
    # Clean text slightly?
    text = text.replace('\n', ' ')
    
    for base_name in unique_base_names:
        if base_name in project_details and project_details[base_name].get('start_year'):
            continue # Already found info
        
        if base_name in text:
            # Find all occurrences? Usually the header is the one we want.
            # Let's assume the header is where the name appears.
            # We take a window of text after the name.
            # Regex escape base_name
            pattern = re.escape(base_name)
            matches = list(re.finditer(pattern, text))
            
            for match in matches:
                start_idx = match.end()
                # snippet window: 2000 chars should cover schedule
                snippet = text[start_idx : start_idx + 2000]
                
                # Extract Start Date
                # Look for "Begin Construction: <Date>"
                # Or "Start Date: <Date>"
                # Or "Project Schedule: ... Begin Construction: <Date>"
                
                start_date = None
                date_match = re.search(r'Begin [Cc]onstruction:?\s*([A-Za-z0-9, ]+)', snippet)
                if date_match:
                    start_date = date_match.group(1).strip()
                
                # If not found, try "Construction start"
                if not start_date:
                     date_match = re.search(r'Construction start:?\s*([A-Za-z0-9, ]+)', snippet, re.IGNORECASE)
                     if date_match:
                         start_date = date_match.group(1).strip()

                # If found, check year
                start_year = None
                if start_date:
                    # Look for 4 digits
                    y_match = re.search(r'20\d{2}', start_date)
                    if y_match:
                        start_year = int(y_match.group(0))
                
                # Check for Disaster keywords in snippet
                is_disaster_text = False
                keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Woolsey Fire', 'Disaster', 'Emergency']
                for kw in keywords:
                    if kw.lower() in snippet.lower():
                        is_disaster_text = True
                        break
                
                if start_year:
                    # Store found info
                    project_details[base_name] = {
                        'start_year': start_year,
                        'is_disaster_text': is_disaster_text,
                        'raw_start_date': start_date
                    }
                    break # Found for this project in this doc

# Calculate Total Funding
total_funding = 0
debug_list = []

for _, row in funding_df.iterrows():
    base_name = row['base_name']
    amount = row['Amount']
    orig_name = row['Project_Name']
    
    # Determine if Disaster
    is_disaster_name = any(x in orig_name for x in ['FEMA', 'CalOES', 'CalJPIA'])
    
    # Check text details
    details = project_details.get(base_name, {})
    is_disaster_text = details.get('is_disaster_text', False)
    start_year = details.get('start_year')
    
    is_disaster = is_disaster_name or is_disaster_text
    
    if is_disaster and start_year == 2022:
        total_funding += amount
        debug_list.append({
            'Project': orig_name,
            'Amount': amount,
            'Year': start_year,
            'Disaster_Name': is_disaster_name,
            'Disaster_Text': is_disaster_text
        })

print("__RESULT__:")
print(json.dumps({'total_funding': total_funding, 'debug': debug_list}))"""

env_args = {'var_function-call-836211722748550531': ['civic_docs'], 'var_function-call-836211722748548546': ['Funding'], 'var_function-call-9061716743711809176': 'file_storage/function-call-9061716743711809176.json', 'var_function-call-9061716743711808369': 'file_storage/function-call-9061716743711808369.json', 'var_function-call-12561724733303725061': 'file_storage/function-call-12561724733303725061.json'}

exec(code, env_args)
