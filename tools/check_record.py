"""Validate the exact 15-record layout and complete PDF source listings."""
import hashlib
import json
import re
from pathlib import Path
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
def main():
    folders=sorted(ROOT.glob('Exercise_*'))
    assert [p.name for p in folders]==[f'Exercise_{n:02d}' for n in range(1,16)]
    assert len(list(ROOT.rglob('*.pdf')))==15
    data=json.loads((ROOT/'tools/experiment_data.json').read_text())
    manifest=json.loads((ROOT/'record_manifest.json').read_text())
    for item,entry in zip(data,manifest):
        n=item['number'];path=ROOT/f'Exercise_{n:02d}/CN_Exercise_{n:02d}.pdf'
        assert path.stat().st_size<10_000_000
        assert hashlib.sha256(path.read_bytes()).hexdigest()==entry['sha256']
        reader=PdfReader(path)
        text='\n'.join(page.extract_text() for page in reader.pages)
        assert len(reader.pages)==entry['pages']
        for heading in ('Aim','Procedure / algorithm','Expected output - not an execution record','Result'):
            assert heading in text
        assert '\ufffd' not in text and '\x00' not in text
        cleaned=re.sub(r'CS23532 \| Experiment \d+\s*Page \d+','',text)
        for source in item['files']:
            source=ROOT/source
            if source.suffix=='.py':compile(source.read_text(),str(source),'exec')
            if source.suffix!='.csv':
                assert re.sub(r'\s+','',source.read_text(encoding='utf-8')) in re.sub(r'\s+','',cleaned),source
    for readme in ROOT.rglob('README.md'):
        for link in re.findall(r'\]\(([^)]+)\)',readme.read_text(encoding='utf-8')):
            if not link.startswith(('http://','https://','#')):assert (readme.parent/link).exists(),link
    print('PASS: exactly 15 exercise folders, 15 valid PDFs, complete source/config listings and links.')

if __name__=='__main__':main()
