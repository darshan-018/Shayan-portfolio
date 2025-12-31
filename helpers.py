import re

def extract_youtube_id(text):
    patterns = [
        r'youtube\.com\/watch\?v=([^&]+)',
        r'youtu\.be\/([^?&]+)',
        r'youtube\.com\/embed\/([^?&]+)'
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1)
    return None
