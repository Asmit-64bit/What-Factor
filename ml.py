import spacy
from collections import Counter

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

text_data = "Tch, what a drag! This is nothing for a genius like me. I'll just use my Shadow Clone Jutsu, send them to the tops of the tallest trees to get a good look around. They'll find the way back to the village in no time. I'll be home for dinner! Believe it!"

# Process the text with the spaCy model
doc = nlp(text_data)

# Get the base form (lemma) of each word, ignoring punctuation and spaces
lemmas = [token.lemma_ for token in doc if not token.is_punct and not token.is_space]

# Count the lemmas
lemma_counts = Counter(lemmas)

# Find the most common lemma
most_common_lemma_info = lemma_counts.most_common(1)[0]

print(f"The words are: {lemmas}")
print(f"The most common root word is '{most_common_lemma_info[0]}' with {most_common_lemma_info[1]} occurrences.")
print("\n" + "="*50 + "\n")

# --- Your Data ---
Analytical = ['think','check','ask', 'prove', 'research', 'organize', 'sort', 'plan', 'question','explain', 'figure-out', 'look-into', 'reason', 'calculate', 'examine', 'double-check', 'break-down','compare', 'map-out', 'analyze']
Creative = ['create', 'imagine', 'make', 'build', 'try', 'doodle', 'sketch', 'play', 'invent', 'design', 'brainstorm', 'daydream', 'express', 'explore', 'picture', 'change', 'improvise', 'wonder', 'make-up', 'see']
Pragmatic = ['do', 'act', 'fix', 'solve', 'work', 'make', 'build', 'finish', 'handle', 'manage', 'focus', 'start', 'simplify', 'achieve', 'adapt', 'apply', 'deliver', 'get-it-done', 'deal-with', 'complete']
Intuitive = ['feel', 'sense', 'guess', 'know', 'read', 'notice', 'listen', 'trust-my-gut', 'get-a-vibe', 'suspect', 'understand', 'predict', 'anticipate', 'feel-out', 'get-a-hunch', 'empathize', 'just-know', 'wonder']
Impulsive = ['act', 'jump', 'go', 'risk', 'rush', 'wing-it', 'react', 'decide-fast', 'dive-in', 'speak-first', 'do-it', 'feel', 'dare', 'just-go', 'commit', 'get-going', 'hurry', 'plunge']
veryHigh = ['lead', 'win', 'build', 'create', 'innovate', 'dominate', 'conquer', 'change-the-world', 'pioneer', 'strive', 'push', 'excel', 'forge', 'establish', 'hustle', 'demand', 'achieve', 'master']
High = ['lead', 'win', 'grow', 'achieve', 'succeed', 'build', 'climb', 'advance', 'push', 'compete', 'earn', 'drive', 'perform', 'excel', 'focus', 'aim-high', 'accomplish', 'progress']
Medium = ['work', 'help', 'support', 'provide', 'contribute', 'maintain', 'secure', 'improve', 'deliver', 'manage', 'focus', 'handle', 'do-my-part', 'commit', 'balance', 'collaborate', 'finish', 'perform']
Low = ['relax', 'chill', 'coast', 'enjoy', 'live', 'balance', 'accept', 'flow', 'drift', 'cruise', 'unplug', 'settle', 'disconnect', 'just-be', 'breathe', 'get-by', 'participate', 'exist']
LawfulGood = ['help', 'obey', 'follow-rules', 'protect', 'serve', 'defend', 'support', 'care', 'respect', 'honor', 'volunteer', 'do-right', 'cooperate', 'trust', 'believe', 'contribute', 'guide', 'build']
LawfulNeutral = ['follow', 'obey', 'enforce', 'report', 'file', 'organize', 'manage', 'judge', 'adhere', 'comply', 'regulate', 'document', 'process', 'uphold', 'respect-authority', 'maintain', 'conform', 'execute']
# FIXED: Removed trailing comma
LawfulEvil = ['control', 'rule', 'command', 'plot', 'scheme', 'manipulate', 'exploit', 'dominate', 'profit', 'manage', 'influence', 'direct', 'use-the-system', 'dictate', 'enforce', 'gain', 'take-over', 'leverage']
NeutralGood = ['help', 'give', 'care', 'fix', 'support', 'heal', 'rescue', 'share', 'comfort', 'protect', 'aid', 'assist', 'listen', 'volunteer', 'improve', 'nurture', 'intervene', 'do-good']
trueNeutral = ['watch', 'wait', 'survive', 'adapt', 'avoid', 'ignore', 'balance', 'focus-on-me', 'stay-out', 'detach', 'decide', 'exist', 'cope', 'live', 'work', 'observe', 'choose', 'stay-neutral']
NeutralEvil = ['take', 'win', 'use', 'profit', 'gain', 'benefit', 'survive', 'scheme', 'betray', 'hustle', 'scam', 'deceive', 'get-ahead', 'look-out-for-me', 'manipulate', 'exploit', 'prioritize-myself', 'acquire']
ChaoticGood = ['help', 'fight', 'rebel', 'break-rules', 'protect', 'challenge', 'rescue', 'speak-out', 'act', 'support', 'defy', 'question', 'improvise', 'liberate', 'champion', 'care', 'disrupt', 'stand-up']
ChaoticNeutral = ['drift', 'wander', 'choose', 'act', 'want', 'feel', 'risk', 'ignore-rules', 'live-free', 'improvise', 'enjoy', 'play', 'react', 'explore', 'do-my-thing', 'decide', 'am-free', 'go-my-own-way']
ChaoticEvil = ['destroy', 'hurt', 'break', 'ruin', 'lie', 'steal', 'betray', 'harm', 'enjoy-chaos', 'take', 'bully', 'corrupt', 'incite', 'defy', 'indulge', 'manipulate', 'vandalize', 'break-things']
Volatile = ['snap', 'yell', 'explode', 'rage', 'react', 'storm', 'vent', 'get-mad', 'feel-strongly', 'flare-up', 'lose-my-temper', 'get-worked-up', 'gush', 'boil-over', 'lash-out', 'get-loud', 'shout', 'get-intense']
Expressive = ['share', 'show', 'talk', 'laugh', 'cry', 'hug', 'connect', 'emote', 'open-up', 'react', 'feel', 'reveal', 'engage', 'smile', 'welcome', 'gesture', 'am-open', 'am-clear']
Reserved = ['watch', 'listen', 'think', 'observe', 'hide', 'internalize', 'stay-quiet', 'hold-back', 'stay-calm', 'reflect', 'analyze', 'manage', 'control', 'retreat', 'ponder', 'am-private', 'keep-to-myself', 'process']
Stoic = ['endure', 'cope', 'handle', 'accept', 'continue', 'carry-on', 'tolerate', 'face', 'bear', 'suppress', 'control', 'manage', 'persist', 'stay-strong', 'push-through', 'stay-calm', 'am-steady', 'am-unbothered']
Subdued = ['am-quiet', 'listen', 'calm', 'relax', 'soften', 'fade', 'observe', 'accept', 'stay-peaceful', 'go-unnoticed', 'be-gentle', 'yield', 'withdraw', 'reflect', 'understate', 'murmur', 'am-still', 'am-mellow']
Strategic = ['plan', 'think-ahead', 'prepare', 'aim', 'consider', 'look-ahead', 'plot', 'position', 'map-out', 'predict', 'evaluate', 'weigh', 'calculate', 'set-up', 'expect', 'wait', 'out-think', 'guide', 'see-the-end', 'think-long-term']

