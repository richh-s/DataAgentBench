code = """import json
import re

# Load data
with open(locals()['var_function-call-6964896026869671245'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-867828661549977430'], 'r') as f:
    funding_data = json.load(f)

# Combine all text from documents
full_text = "\n".join([doc['text'] for doc in civic_docs])

# Pre-processing text to identifying project blocks
# Based on preview, projects headers are lines that don't start with special chars and are followed by "(cid:190) Updates" or similar.
# Actually, looking at the text:
# "Bluffs Park Shade Structure\n\n(cid:190) Updates:"
# So I can split by `(cid:190) Updates`. The text immediately preceding it (ignoring whitespace) is likely the project name.

# Let's try to extract project blocks.
# We will create a map of Project Name -> Text Block
project_map = {}

# Split by the specific bullet point character used in the text for Updates
# The character in the preview is `(cid:190)`. Unicode \u00be (¾).
# It seems the text representation has `(cid:190)`.
# Let's search for `(cid:190) Updates`.
segments = full_text.split('(cid:190) Updates')

# The first segment is intro.
# The subsequent segments start with ": " or similar, then the updates, then eventually the next project title at the end.
# Wait, `split` consumes the separator.
# segment[i] ends with the title of project[i]. segment[i+1] is the body of project[i].
# This is tricky because the title is at the end of the previous segment.

# Let's try regex.
# Pattern: looks for a line that is likely a title, then `(cid:190) Updates`.
# But title matching is hard.

# Alternative:
# Iterate through Funding Projects.
# For each project, check if it's in the text.
# If it is, locate it and grab the text until the next project or reasonable delimiter.
# This avoids guessing titles.

# Cleaning function for Funding Names
def clean_name(name):
    # Remove (...) suffixes
    name = re.sub(r'\s*\(.*?\)$', '', name)
    return name.strip()

total_funding = 0
matched_projects = []

# cache text lower for searching
full_text_lower = full_text.lower()

# Group funding by cleaned name to avoid processing same text multiple times
funding_by_clean_name = {}
for entry in funding_data:
    raw_name = entry['Project_Name']
    amt = int(entry['Amount'])
    c_name = clean_name(raw_name)
    if c_name not in funding_by_clean_name:
        funding_by_clean_name[c_name] = {'amounts': [], 'raw_names': []}
    funding_by_clean_name[c_name]['amounts'].append(amt)
    funding_by_clean_name[c_name]['raw_names'].append(raw_name)

# Process each unique project name
for c_name, data in funding_by_clean_name.items():
    if len(c_name) < 5: continue # Skip short/empty names
    if "project_" in c_name.lower(): continue # Skip placeholder names
    
    # Find in text
    # We look for the name in the text.
    # To ensure it's a header, maybe check if it's followed by "Update" or newlines.
    # But even simple substring search is a good start.
    
    # Use re.escape to handle special chars in name
    # We look for the name, followed by some optional whitespace/newlines, then "(cid:190)" or "Updates"
    pattern = re.escape(c_name) + r'\s*(?:\n\s*)*' + r'(?:\(cid:190\)|Updates|Project Description|Project Schedule)'
    
    match = re.search(pattern, full_text, re.IGNORECASE)
    
    if match:
        # Found the project header.
        # Now extract the content.
        # Start from the end of the match.
        start_idx = match.end()
        # End at the next occurrence of a known project header or some delimiter.
        # Hard to predict next header.
        # Let's take a chunk, say 2000 chars, or until next "(cid:190) Updates" if we can find the project name before it.
        # A simple heuristic: take next 1000 characters.
        context = full_text[start_idx:start_idx+1000]
        
        # Check topic "park"
        # Topic can be in the name or the context.
        is_park = False
        if 'park' in c_name.lower():
            is_park = True
        else:
            # Check context for keywords
            # "topic: ... park" isn't explicit. Just look for "park".
            # Hints say "The topic field contains comma-separated keywords... Common topics include: 'park'..."
            # Maybe I should look for "Topic:" in the text?
            # The preview didn't show "Topic:". It showed "Subject: ...".
            # But the DB description says "topic: Keywords describing...". This might be an extracted field I should derive.
            # I'll search for "park" in the context.
            if 'park' in context.lower():
                is_park = True
        
        if is_park:
            # Check status completed in 2022
            # Look for "completed" and "2022" in context
            context_lower = context.lower()
            if 'completed' in context_lower and '2022' in context_lower:
                # verify they are related
                # e.g. "completed november 2022" or "completed: ... 2022"
                # Let's be slightly strict: "completed" within 50 chars of "2022"
                # find all indices of completed
                comp_indices = [m.start() for m in re.finditer('completed', context_lower)]
                found_date = False
                for idx in comp_indices:
                    sub = context_lower[idx:idx+100] # look ahead
                    sub_prev = context_lower[max(0, idx-50):idx] # look behind
                    if '2022' in sub or '2022' in sub_prev:
                        found_date = True
                        break
                
                if found_date:
                    # It's a match!
                    # Sum all amounts for this project name
                    total = sum(data['amounts'])
                    total_funding += total
                    matched_projects.append({
                        "name": c_name,
                        "amount": total,
                        "match_reason": "Found park and completed 2022"
                    })

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": matched_projects}))"""

env_args = {'var_function-call-6964896026869671245': 'file_storage/function-call-6964896026869671245.json', 'var_function-call-16721484954554461294': ['Funding'], 'var_function-call-867828661549977430': 'file_storage/function-call-867828661549977430.json'}

exec(code, env_args)
