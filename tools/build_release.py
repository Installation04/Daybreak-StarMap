#!/usr/bin/env python3
"""Turn a published map page into the standalone app page.

Usage: build_release.py <published index.html> <app/index.html> <version>

The published page arrives wrapped in the hosting service's own document head; the
standalone page is the document that begins at the second <!doctype html>. Every
other edit is an exact-match replacement that must occur exactly once.
"""
import sys, pathlib

SRC, OUT, VER = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), sys.argv[3]
s = SRC.read_text(encoding='utf-8')
LOG = []

def rep(old, new, tag):
    global s
    c = s.count(old)
    if c != 1:
        raise SystemExit(f'{tag}: expected 1 match, found {c}: {old[:80]!r}')
    s = s.replace(old, new); LOG.append(tag)

# 1. strip the hosting wrapper: keep from the page's own doctype onward
parts = s.split('<!doctype html>')
if len(parts) == 3:
    s = '<!doctype html>' + parts[2]; LOG.append('wrapper-stripped')
elif len(parts) == 2:
    LOG.append('no-wrapper')
else:
    raise SystemExit(f'unexpected doctype count {len(parts)-1}')
assert s.startswith('<!doctype html><html lang="en"><head>')
assert s.count('</head><body>') == 1 and s.rstrip().endswith('</body></html>')

# 2. creators line in the About sheet
rep('<p>Built by Faber.</p>',
    '<p>Built by Faber and Tacitus. Faber built the map: the code, the placements, the system models and the write-ups. Tacitus made the Project Daybreak charts and the Daybreak galaxy map that the placements follow.</p>',
    'about-creators')

# 3. version stamp in the About sheet heading line
rep('<h2 id="aboutH">About this map</h2><p>What it is, and where everything came from</p>',
    f'<h2 id="aboutH">About this map</h2><p>Version {VER}. What it is, and where everything came from</p>',
    'about-version')

# 4. name the Henry Draper catalogue among AT-HYG's parents, as CREDITS.md does
rep('compiled from Hipparcos and Tycho-2 (ESA), Gaia DR3, the Yale Bright Star Catalogue',
    'compiled from Hipparcos and Tycho-2 (ESA), Gaia DR3, the Henry Draper catalogue, the Yale Bright Star Catalogue',
    'about-henry-draper')

OUT.write_text(s, encoding='utf-8')
print(f'wrote {OUT} ({len(s):,} chars): ' + ', '.join(LOG))
