import yaml
import re

def load_stories():
    with open("user_stories/stories.yaml") as f:
        return yaml.safe_load(f)

def extract_test_mapping():
    mapping = {}

    with open("tests/test_app.py") as f:
        lines = f.readlines()

    current_story = None

    for line in lines:
        # Detect story ID
        story_match = re.search(r'US-\d+', line)
        if story_match:
            current_story = story_match.group()

        # Detect test function
        test_match = re.search(r'def (test_\w+)', line)
        if test_match and current_story:
            test_name = test_match.group(1)
            mapping[current_story] = test_name
            current_story = None

    return mapping