code = """import json, re

# Load funding data (> $50,000) from stored file path
funding_path = var_call_qavtXlmiGoW9QnOA78pUlytE
with open(funding_path, "r") as f:
    funding_records = json.load(f)

funded_over_50k = { (rec.get("Project_Name") or "").strip() for rec in funding_records if isinstance(rec.get("Project_Name"), str) }

# Load civic documents
civic_path = var_call_RZF88M1S8GL1Z6q8kFep6vBb
with open(civic_path, "r") as f:
    civic_docs = json.load(f)

header_marker = "capital improvement projects (design)"
stop_markers = [
    "capital improvement projects (construction)",
    "capital improvement projects (not started)",
    "disaster recovery projects"
]

bullet_pattern = re.compile("\(cid:[^)]*\)")

capital_design_projects = set()

for doc in civic_docs:
    text = doc.get("text") or ""
    if not text:
        continue
    lines = text.split("\n")
    lowers = [ln.lower() for ln in lines]

    # Find all design header positions
    starts = [i for i, ln in enumerate(lowers) if header_marker in ln]
    for si in starts:
        # Determine section end
        end_idx = len(lines)
        for j in range(si + 1, len(lines)):
            lnj = lowers[j]
            if header_marker in lnj:
                end_idx = j
                break
            if any(sm in lnj for sm in stop_markers):
                end_idx = j
                break
        section = lines[si + 1:end_idx]
        section_low = [ln.lower() for ln in section]
        n = len(section)

        # Strategy A: Use lines with updates/schedule/description as anchors; take previous line as project name
        def is_anchor(l):
            l = l.strip()
            return (
                l.endswith("updates:") or l == "updates:" or l == "project updates:" or
                ("project schedule" in l) or ("estimated schedule" in l) or l.endswith("description:") or l == "project description:"
            )

        for idx in range(n):
            if is_anchor(section_low[idx]):
                k = idx - 1
                # move back to find candidate title
                while k >= 0 and (section[k].strip() == "" or section_low[k].startswith("agenda item") or section_low[k].startswith("page ")):
                    k -= 1
                # If we landed on a description line, step further back
                if k >= 0 and ("description:" in section_low[k]):
                    k -= 1
                    while k >= 0 and (section[k].strip() == "" or section_low[k].startswith("agenda item") or section_low[k].startswith("page ")):
                        k -= 1
                if k >= 0:
                    cand = section[k].strip()
                    # filter out non-name lines
                    if cand and not cand.endswith(":"):
                        cand = bullet_pattern.sub("", cand).strip()
                        cand = re.sub("\s+", " ", cand)
                        if len(cand) > 2:
                            capital_design_projects.add(cand)
        
        # Strategy B: Title-like lines followed within 5 lines by an anchor
        for idx in range(n):
            cand = section[idx].strip()
            low = section_low[idx]
            if not cand:
                continue
            if low.startswith("agenda item") or low.startswith("page "):
                continue
            if ":" in cand:
                continue
            found = False
            for kk in range(1, 6):
                if idx + kk >= n:
                    break
                if is_anchor(section_low[idx + kk]):
                    found = True
                    break
            if found:
                clean = bullet_pattern.sub("", cand).strip()
                clean = re.sub("\s+", " ", clean)
                if len(clean) > 2:
                    capital_design_projects.add(clean)

# Intersect with funded-over-50k project names
matched_projects = sorted([name for name in capital_design_projects if name in funded_over_50k])

result = {"count": len(matched_projects), "matched_projects": matched_projects}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_emkmzpvum2bkhY3KeP5UYxCb': ['civic_docs'], 'var_call_o7fqj1i1czAOdbOZBSxsmZnL': ['Funding'], 'var_call_qavtXlmiGoW9QnOA78pUlytE': 'file_storage/call_qavtXlmiGoW9QnOA78pUlytE.json', 'var_call_RZF88M1S8GL1Z6q8kFep6vBb': 'file_storage/call_RZF88M1S8GL1Z6q8kFep6vBb.json', 'var_call_AbZ8lqeSkNP5EWX7XQhMRPdW': {'funding_count': 276, 'docs_count': 19}}

exec(code, env_args)
