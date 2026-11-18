"""Recover the editable static release from the small, self-contained web build."""
from pathlib import Path
import base64
import gzip
import re

root = Path(__file__).resolve().parent
packed = (root / 'index.html').read_text()
payload = re.search(r"atob\('([A-Za-z0-9+/=]+)'\)", packed).group(1)
html = gzip.decompress(base64.b64decode(payload)).decode()
out = root / 'source'
out.mkdir(exist_ok=True)
scripts = re.findall(r'<script>(.*?)</script>', html, re.S)
assert len(scripts) == 2, 'Unexpected build structure'
(out / 'three.min.js').write_text(scripts[0])
(out / 'game.js').write_text(scripts[1])
html = html.replace('<script>' + scripts[0] + '</script>', '<script src="three.min.js"></script>', 1)
html = html.replace('<script>' + scripts[1] + '</script>', '<script src="game.js"></script>', 1)
(out / 'index.html').write_text(html)
notice = re.search(r'<!-- Third-party notice: Three.js\n(.*?)\n-->', html, re.S)
if notice:
    (out / 'THREE-LICENSE.txt').write_text(notice.group(1))
print('Recovered editable game in source/')
