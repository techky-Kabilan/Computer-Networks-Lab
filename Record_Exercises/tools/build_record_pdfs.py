"""Render full experiment documents as ordinary, embedded-font PDFs."""
import csv
import hashlib
import json
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted, Image, Table, TableStyle
from pypdf import PdfReader, PdfWriter

ROOT=Path(__file__).resolve().parents[1]
WIDTH=A4[0]-88

def font_path(options):
    for path in options:
        if Path(path).exists():return path
    raise FileNotFoundError('Install DejaVu fonts or supply Arial/Consolas to embed fonts')

def register_fonts():
    regular=font_path(['C:/Windows/Fonts/arial.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'])
    bold=font_path(['C:/Windows/Fonts/arialbd.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'])
    mono=font_path(['C:/Windows/Fonts/consola.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'])
    for name,path in [('Body',regular),('BodyBold',bold),('Mono',mono)]:
        pdfmetrics.registerFont(TTFont(name,path))
    pdfmetrics.registerFontFamily('Body',normal='Body',bold='BodyBold')

styles={
 'title':ParagraphStyle('title',fontName='BodyBold',fontSize=19,leading=24,spaceAfter=14),
 'body':ParagraphStyle('body',fontName='Body',fontSize=10.8,leading=15,spaceAfter=8),
 'heading':ParagraphStyle('heading',fontName='BodyBold',fontSize=12,leading=16,spaceBefore=13,spaceAfter=7,keepWithNext=True),
 'code':ParagraphStyle('code',fontName='Mono',fontSize=9.2,leading=11.8,spaceAfter=9),
 'cell':ParagraphStyle('cell',fontName='Body',fontSize=9.5,leading=13),
}
def para(text,kind='body'):return Paragraph(escape(text),styles[kind])
def source_block(text):
    # Continuation indentation is visual wrapping only; source files are exact.
    limit=int(WIDTH/pdfmetrics.stringWidth('M','Mono',9.2))
    lines=[]
    for line in text.expandtabs(4).splitlines():
        if len(line)<=limit:lines.append(line)
        else:
            indent=len(line)-len(line.lstrip())
            lines.extend(textwrap.wrap(line,width=limit,subsequent_indent=' '*(min(indent,20)+4),
                                       replace_whitespace=False,drop_whitespace=False,
                                       break_long_words=True,break_on_hyphens=False))
    return Preformatted('\n'.join(lines),styles['code'])

def csv_table(path):
    rows=list(csv.reader(path.read_text(encoding='utf-8').splitlines()))
    cells=[[para(cell,'cell') for cell in row] for row in rows]
    widths=[WIDTH/len(rows[0])]*len(rows[0])
    table=Table(cells,colWidths=widths,repeatRows=1,hAlign='LEFT')
    table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eaf0f4')),
       ('GRID',(0,0),(-1,-1),.4,colors.HexColor('#9cabb5')),('VALIGN',(0,0),(-1,-1),'TOP'),
       ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    return table

def footer(number):
    def draw(c,doc):
        c.setFont('Body',8.5);c.setFillColor(colors.HexColor('#455665'))
        c.drawString(44,25,f'CS23532 | Experiment {number:02d}')
        c.drawRightString(A4[0]-44,25,f'Page {doc.page}')
        c.setStrokeColor(colors.HexColor('#c6cfd6'));c.setLineWidth(.5)
        c.line(44,39,A4[0]-44,39)
    return draw

def build():
    register_fonts()
    data=json.loads((ROOT/'tools/experiment_data.json').read_text())
    output=ROOT
    manifest=[]
    for item in data:
        n=item['number'];directory=ROOT/f'Exercise_{n:02d}'
        story=[para(f'Experiment {n:02d}','heading'),para(item['title'],'title'),
               para('Aim','heading'),para(item['aim']),
               para('Requirements','heading'),para(item['requirements']),
               para('Procedure / algorithm','heading')]
        story += [para(f'{i}. {step}') for i,step in enumerate(item['procedure'],1)]
        for file in item['files']:
            path=ROOT/file
            story += [para('Complete source / configuration: '+path.name,'heading')]
            story += [csv_table(path) if path.suffix=='.csv' else source_block(path.read_text(encoding='utf-8'))]
        for file in item['diagrams']:
            story += [para('Diagram: '+Path(file).stem.replace('_',' '),'heading'),
                      Image(str(ROOT/file),width=WIDTH,height=WIDTH*610/1100)]
        if item.get('run'):
            story += [para('Run','heading'),para('From the repository root unless a cd command is shown.'),source_block('\n'.join(item['run']))]
        actual=directory/'outputs/actual.txt'
        story += [para('Actual output / verification','heading')]
        if actual.exists():story += [source_block(actual.read_text(encoding='utf-8'))]
        else:story += [para('Not executed in the required lab/tool environment. No actual operational output is claimed.')]
        summary=directory/'outputs/protocol_summary.txt'
        if summary.exists():story += [para('Actual TShark protocol summary','heading'),source_block(summary.read_text(encoding='utf-8'))]
        fixture=directory/'outputs/fixture_check.txt'
        if fixture.exists():story += [para('Actual synthetic-fixture check - not Webalizer output','heading'),source_block(fixture.read_text())]
        story += [para('Expected output - not an execution record','heading'),para(item['expected']),
                  para('Observations','heading'),para(item['observations']),
                  para('Result','heading'),para(item['result'])]
        path=ROOT/f'Exercise_{n:02d}/CN_Exercise_{n:02d}.pdf'
        doc=SimpleDocTemplate(str(path),pagesize=A4,rightMargin=44,leftMargin=44,
                             topMargin=44,bottomMargin=55,title=item['title'],author='CS23532 Computer Networks Laboratory')
        doc.build(story,onFirstPage=footer(n),onLaterPages=footer(n))
        reader=PdfReader(path)
        manifest.append({'experiment':n,'file':path.relative_to(ROOT).as_posix(),
                         'pages':len(reader.pages),'bytes':path.stat().st_size,
                         'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    (ROOT/'record_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print('Rebuilt exactly 15 exercise PDFs:',sum(e['pages'] for e in manifest),'pages')

if __name__=='__main__':build()
