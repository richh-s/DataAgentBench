code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-9278851709122145007'], 'r') as f:
    papers_data = json.load(f)

df_papers = pd.DataFrame(papers_data)

print("Checking first 5 papers for keywords extraction:")
for i, row in df_papers.head(5).iterrows():
    text = row['text']
    # Debug extraction
    patterns = [r"Author Keywords", r"Keywords"]
    start_idx = -1
    for p in patterns:
        match = re.search(p, text, re.IGNORECASE)
        if match:
            start_idx = match.end()
            break
    
    extracted = "NOT FOUND"
    if start_idx != -1:
        sub_text = text[start_idx:]
        end_markers = ["ACM Classification Keywords", "INTRODUCTION", "ABSTRACT"]
        end_idx = len(sub_text)
        for marker in end_markers:
            marker_match = re.search(marker, sub_text, re.IGNORECASE)
            if marker_match:
                end_idx = min(end_idx, marker_match.start())
        extracted = sub_text[:end_idx].strip()
        
    print(f"File: {row['filename']}")
    print(f"Extracted Keywords: {extracted[:200]}...") # Print first 200 chars
    print("-" * 20)

# Check if 'food' appears in any extracted keywords
print("Checking for 'food' in extracted keywords...")
found_count = 0
for i, row in df_papers.iterrows():
    text = row['text']
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
            found_count += 1
            print(f"Found 'food' in: {row['filename']}")

print(f"Total papers with 'food' in keywords: {found_count}")

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-10309278563115687463': ['paper_docs'], 'var_function-call-17310270331774513134': 'file_storage/function-call-17310270331774513134.json', 'var_function-call-14859437005275468977': 'file_storage/function-call-14859437005275468977.json', 'var_function-call-9278851709122145007': 'file_storage/function-call-9278851709122145007.json', 'var_function-call-2702061835981032480': 0}

exec(code, env_args)
