#!/usr/bin/env python3
"""Validate the shape of an AI Video Editor plan."""
import argparse, re, sys
from pathlib import Path

HEADINGS = [
    "PROJECT ANALYSIS", "EDITING STYLE", "MUSIC / BPM", "TIMELINE",
    "CUT PLAN", "TRANSITION PLAN", "SPEED PLAN", "MOTION PLAN",
    "SOUND DESIGN", "COLOR GRADING", "TEXT / TYPOGRAPHY",
    "SOFTWARE-SPECIFIC STEPS", "EXPORT SETTINGS", "FINAL QUALITY CHECK",
]
TIME = re.compile(r"\b\d{1,2}:\d{2}(?:[.:]\d{1,3})?\b")
PURPOSE = re.compile(r"\b(why|purpose|reason|because|to )\b", re.I)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('file', type=Path)
    args = ap.parse_args()
    text = args.file.read_text(encoding='utf-8')
    missing = [h for h in HEADINGS if h not in text.upper()]
    times = TIME.findall(text)
    warnings = []
    if missing: warnings.append('missing headings: ' + ', '.join(missing))
    if len(times) < 2: warnings.append('add at least two timecodes to make the timeline executable')
    if 'transition' in text.lower() and not PURPOSE.search(text): warnings.append('state a purpose for transitions/effects')
    if warnings:
        print('WARNINGS')
        print('\n'.join('- ' + w for w in warnings))
        return 1
    print(f'OK: {args.file} contains all required sections and {len(times)} timecodes.')
    return 0
if __name__ == '__main__': sys.exit(main())
