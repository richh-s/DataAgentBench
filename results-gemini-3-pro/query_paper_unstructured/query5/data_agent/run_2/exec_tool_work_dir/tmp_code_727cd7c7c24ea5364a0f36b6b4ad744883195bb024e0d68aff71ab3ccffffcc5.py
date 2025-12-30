code = """import json
import re

# Load SQLite results
with open(locals()['var_function-call-5224720057325487850'], 'r') as f:
    citations_data = json.load(f)

# Create a lookup for citation counts: title -> count
citation_map = {item['title']: item['citation_count'] for item in citations_data}

# Load Mongo results
docs = []
# Batch 1
with open(locals()['var_function-call-2124735565841036001'], 'r') as f:
    docs.extend(json.load(f))
# Batch 2
with open(locals()['var_function-call-17006364439128705888'], 'r') as f:
    docs.extend(json.load(f))

total_citations = 0
chi_papers = []

print(f"Total docs found: {len(docs)}")

for doc in docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check first 1000 chars for venue
    header = text[:1000]
    
    # Logic to detect CHI
    # Patterns: "CHI 'YY", "CHI 20YY", "Conference on Human Factors in Computing Systems"
    is_chi = False
    if re.search(r"CHI\s*'?\d{2,4}", header, re.IGNORECASE):
        is_chi = True
    elif "Conference on Human Factors in Computing Systems" in header:
        is_chi = True
        
    # Additional check: exclude "OzCHI", "CHI Play", etc if strict "CHI" is required.
    # The query says "presented at CHI". Usually means the main conference.
    # OzCHI is distinct. CHI Play is distinct.
    # If regex matches "OzCHI", it might also match "CHI".
    # We should ensure it's "CHI" word boundary?
    # "CHI '15"
    
    if is_chi:
        # Check for false positives like "OzCHI"
        if "OzCHI" in header and "CHI '" not in header and "CHI 20" not in header:
             # This is a heuristic. 
             pass
        
    if is_chi:
        count = citation_map.get(title, 0)
        # count is int or str? in preview it was "65" (str).
        try:
            count = int(count)
        except:
            count = 0
        total_citations += count
        chi_papers.append(title)

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "chi_paper_count": len(chi_papers), "chi_papers": chi_papers}))"""

env_args = {'var_function-call-7135423062903298994': ['Citations', 'sqlite_sequence'], 'var_function-call-7135423062903296087': ['paper_docs'], 'var_function-call-5224720057325487850': 'file_storage/function-call-5224720057325487850.json', 'var_function-call-5224720057325488687': 'file_storage/function-call-5224720057325488687.json', 'var_function-call-6314409966218616045': 188, 'var_function-call-18245712614584764199': 'file_storage/function-call-18245712614584764199.json', 'var_function-call-3601486565505648130': 'file_storage/function-call-3601486565505648130.json', 'var_function-call-9720797452999048839': ['Sundroid: Solar Radiation Awareness with Smartphones.txt', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application.txt", 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection.txt', 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt', 'Modeling Interdependent and Periodic Real-World Action Sequences.txt', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video.txt', 'How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace.txt', 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations.txt', 'A Lived Informatics Model of Personal Informatics.txt', 'Charting Design Preferences on Wellness Wearables.txt', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'Heed: Exploring the Design of Situated Self-Reporting Devices.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis.txt', 'Technologies for Everyday Life Reflection: Illustrating a Design Space.txt', 'Personal Tracking of Screen Time on Digital Devices.txt', 'Sensor Requirements for Activity Recognition on Smart Watches.txt', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture.txt', 'Defining Adherence: Making Sense of Physical Activity Tracker Data.txt', 'Live Interest Meter: Learning from Quantified Feedback in Mass Lectures.txt', 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game.txt', 'Communicating Uncertainty in Fertility Prognosis.txt', 'Understanding Personal Productivity: How Knowledge Workers Define, Evaluate, and Reflect on Their Productivity.txt', 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings.txt', 'Visual ODLs: Co-Designing Patient-Generated Observations of Daily Living to Support Data-Driven Conversations in Pediatric Care.txt', 'Pass the Ball: Enforced Turn-Taking in Activity Tracking.txt', 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data.txt', 'Scaffolding for an OLM for Long-Term Physical Activity Goals.txt', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace.txt', 'Turn to the Self in Human-Computer Interaction: Care of the Self in Negotiating the Human-Technology Relationship.txt', "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps.txt", 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics.txt', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance.txt', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt', 'Understanding Animals: A Critical Challenge in ACI.txt', 'Social (Media) Jet Lag: How Usage of Social Technology Can Modulate and Reflect Circadian Rhythms.txt', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats.txt', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness.txt', 'TastyBeats: Designing Palatable Representations of Physical Activity.txt', 'Toward Health Information Technology That Supports Overweight/Obese Women in Addressing Emotion- and Stress-Related Eating.txt', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices.txt', 'Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration.txt'], 'var_function-call-2124735565841036001': 'file_storage/function-call-2124735565841036001.json', 'var_function-call-15632493221343134602': 'file_storage/function-call-15632493221343134602.json', 'var_function-call-17006364439128705888': 'file_storage/function-call-17006364439128705888.json', 'var_function-call-10886053708587340973': [], 'var_function-call-5291751097886377606': [], 'var_function-call-4565888100411783468': [], 'var_function-call-3361289442905450367': [], 'var_function-call-17984830700348301280': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-18224936322923523571': []}

exec(code, env_args)
