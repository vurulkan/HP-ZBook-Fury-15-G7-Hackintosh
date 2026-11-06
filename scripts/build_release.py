#!/usr/bin/env python3
"""Build the sanitized release; never reads the live EFI or local audit folders."""
import argparse
import hashlib
import pathlib
import re
import zipfile
from validate import validate


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tag', default='v1.0.0')
    options = parser.parse_args()
    if not re.fullmatch(r'v[0-9]+\.[0-9]+\.[0-9]+', options.tag):
        parser.error('Use a tag such as v1.0.0')
    root = pathlib.Path(__file__).resolve().parents[1]
    validate(root)
    output = root / 'dist'
    output.mkdir(exist_ok=True)
    filename = f'HP-ZBook-Fury-15-G7-OpenCore-1.0.8-{options.tag}.zip'
    archive = output / filename
    files = []
    for folder in ('EFI', 'Sources', 'docs', 'licenses', 'scripts'):
        files.extend(p for p in (root / folder).rglob('*') if p.is_file() and
                     '__pycache__' not in p.parts and p.suffix != '.pyc')
    files.extend(root / name for name in ('README.md', 'README.tr.md', 'LICENSE', 'THIRD_PARTY.md'))
    sums = ''.join(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + p.relative_to(root).as_posix() + '\n'
                   for p in sorted(files) if p.is_relative_to(root / 'EFI'))
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        def add(name, data):
            info = zipfile.ZipInfo(name, date_time=(2026, 11, 7, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            executable = '/Contents/MacOS/' in name
            info.external_attr = (0o100755 if executable else 0o100644) << 16
            z.writestr(info, data)
        for file in sorted(files):
            add(file.relative_to(root).as_posix(), file.read_bytes())
        add('EFI-SHA256SUMS.txt', sums.encode())
    with zipfile.ZipFile(archive) as z:
        if z.testzip() is not None:
            raise RuntimeError('Archive CRC validation failed')
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (output / 'SHA256SUMS.txt').write_text(digest + '  ' + filename + '\n')
    print(archive)
    print(digest)


if __name__ == '__main__':
    main()
