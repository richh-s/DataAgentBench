import re
import json

RESULT_MARKER = "__RESULT__:"

def parse_result_python(text):
    pattern = re.escape(RESULT_MARKER) + r"(.*)$"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        parsed_result_str = match.group(1).strip()
        try:
            parsed_result = json.loads(parsed_result_str)
            return parsed_result
        except json.JSONDecodeError as e: # fallback
            raise ValueError(f"Failed to parse the printed result ({type(e).__name__}):\nPrinted result:\n{parsed_result_str}\nError:\n{str(e)}")
    raise ValueError(f"{RESULT_MARKER} not found in the printed output.")