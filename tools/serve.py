#!/usr/bin/env python3
"""Serve app/ on http://localhost:8080 for running the map in an ordinary browser.

A browser will not load the .wasm binaries from a file:// URL, so double-clicking
index.html does not work; this is the smallest thing that does.
"""
import http.server, os, sys, webbrowser

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'app')
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080

class H(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map,
                      '.wasm': 'application/wasm', '.webp': 'image/webp', '.woff2': 'font/woff2'}
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)
    def log_message(self, *a):
        pass

os.chdir(ROOT)
with http.server.ThreadingHTTPServer(('127.0.0.1', PORT), H) as srv:
    url = f'http://localhost:{PORT}/'
    print(f'Daybreak Star Map at {url}  (Ctrl+C to stop)')
    try:
        webbrowser.open(url)
    except Exception:
        pass
    srv.serve_forever()
