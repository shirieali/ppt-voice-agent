"""Extract slide content and render slide images from a .pptx file."""
import glob, os, re, subprocess, tempfile
from pptx import Presentation

def _run(cmd, timeout=180):
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    return result
