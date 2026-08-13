from anthropic import Anthropic

MODEL = "claude-sonnet-5"
_client = None

def _get_client():
    global _client
    if _client is None:
        _client = Anthropic()
    return _client

SYSTEM_PROMPT = """Generate spoken narration for slides."""

def generate_narration(slide, deck_title, slide_count, previous_narration=None):
    client = _get_client()
    return ""
