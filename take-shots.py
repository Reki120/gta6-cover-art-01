#!/usr/bin/env python3
"""Capture the studio's deterministic scenes using local headless Chrome."""
import io
import json
from pathlib import Path
import subprocess
import tempfile
import time
import urllib.parse
import urllib.request
from PIL import Image, ImageStat

ROOT = Path(__file__).resolve().parent
CHROME = '/home/hatch/.cache/ms-playwright/chromium-1255/chrome-linux64/chrome'
LIMIT = 256 * 1024

def main():
    scenes = json.loads((ROOT / 'shots.json').read_text())
    destination = ROOT / 'screenshots'
    destination.mkdir(exist_ok=True)
    server = subprocess.Popen(['node', 'serve.ts', '--port', '8123'], cwd=ROOT,
                              stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    try:
        for _ in range(100):
            if server.poll() is not None:
                raise RuntimeError(server.stderr.read().decode())
            try:
                with urllib.request.urlopen('http://localhost:8123', timeout=1) as response:
                    if response.status == 200:
                        break
            except OSError:
                time.sleep(.1)
        else:
            raise RuntimeError('Server did not become ready')
        with tempfile.TemporaryDirectory(prefix='neon-shots-') as temporary:
            for scene in scenes:
                capture = Path(temporary) / 'capture.png'
                subprocess.run([CHROME, '--headless=new', '--no-sandbox', '--disable-dev-shm-usage',
                                '--hide-scrollbars', '--no-first-run',
                                f'--user-data-dir={temporary}/profile',
                                f'--screenshot={capture}', f'--window-size={scene["w"]},{scene["h"]}',
                                '--virtual-time-budget=8000',
                                'http://localhost:8123/' + scene['query']],
                               check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, timeout=45)
                with Image.open(capture) as original:
                    picture = original.convert('RGB')
                picture.thumbnail((1280, 1280), Image.Resampling.LANCZOS)
                if min(picture.size) < 480:
                    raise RuntimeError('Capture short side is below 480px')
                for quality in range(94, 19, -2):
                    buffer = io.BytesIO()
                    picture.save(buffer, 'JPEG', quality=quality, optimize=True)
                    if buffer.tell() <= LIMIT:
                        break
                else:
                    raise RuntimeError('Cannot fit JPEG within 256 KiB')
                target = destination / scene['name']
                target.write_bytes(buffer.getvalue())
                print(f'{target.relative_to(ROOT)}: {picture.width}x{picture.height}, {target.stat().st_size} bytes; RGB stddev {ImageStat.Stat(picture).stddev}')
        expected = {scene['name'] for scene in scenes}
        for old in destination.iterdir():
            if old.is_file() and old.name not in expected:
                old.unlink()
    finally:
        server.terminate()
        try:
            server.wait(timeout=5)
        except subprocess.TimeoutExpired:
            server.kill()
            server.wait()
        server.stderr.close()

if __name__ == '__main__':
    main()
