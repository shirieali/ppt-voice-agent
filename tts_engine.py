"""Convert narration text to speech with edge-tts and report clip duration."""
import edge_tts
from mutagen.mp3 import MP3

DEFAULT_VOICE = "en-US-AriaNeural"
