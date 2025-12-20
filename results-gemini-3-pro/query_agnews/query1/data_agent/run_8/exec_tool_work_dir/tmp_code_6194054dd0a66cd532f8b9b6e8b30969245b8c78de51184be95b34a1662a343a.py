code = """import json

# Load the file
with open(locals()['var_function-call-8284316981365420739'], 'r') as f:
    articles = json.load(f)

print(f"Total loaded: {len(articles)}")

# Define keywords
sports_keywords = {
    "sport", "sports", "football", "basketball", "baseball", "soccer", "tennis", "golf", "hockey", 
    "olympic", "olympics", "f1", "nascar", "cricket", "rugby", "boxing", "wrestling", "medal", 
    "tournament", "championship", "league", "cup", "athlete", "player", "coach", "team", "match", 
    "score", "game", "playoff", "finals", "super bowl", "world cup", "wimbledon", "nfl", "nba", 
    "mlb", "nhl", "fifa", "uefa", "quarterback", "touchdown", "homerun", "goal", "striker", 
    "midfielder", "defender", "goalkeeper", "pitcher", "batter", "inning", "puck", "red sox", 
    "yankees", "lakers", "bulls", "knicks", "celtics", "real madrid", "barcelona", "manchester united", 
    "arsenal", "chelsea", "liverpool", "ac milan", "inter milan", "juventus", "bayern munich"
}

business_keywords = {
    "stock", "market", "price", "company", "corp", "inc", "ltd", "profit", "revenue", "sale", 
    "investment", "share", "business", "economy", "trade", "dollar", "euro", "bank", "fed", 
    "inflation", "job", "manager", "executive", "ceo", "cfo", "wall st", "nasdaq", "dow jones", 
    "oil", "gas", "energy", "merger", "acquisition", "ipo", "finance", "financial"
}

sci_tech_keywords = {
    "software", "internet", "computer", "microsoft", "google", "apple", "linux", "virus", "space", 
    "nasa", "science", "research", "study", "cell", "phone", "technology", "tech", "web", "online", 
    "digital", "chip", "processor", "intel", "amd", "ibm", "server", "network", "wireless", "satellite"
}

world_keywords = {
    "iraq", "president", "election", "war", "peace", "government", "minister", "official", "united nations", 
    "un", "eu", "police", "court", "judge", "military", "army", "troop", "bomb", "attack", "kill", 
    "party", "politic", "congress", "senate", "law", "bill", "vote", "voter", "candidate", "campaign"
}

def classify(text):
    text = text.lower()
    scores = {"Sports": 0, "Business": 0, "Sci/Tech": 0, "World": 0}
    
    words = text.split()
    for word in words:
        # Strip punctuation
        word = word.strip('.,;:"\'()?!')
        if word in sports_keywords: scores["Sports"] += 1
        if word in business_keywords: scores["Business"] += 1
        if word in sci_tech_keywords: scores["Sci/Tech"] += 1
        if word in world_keywords: scores["World"] += 1
    
    # Priority if ambiguous?
    # Return the category with max score
    if max(scores.values()) == 0:
        return "Unknown"
    
    return max(scores, key=scores.get)

# Sort by description length
articles.sort(key=lambda x: len(x['description']), reverse=True)

# Find first sports article
candidate = None
for art in articles:
    # Combine title and description for classification
    full_text = art['title'] + " " + art['description']
    category = classify(full_text)
    if category == "Sports":
        candidate = art
        break

print("__RESULT__:")
if candidate:
    print(json.dumps({"title": candidate['title'], "length": len(candidate['description']), "description_preview": candidate['description'][:100]}))
else:
    print(json.dumps({"error": "No sports article found"}))"""

env_args = {'var_function-call-5600887256776046897': [{'_id': '694468d48f62606ef06538a3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-6243788860290969808': ['authors', 'article_metadata'], 'var_function-call-621124544545937450': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-14125888797793058960': [{'_id': '694468d48f62606ef06538a3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694468d48f62606ef06538a4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694468d48f62606ef06538a5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694468d48f62606ef06538a6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694468d48f62606ef06538a7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-371116049882488257': [{'author_id': '0', 'name': 'Felicia Miles'}, {'author_id': '1', 'name': 'Stacy Hunt'}, {'author_id': '2', 'name': 'Carol Reed'}, {'author_id': '3', 'name': 'Dr. Daniel Brown'}, {'author_id': '4', 'name': 'Andre Lam MD'}], 'var_function-call-16428439284826624530': [{'_id': '694468d48f62606ef06538a3', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694468d48f62606ef06538a4', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694468d48f62606ef06538a5', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694468d48f62606ef06538a6', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694468d48f62606ef06538a7', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7895339117705645390': {'count': 5, 'sample_titles': ['Wall St. Bears Claw Back Into the Black (Reuters)', 'Carlyle Looks Toward Commercial Aerospace (Reuters)', "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'Oil prices soar to all-time record, posing new menace to US economy (AFP)']}, 'var_function-call-15665066354817605845': 'file_storage/function-call-15665066354817605845.json', 'var_function-call-4236206756542118061': {'count': 10000}, 'var_function-call-8284316981365420739': 'file_storage/function-call-8284316981365420739.json'}

exec(code, env_args)
