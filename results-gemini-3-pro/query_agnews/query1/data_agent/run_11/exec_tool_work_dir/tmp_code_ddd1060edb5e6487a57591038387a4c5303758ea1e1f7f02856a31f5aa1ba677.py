code = """import json

with open(locals()['var_function-call-6947491916061976961'], 'r') as f:
    articles = json.load(f)

sports_keywords = [
    "olympic", "athens", "medal", "gold medal", "silver medal", "bronze medal",
    "football", "soccer", "basketball", "baseball", "tennis", "golf", "hockey", "cricket", "rugby",
    "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "wta", "atp", "pga", "lpga", "nascar", "f1", "formula one",
    "world cup", "super bowl", "championship", "tournament", "grand slam", "davis cup", "ryder cup",
    "quarterfinal", "semifinal", "quarter-final", "semi-final",
    "touchdown", "homerun", "goal", "wicket", "hat-trick", "shutout",
    "sprint", "marathon", "relay", "gymnastics", "swimming", "boxing", "wrestling", "volleyball",
    "athlete", "quarterback", "receiver", "pitcher", "striker", "goalie", "goalkeeper", "referee", "umpire",
    "game", "match", "league", "cup", "team", "squad", "club", "coach", "manager", "player",
    "win", "won", "loss", "lost", "draw", "score", "season", "playoff", "series", "final", "champion",
    "sport", "racing", "driver", "track", "field", "stadium", "arena", "u.s. open", "us open", "wimbledon", "french open"
]

negative_keywords = [
    "stock", "market", "economy", "bank", "investment", "fund", "company", "corp", "inc", "ceo", "profit",
    "software", "computer", "internet", "web", "technology", "science", "microsoft", "google", "apple", "linux", "java", "code", "blog", "rss",
    "iraq", "war", "president", "minister", "government", "police", "court", "judge", "election", "poll", "party", "killed", "bomb",
    "movie", "film", "television", "tv", "actor", "actress", "drama", "show", "entertainment", "hollywood"
]

def get_sports_score(title, description):
    text = (title + " " + description).lower()
    
    score = 0
    # Check positive keywords
    for k in sports_keywords:
        # Check for whole word match to avoid substrings like "win" in "winter"
        # Using simple check first
        if k in text:
            score += 1
            # Boost specific terms
            if k in ["olympic", "nba", "nfl", "mlb", "nhl", "fifa", "world cup", "championship", "tournament", "medal", "athlete", "wimbledon", "u.s. open", "us open"]:
                score += 2
                
    # Check negative keywords
    neg_score = 0
    for k in negative_keywords:
        if k in text:
            neg_score += 1
    
    # Penalize
    score -= (neg_score * 3)
    
    return score

candidates = []
for art in articles:
    s = get_sports_score(art.get("title", ""), art.get("description", ""))
    if s > 2: # Threshold
        candidates.append({
            "title": art["title"],
            "description": art["description"],
            "len": len(art["description"]),
            "score": s
        })

candidates.sort(key=lambda x: x["len"], reverse=True)

print("__RESULT__:")
print(json.dumps(candidates[:10]))"""

