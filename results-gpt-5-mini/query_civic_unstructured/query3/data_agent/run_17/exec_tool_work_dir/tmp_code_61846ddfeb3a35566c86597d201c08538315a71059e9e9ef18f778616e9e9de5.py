code = """import json
path = var_call_kESzRD6axEvtHVPDcXvLTW1P
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

candidates = {}
keywords = ["project", "repairs", "improvements", "facility", "park", "road", "drainage", "warning", "signal", "playground", "water"]

for doc in docs:
    text = doc.get("text", "")
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        low_ln = ln.lower()
        if "fema" in low_ln or "emergency" in low_ln:
            title_found = False
            for j in range(1, 9):
                idx = i - j
                if idx < 0:
                    break
                cand = lines[idx]
                if not cand:
                    continue
                low = cand.lower()
                if any(skip in low for skip in ["agenda", "page", "meeting", "item", "report", "updates", "discussion", "prepared", "approved", "subject"]):
                    continue
                if any(k in low for k in keywords) or "project" in low:
                    title = " ".join(cand.split())
                    # build context
                    start = max(0, idx-2)
                    end = min(len(lines), i+4)
                    context = " ".join(lines[start:end]).lower()
                    status = "design"
                    if "construction was completed" in context or "complete construction" in context or "notice of completion" in context or "completed" in context:
                        status = "completed"
                    elif "not started" in context or "not begun" in context or "identified" in context:
                        status = "not started"
                    elif "design" in context or "preliminary design" in context or "complete design" in context or "working with the consultant" in context or "finalize the design" in context:
                        status = "design"
                    candidates[title] = status
                    title_found = True
                    break
            if not title_found:
                # fallback: use the line itself or nearby line
                title = " ".join(ln.split())
                context = " ".join(lines[max(0, i-2):min(len(lines), i+3)]).lower()
                status = "design"
                if "completed" in context:
                    status = "completed"
                candidates[title] = status

out = []
for name in sorted(candidates.keys()):
    out.append({"Project_Name": name, "Status": candidates[name]})

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WKtxU0jxPJ15joDyaPmwBSnF': ['civic_docs'], 'var_call_jGUa9xleKbwSjDyorm3VrObQ': ['Funding'], 'var_call_kESzRD6axEvtHVPDcXvLTW1P': 'file_storage/call_kESzRD6axEvtHVPDcXvLTW1P.json'}

exec(code, env_args)
