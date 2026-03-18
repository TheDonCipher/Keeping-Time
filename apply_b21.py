import re
import os

file_path = 'KeepingTime_VolumeOne.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Define the exact word replacements requested
replacements = {
    r'\bmanual digits\b': 'hands',
    r'\boptical sensors? (\bwere\b|\bwas\b)?': 'eyes ', # "eyes were"
    r'\boptical sensors\b': 'eyes',
    r'\bexecuted a negative lateral head movement\b': 'shook his head',
    r'\bexecuted a positive lateral head movement\b': 'nodded',
    r'\binitiated a respiratory cycle\b': 'took a breath',
    r'\bassumed a seated position\b': 'sat down',
    r'\bassumed a standing position\b': 'stood',
    r'\bcervical region\b': 'neck',
    r'\bproximate biological entity\b': 'the person next to him',
    r'\bThe subject maintained position\b': 'Taro didn\'t move',
    r'\bocular inputs\b': 'eyes',
    r'\bauditory receivers\b': 'ears',
    r'\bdirected his optical focus\b': 'looked',
    r'\bphysical latch\b': 'door handle',
    r'\bkinetic force\b': 'force',
    # Some other specific ones:
    r'\bThe subject executed\b': 'He',
    r'\belevated his (arm|hand|leg|limb|appendage)\b': r'raised his \1',
    r'\btraversed to\b': 'walked to',
}

# The rule says: Keep clinical vocabulary in dialogue when spoken by Hana, Voss, or Krell.
# Only simplify third-person prose narration.
# Also "The subject" -> "Taro" or "He" where appropriate.
# "vocalization" -> "voice"

# Function to apply replacements to prose (outside of quotes)
def process_prose_block(text):
    for k, v in replacements.items():
        # Case insensitive to catch "The Subject" vs "the subject" if needed, but we'll use regex flags
        text = re.sub(k, v, text, flags=re.IGNORECASE)
        
    text = re.sub(r'\bvocalization\b', 'voice', text, flags=re.IGNORECASE)
    
    # Specific Subject replacement to Taro, but keeping capitalization
    text = re.sub(r'\bThe subject\b', 'Taro', text)
    text = re.sub(r'\bthe subject\b', 'Taro', text)
    
    # Cleanup any "Taro didn't move" -> "The subject maintained position" was replaced
    text = re.sub(r'Taro didn\'t move', "Taro didn't move", text) 
    
    # "optical sensors were" -> "eyes were" happens automatically, but let's clean grammar:
    text = text.replace('eyes was', 'eyes were')
    
    text = text.replace('his hands', 'his hands')
    return text

# We process the text inside <p> or <blockquote> tags or just generally outside of quotation marks
# Let's write a function that splits by HTML tags and quotes, to ensure we don't mess up HTML attributes or dialogue

parts = re.split(r'(<[^>]+>|"[^"]*"|“[^”]*”)', html_content)
# parts[0] is text outside tags/quotes
# parts[1] is tag/quote
# parts[2] is text outside

for i in range(len(parts)):
    part = parts[i]
    if i % 2 == 0:
        # This is plain text between tags and quotes
        parts[i] = process_prose_block(part)
    pass # we might want to also do dialogue, but the rule says "only simplify third-person prose narration".
          # We'll leave anything inside " quotes empty of replacements.

new_html_content = "".join(parts)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_html_content)

print("Applied B21 replacements.")
