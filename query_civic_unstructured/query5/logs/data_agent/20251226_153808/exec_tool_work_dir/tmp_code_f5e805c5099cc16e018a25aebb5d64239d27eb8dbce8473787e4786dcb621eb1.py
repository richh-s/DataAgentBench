code = """import json, re

# Load civic docs
civic_path = var_call_IK3fn2ugEoLmAv5K3pegEKfT
with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Load funding table
funding_path = var_call_t4pMP4lJNGkh6vsjm9xCDWEx
with open(funding_path, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Pattern to strip disaster suffixes
suffix_pattern = re.compile(r"\s*\((?:FEMA(?:/[A-Za-z]+)?|CalOES|CalJPIA)(?:[^)]*)\)\s*$", re.IGNORECASE)

def base_name(name):
    n = suffix_pattern.sub("", name or "").strip()
    n = re.sub(r"\s+", " ", n)
    return n

def is_disaster_name(name):
    return bool(re.search(r"FEMA|CalOES|CalJPIA", name or "", re.IGNORECASE))

eligible_base_names = set()

for doc in civic_docs:
    text = (doc.get("text") or "").replace("\r\n", "\n")
    lines = [ln.strip() for ln in text.split("\n")]
    n = len(lines)
    # Build section map
    section_by_idx = {}
    current = None
    for i, ln in enumerate(lines):
        low = ln.lower()
        if "disaster recovery projects" in low:
            current = "disaster"
        elif "capital improvement projects" in low:
            current = "capital"
        section_by_idx[i] = current
    # Scan for Begin Construction lines with 2022
    for i, ln in enumerate(lines):
        if ("begin construction" in ln.lower()) and ("2022" in ln):
            # Only consider if in disaster section or nearby lines mention FEMA/CalOES/CalJPIA
            sec = section_by_idx.get(i)
            is_disaster = (sec == "disaster")
            if not is_disaster:
                # check nearby context for FEMA mentions
                ctx = "\n".join(lines[max(0, i-10):min(n, i+10)])
                if re.search(r"FEMA|CalOES|CalJPIA|Woolsey|fire", ctx, re.IGNORECASE):
                    is_disaster = True
            if not is_disaster:
                continue
            # find title above within 12 lines
            title = None
            for j in range(i-1, max(-1, i-15), -1):
                if j < 0:
                    break
                t = lines[j].strip()
                if not t:
                    continue
                if ":" in t:
                    continue
                tl = t.lower()
                if tl in {"updates", "project updates", "project schedule", "estimated schedule", "agenda", "subject", "discussion"}:
                    continue
                if 3 <= len(t) <= 140:
                    title = t
                    break
            if title:
                eligible_base_names.add(base_name(title))

# Sum funding amounts for matching disaster projects
total = 0
included = []
for row in funding_rows:
    pname = row.get("Project_Name", "")
    if not is_disaster_name(pname):
        continue
    if base_name(pname) in eligible_base_names:
        amt_str = row.get("Amount")
        try:
            amt = int(amt_str)
        except Exception:
            try:
                amt = int(re.sub(r"[^0-9]", "", str(amt_str)))
            except Exception:
                continue
        total += amt
        included.append({"Project_Name": pname, "Amount": amt})

result = {
    "eligible_project_basenames": sorted(list(eligible_base_names)),
    "funding_records_included": included,
    "total_funding": total
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2KKXqa5RVrT2vjHf1gQGBy65': ['civic_docs'], 'var_call_IK3fn2ugEoLmAv5K3pegEKfT': 'file_storage/call_IK3fn2ugEoLmAv5K3pegEKfT.json', 'var_call_4bAYPsTZoMODzL7tQBATHndp': ['Funding'], 'var_call_t4pMP4lJNGkh6vsjm9xCDWEx': 'file_storage/call_t4pMP4lJNGkh6vsjm9xCDWEx.json'}

exec(code, env_args)
