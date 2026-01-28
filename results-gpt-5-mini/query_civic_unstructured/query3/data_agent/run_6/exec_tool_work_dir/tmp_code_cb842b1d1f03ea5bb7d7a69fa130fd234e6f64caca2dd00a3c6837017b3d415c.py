code = """import json, re

# Load funding records
funding_var = var_call_cQ1zQFelFE9RnIqGqbRuGGrR
if isinstance(funding_var, str):
    with open(funding_var, 'r') as f:
        funding = json.load(f)
else:
    funding = funding_var

# Load civic docs
civic_var = var_call_igZlSbiLWjIZqU8d0FYKe2z4
if isinstance(civic_var, str):
    with open(civic_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_var

# Helper to normalize project name by removing parenthetical suffixes
def base_name(name):
    # remove trailing parenthesis groups like ' (FEMA Project)'
    return re.sub(r"\s*\(.*?\)\s*$", "", name).strip()

# Helper to determine status from text snippet
def infer_status(snippet_lower):
    # design indicators
    design_terms = ['complete design', 'complete design:', 'design phase', 'preliminary design', 'final design', 'working with the consultant to finalize the design', 'project is in the preliminary design', 'project is in the design']
    completed_terms = ['construction was completed', 'complete construction', 'complete construction:', 'complete construction.', 'notice of completion', 'under construction', 'begin construction', 'begin construction:', 'began construction', 'project is currently under construction']
    not_started_terms = ['not started', 'not begun', 'identified in', 'identified and']

    for t in design_terms:
        if t in snippet_lower:
            return 'design'
    for t in completed_terms:
        if t in snippet_lower:
            return 'completed'
    for t in not_started_terms:
        if t in snippet_lower:
            return 'not started'
    return None

results = []

# Pre-lower civic docs texts for faster search
docs_texts = [doc.get('text','') for doc in civic_docs]
docs_texts_lower = [t.lower() for t in docs_texts]

for rec in funding:
    proj = rec.get('Project_Name','')
    proj_lower = proj.lower()
    bname = base_name(proj)
    bname_lower = bname.lower()

    related = False
    status = None

    # If funding project name explicitly mentions FEMA or emergency
    if 'fema' in proj_lower or 'emergency' in proj_lower:
        related = True

    # Otherwise, check if base name appears in any civic doc (these docs already contain emergency/FEMA)
    if not related:
        for doc_text_lower in docs_texts_lower:
            if bname_lower and bname_lower in doc_text_lower:
                related = True
                break

    # If related, attempt to infer status from civic docs where it appears
    if related:
        # search each document for the project name and extract nearby context
        for doc_text, doc_text_lower in zip(docs_texts, docs_texts_lower):
            # find occurrences of either full project name or base name
            idx = -1
            if proj_lower in doc_text_lower:
                idx = doc_text_lower.find(proj_lower)
            elif bname_lower in doc_text_lower:
                idx = doc_text_lower.find(bname_lower)
            if idx >= 0:
                start = max(0, idx-300)
                end = min(len(doc_text), idx+300)
                snippet = doc_text[start:end]
                snippet_lower = snippet.lower()
                inferred = infer_status(snippet_lower)
                if inferred:
                    status = inferred
                    break
                else:
                    # try broader search in full doc
                    inferred_full = infer_status(doc_text_lower)
                    if inferred_full:
                        status = inferred_full
                        break
        # If still not found, look for general indicators in all civic docs
        if status is None:
            for doc_text_lower in docs_texts_lower:
                inferred_full = infer_status(doc_text_lower)
                if inferred_full:
                    status = inferred_full
                    break
    
    if related:
        # normalize amount to int if possible
        amt = rec.get('Amount')
        try:
            amt_val = int(str(amt))
        except:
            try:
                amt_val = int(float(str(amt)))
            except:
                amt_val = None
        results.append({
            'Project_Name': proj,
            'Funding_Source': rec.get('Funding_Source'),
            'Amount': amt_val,
            'Status': status if status is not None else 'unknown'
        })

# Remove duplicates by Project_Name keeping first
seen = set()
unique_results = []
for r in results:
    if r['Project_Name'] not in seen:
        unique_results.append(r)
        seen.add(r['Project_Name'])

# Print results as JSON string
print("__RESULT__:")
print(json.dumps(unique_results))"""

env_args = {'var_call_igZlSbiLWjIZqU8d0FYKe2z4': 'file_storage/call_igZlSbiLWjIZqU8d0FYKe2z4.json', 'var_call_cQ1zQFelFE9RnIqGqbRuGGrR': 'file_storage/call_cQ1zQFelFE9RnIqGqbRuGGrR.json'}

exec(code, env_args)