env_args = {'var_function-call-15580350581523998620': ['articles'], 'var_function-call-15580350581523998523': [{'_id': '69446b549762fc32b4d1b1ae', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-15580350581523998426': ['authors', 'article_metadata'], 'var_function-call-15580350581523998329': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-2000961058329415325': [{'_id': '69446b549762fc32b4d1b1ae', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446b549762fc32b4d1b1af', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446b549762fc32b4d1b1b0', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446b549762fc32b4d1b1b1', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446b549762fc32b4d1b1b2', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6947491916061976961': 'file_storage/function-call-6947491916061976961.json', 'var_function-call-5506273525767004531': {'title': 'Pretty Log4J', 'desc_len': 708}, 'var_function-call-18437170732192184940': [{'title': 'Pretty Log4J', 'description': '\\\\I\'ve been a big fan of Log4J  for a while now but haven\'t migrated any code\\over for one central reason.  The following line of code:\\\\    final static Logger logger = Logger.getLogger( "some.name" );\\\\... is amazingly ugly and difficult to work with.\\\\Most people use Log4J with a logger based on the classname:\\\\So we would probably see:\\\\    static Logger logger = Logger.getLogger( "org.apache.commons.feedparser.locate.FeedLocator" );\\\\Which is amazingly verbose.  A lot of developers shorten this to:\\\\    static Logger logger = Logger.getLogger( FeedLocator.class );\\\\But this still leaves us with cut and paste errors.\\\\What if we could just reduce it to:\\\\    static Logger logger = Logger.g ...\\\\', 'len': 708, 'scores': {'Sports': 1, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': 'Check Out Rojo', 'description': '\\\\John Battelle blogs about Rojo :\\\\"Yesterday I hung out with Chris Alden, a founder of the original Red Herring\\who has moved his focus to publishing in a Web 2.0 world (in other words, a\\fellow traveler). He\'s putting the finishing touches on a new publishing\\platform/feed reader called Rojo (think "mojo") that he and his team have been\\working on for quite some time now. It\'s moved into invitation-only beta\\recently, and he gave me a tour. I liked it quite a bit. Think of it as a\\second-generation RSS aggregator with some subtle social networking,\\recommendation, and republishing juice."\\\\I co-founded Rojo about a year ago with Chris Alden  and Mark Graham\\(peace.net, iVillage, etc) after  ...\\\\', 'len': 708, 'scores': {'Sports': 2, 'Business': 0, 'Sci/Tech': 2, 'World': 2}}, {'title': 'Serena Reaches Fourth Round of U.S. Open (AP)', 'description': "AP - Hardly at her best, barely beating one of the tour's pesky teens, Serena Williams suddenly found herself face-down at the U.S. Open. Running for a ball she couldn't reach, the six-time Grand Slam champion slipped and planted both palms on court to brace herself. Williams shook the sting out of her hands, beckoned a ball boy to retrieve her fallen racket, then took her sweet time before facing break point. Recomposed, Williams smacked a service winner at 111 mph, an ace just as fast, and forced an error. Just like that, she held serve en route to beating 30th-seeded Tatiana Golovin 7-5, 6-4 Friday night to reach the Open's fourth round.", 'len': 648, 'scores': {'Sports': 2, 'Business': 0, 'Sci/Tech': 0, 'World': 1}}, {'title': 'THECHAT', 'description': '&lt;em&gt; Dean Cain has spent much of his life in a uniform. He\'s done time as an all-American safety at Princeton (where he established a since-broken single-season Division I-AA record for interceptions), an undrafted free agent with the Buffalo Bills (before a preseason knee injury ended his football career), a sportsman of the future (in the aptly named movie "Futuresport") and an iconic superhero (in television\'s "Lois and Clark: The New Adventures of Superman"). Next up is a set of pinstripes -- Cain plays star third baseman Conrad Dean in the CBS drama "Clubhouse," which is scheduled to debut next month. &lt;/em&gt;', 'len': 631, 'scores': {'Sports': 3, 'Business': 0, 'Sci/Tech': 1, 'World': 0}}, {'title': 'Swiss Army Medicine (Forbes.com)', 'description': "Forbes.com - Early last year 61-year-old Judy Norris was ready to stop all treatment and let her cancer run its course. Her kidney tumor, diagnosed in 1997, had spread to her abdomen, pancreas and both lungs. Six months of treatment with toxic interleukin-2, one of the only treatments for advanced kidney cancer, had eroded nerves in her hands and feet, caused frequent vomiting and made her skin peel all over--but did nothing to slow the tumors' relentless growth. In June, in a last-ditch effort to save her life, her oncologist recommended an experimental pill from Pfizer called SU11248. ...", 'len': 597, 'scores': {'Sports': 1, 'Business': 0, 'Sci/Tech': 1, 'World': 1}}], 'var_function-call-12630071079352670922': [{'title': 'THECHAT', 'description': '&lt;em&gt; Dean Cain has spent much of his life in a uniform. He\'s done time as an all-American safety at Princeton (where he established a since-broken single-season Division I-AA record for interceptions), an undrafted free agent with the Buffalo Bills (before a preseason knee injury ended his football career), a sportsman of the future (in the aptly named movie "Futuresport") and an iconic superhero (in television\'s "Lois and Clark: The New Adventures of Superman"). Next up is a set of pinstripes -- Cain plays star third baseman Conrad Dean in the CBS drama "Clubhouse," which is scheduled to debut next month. &lt;/em&gt;', 'len': 631}, {'title': 'Sprint certifies QuickTime, Xserve G5 for phone media (MacCentral)', 'description': "MacCentral - Telecommunications company Sprint on Thursday announced that it has certified Apple's Xserve G5 and QuickTime as mobile multimedia delivery platforms for Sprint's own PCS Vision Multimedia Services. This enables content service providers to use Xserve G5 systems and QuickTime to deliver streaming audio and video clips to Sprint customers whose phones support Sprint's new Vision Multimedia Service. The service provides content from CNN, NBC, Fox Sports, The Weather Channel, E! Entertainment, mFlix and other companies. ...", 'len': 539}, {'title': 'U.S. Bounces Back to Beat Greece 77-71', 'description': "ATHENS, Greece - Lamar Odom made a key defensive play on Greece's Dimitris Pipanikoulaou, preventing him from getting a clean layup attempt that could have cut the United States' lead to two points, and the Americans won 77-71 Tuesday night in the second round of the Olympic men's basketball tournament.    In a much closer game than expected, the Americans bounced back from their embarrassing loss to Puerto Rico in their opener and avoided dropping to 0-2, which would have matched their loss total from the previous 68 years...", 'len': 532}, {'title': 'Health Highlights: Aug. 17, 2004', 'description': 'Here are some of the latest health and medical news developments, compiled by editors of HealthDay:    -----     Arizona Leads Nation in West Nile Cases      Thousands of abandoned swimming pools, along with irrigation canals and other prime breeding sites for mosquitoes in Phoenix, have made Arizona the state hardest hit by West Nile virus this year.      Arizona has accounted for at least 290 of more than 500 reported cases of West Nile virus in the United States so far in 2004...', 'len': 487}, {'title': 'DiMarco, Riley Play Way Into Ryder Cup (AP)', 'description': "AP - Chris DiMarco and Chris Riley faced knee-knocking pressure in the last round of the PGA Championship. And what did they get for their efforts? More of the same. DiMarco and Riley played themselves into the pressure-packed Ryder Cup with their performances Sunday in the year's final major. DiMarco finished second after a three-man, three-hole playoff and Riley was fourth  #151; good enough to knock Jay Haas and Steve Flesch out of the top 10 in the Ryder Cup point standings.", 'len': 483}]}

exec(code, env_args)
