code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-9278851709122145007'], 'r') as f:
    papers_data = json.load(f)

debug_info = []

# Check for 'food' in Keywords
food_papers = []
for paper in papers_data:
    text = paper['text']
    # Extract keywords
    patterns = [r"Author Keywords", r"Keywords"]
    start_idx = -1
    for p in patterns:
        match = re.search(p, text, re.IGNORECASE)
        if match:
            start_idx = match.end()
            break
    
    if start_idx != -1:
        sub_text = text[start_idx:]
        end_markers = ["ACM Classification Keywords", "INTRODUCTION", "ABSTRACT"]
        end_idx = len(sub_text)
        for marker in end_markers:
            marker_match = re.search(marker, sub_text, re.IGNORECASE)
            if marker_match:
                end_idx = min(end_idx, marker_match.start())
        keywords = sub_text[:end_idx].lower()
        
        if 'food' in keywords:
            food_papers.append(paper['filename'])
        
        # Add to debug info for first few papers
        if len(debug_info) < 5:
            debug_info.append({
                "filename": paper['filename'],
                "extracted_keywords": keywords[:100]
            })

print("__RESULT__:")
print(json.dumps({"food_papers_count": len(food_papers), "food_papers": food_papers, "debug": debug_info}))"""

env_args = {'var_function-call-10309278563115687463': ['paper_docs'], 'var_function-call-17310270331774513134': 'file_storage/function-call-17310270331774513134.json', 'var_function-call-14859437005275468977': 'file_storage/function-call-14859437005275468977.json', 'var_function-call-9278851709122145007': 'file_storage/function-call-9278851709122145007.json', 'var_function-call-2702061835981032480': 0, 'var_function-call-14459346751113599875': 'Done'}

exec(code, env_args)
