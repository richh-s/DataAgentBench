code = """import json
import re

# Load data
with open(locals()['var_function-call-11529138748773800259'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-6363168235283738913'], 'r') as f:
    funding_data = json.load(f)

# Normalize funding data for easier lookup
funding_map = {}
for entry in funding_data:
    funding_map[entry['Project_Name']] = float(entry['Amount'])

completed_park_projects = []
matched_project_names = set()

# Regex to find project blocks
# Looking for lines that look like a project name followed by "(cid:190) Updates:" or "(cid:190) Project Description:"
# The special characters (cid:190) might be represented differently or standard text. 
# In the preview: "(cid:190)" is visible.
# It seems to be a bullet point.

# Let's iterate through lines to identify project starts
def extract_projects(text):
    projects = []
    lines = text.split('\n')
    current_project_name = None
    current_project_text = []
    
    # Heuristic: Project name is a line followed by a line starting with (cid:190)
    # or containing "Updates:" or "Project Description:"
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
            
        # Check if this line marks the start of a project description block
        # The marker seems to be "(cid:190)" which might be encoded or just text
        if "(cid:190)" in stripped:
            # The previous non-empty line was likely the project name
            # We need to backtrack to find it.
            # But wait, we are iterating.
            pass

    # Better approach with regex on full text
    # Split by double newlines to get paragraphs
    # If a paragraph starts with a name and the next starts with (cid:190), it's a project.
    
    return projects

# Let's try a regex approach on the whole text
# We assume the structure: <ProjectName>\n\n(cid:190) (Updates|Project Description)
# We capture the ProjectName and the following text until the next ProjectName or end of section.

project_pattern = re.compile(r'(?P<name>^[A-Za-z0-9 \-&]+)\n+(?=\(cid:190\))', re.MULTILINE)

# This regex finds the name. But we need the text *after* it.
# Let's split the text by the project name pattern? No, names are variable.

# Alternative: Split by the bullet point "(cid:190)"
# The text before it (up to previous newline) is the header/project name.
# The text after it is the content.

matched_projects = []

for doc in civic_docs:
    text = doc['text']
    # Split by the specific bullet char pattern
    parts = text.split('(cid:190)')
    
    # parts[0] is preamble.
    # parts[1] starts with "Updates:" or "Project Description:" and belongs to Project 1.
    # But wait, Project 1's name is at the end of parts[0].
    
    for i in range(1, len(parts)):
        content = parts[i]
        # The project name is at the end of parts[i-1]
        prev_chunk = parts[i-1].strip()
        lines = prev_chunk.split('\n')
        
        # Filter out empty lines
        lines = [l.strip() for l in lines if l.strip()]
        
        if not lines:
            continue
            
        project_name = lines[-1] # The last line before the bullet is the name
        
        # Clean up project name (sometimes it might have extra stuff)
        # Check if it's a known header like "Capital Improvement Projects (Design)"
        if "Capital Improvement Projects" in project_name:
            # Then the project name is actually not this line.
            # But looking at the text:
            # "Capital Improvement Projects (Design)\n\n2022 Morning View..."
            # So "2022 Morning View..." is the name.
            # If the header was just above, the split logic takes the last line.
            # So if lines[-1] is "Capital Improvement Projects...", then there is no project name?
            # Or maybe the bullet is attached to the project name?
            # Text: "2022 Morning View ...\n\n(cid:190) Updates:"
            # So lines[-1] should be "2022 Morning View ..."
            pass
            
        # Check keywords in project_name or content
        is_park = 'park' in project_name.lower() # Strict requirement: park-related.
        # Maybe check content too? "topic: Keywords ... Common topics include: 'park'"
        # I'll check if 'park' is in project_name. If not, check content?
        # The prompt says "Project_Name: The name... topic: Keywords...".
        # It's safer to check both name and content for "park".
        # But commonly, park projects have "Park" in the name.
        if 'park' not in project_name.lower():
             # Check if keywords appear in content?
             # But "Malibu Park" is a location, so "Malibu Park Drainage" might be road related.
             # "Bluffs Park Shade Structure" is definitely park related.
             # "Trancas Canyon Park" is park related.
             # Let's stick to "park" in the name for high precision, or specific keywords in text like "playground".
             if 'park' in content.lower():
                 # "Park" in content might be "parking". Be careful.
                 # "Skate Park" -> yes.
                 pass
        
        # Let's assume if "park" is in the name, it's a park project. 
        # Also need to handle "Malibu Park" which is a neighborhood, but projects like "Malibu Park Resurfacing" might be road.
        # But "Bluffs Park" is a park.
        # Let's look at the specific park names in the DB or infer.
        # "Legacy Park", "Bluffs Park", "Trancas Canyon Park", "Las Flores Creek Park".
        # If the project is "Malibu Park Resurfacing Project", is it a park project or a road project in the Malibu Park neighborhood? 
        # Usually "Resurfacing" implies roads.
        # "Malibu Bluffs Park" is a park.
        # "Legacy Park" is a park.
        # "Trancas Canyon Park" is a park.
        # "Permanent Skate Park" is a park/rec project.
        
        # Let's refine "park-related".
        # Hints say: "Common topics include: 'park'...".
        # I will look for the word "park" as a whole word (regex `\bpark\b`) in the text associated with the project, OR in the name.
        # But "Malibu Park" matches.
        # Let's look at the funding table project names to see what we have.
        # "Bluffs Park Shade Structure"
        # "Bluffs Park Workout Station"
        # "Legacy Park Benches..."
        # "Legacy Park Paver..."
        # "Malibu Bluffs Park Roof..."
        # "Malibu Bluffs Park South Walkway"
        # "Trancas Canyon Park..."
        # "Permanent Skate Park"
        # "Malibu Park Drainage Improvements" -> This is ambiguous. "Malibu Park" is a neighborhood. But "Drainage" is usually infrastructure.
        # However, if the topic extraction says "park", I should count it.
        # Given I cannot run the sophisticated topic extractor, I will count it if "Park" is in the name AND it's not clearly just a road name like "Malibu Park Road" (but "Malibu Park" is a neighborhood).
        # Actually, "Malibu Park" is often used to refer to the neighborhood. 
        # But let's check the status/date first. That will filter down the candidates.
        
        # Check completion in 2022
        # Patterns: "Construction was completed November 2022", "Construction was completed, November 2022"
        # "Construction was completed <Month> 2022"
        # "Complete Construction: <Month> 2022"
        
        completed_2022 = False
        
        # Normalize content to single line for easier regex
        content_linear = content.replace('\n', ' ')
        
        # Regex for completion
        # matches: "completed November 2022", "completed, November 2022", "Complete Construction: November 2022"
        # We need "2022" specifically.
        
        completion_match = re.search(r'(?:completed|Construction:)[\w\s,]+2022', content_linear, re.IGNORECASE)
        if completion_match:
            # Check if it says "November 2022" or similar.
            # Make sure it's 2022.
            if "2022" in completion_match.group(0):
                completed_2022 = True
                
        if completed_2022:
            matched_projects.append({'name': project_name, 'text': content})

print('__RESULT__:')
print(json.dumps(matched_projects))"""

env_args = {'var_function-call-9104980258508522346': ['Funding'], 'var_function-call-9104980258508522899': ['civic_docs'], 'var_function-call-6363168235283738913': 'file_storage/function-call-6363168235283738913.json', 'var_function-call-6363168235283742026': 'file_storage/function-call-6363168235283742026.json', 'var_function-call-11529138748773800259': 'file_storage/function-call-11529138748773800259.json'}

exec(code, env_args)