# A dictionary to hold all your sets for easy access
all_sets = {
    "Set A (Analytical)": Analytical,
    "Set B (Creative)": Creative,
    "Set C (Pragmatic)": Pragmatic,
    "Set D (Intuitive)": Intuitive,
    "Set E (Impulsive)": Impulsive,
    "Set F (veryHigh)": veryHigh,
    "Set G (High)": High,
    "Set H (Medium)": Medium,
    "Set I (Low)": Low,
    "Set J (LawfulGood)": LawfulGood,
    "Set K (LawfulNeutral)": LawfulNeutral,
    "Set L (LawfulEvil)": LawfulEvil,
    "Set M (NeutralGood)": NeutralGood,
    "Set N (trueNeutral)": trueNeutral,
    "Set O (NeutralEvil)": NeutralEvil,
    "Set P (ChaoticGood)": ChaoticGood,
    "Set Q (ChaoticNeutral)": ChaoticNeutral,
    "Set R (ChaoticEvil)": ChaoticEvil,
    "Set S (Volatile)": Volatile,
    "Set T (Expressive)": Expressive,
    "Set U (Reserved)": Reserved,
    "Set V (Stoic)": Stoic,
    "Set W (Subdued)": Subdued,
    "Set X (Strategic)": Strategic    
}

# --- Analysis 1: Find set with most duplicate words ---
print("ANALYSIS 1: Finding set with most word repetitions")
print("-" * 50)
highest_score = -1
flagged_set_name = None

for name, word_list in all_sets.items():
    if not word_list:
        continue
    
    word_counts = Counter(word_list)
    # Get the count of the most repeated word
    current_set_score = word_counts.most_common(1)[0][1]
    
    print(f"{name}: Most frequent word appears {current_set_score} times.")
    
    if current_set_score > highest_score:
        highest_score = current_set_score
        flagged_set_name = name

print("\n" + "="*50)
if flagged_set_name:
    print(f"✅ Flagged Set: {flagged_set_name} (with a top score of {highest_score})")
else:
    print("Could not flag a set.")

# --- Analysis 2: Find set with most keyword matches ---
print("\n\nANALYSIS 2: Finding set with most keyword matches")
print("-" * 50)

# FIXED: Use keywords that actually exist in the sets
keywords = ["help", "build", "act", "feel", "plan"]

highest_keyword_count = -1
flagged_set_name_by_keyword = None

for name, word_list in all_sets.items():
    keyword_count = sum(1 for word in word_list if word in keywords)
    
    print(f"{name}: Found {keyword_count} keywords.")
    
    if keyword_count > highest_keyword_count:
        highest_keyword_count = keyword_count
        flagged_set_name_by_keyword = name

print("\n" + "="*50)
if flagged_set_name_by_keyword:
    print(f"✅ Flagged Set (by keyword): {flagged_set_name_by_keyword} (with {highest_keyword_count} matches)")
else:
    print("Could not flag a set.")