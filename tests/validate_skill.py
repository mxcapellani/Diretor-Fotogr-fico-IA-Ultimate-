from pathlib import Path
import re,json,sys,yaml
B=Path('.agents/skills/diretor-fotografico-ia-ultimate')
class Unique(yaml.SafeLoader):pass
def unique(loader,node,deep=False):
 d={}
 for k,v in node.value:
  key=loader.construct_object(k,deep=deep)
  if key in d:raise ValueError('duplicate YAML key')
  d[key]=loader.construct_object(v,deep=deep)
 return d
Unique.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,unique)
def validate(root):
 root=Path(root);e=[]
 for p in ('README.md','LICENSE','NOTICE.md','docs/coverage.json','docs/source-manifest.json','tests/acceptance-tests.md',str(B/'SKILL.md')):
  if not (root/p).is_file() or not (root/p).read_text().strip():e.append('missing '+p)
 if e:return e
 text=(root/B/'SKILL.md').read_text()
 try:
  assert text.startswith('---\n');d=yaml.load(text.split('---',2)[1],Loader=Unique);assert set(d)=={'name','description'};assert d['name']=='diretor-fotografico-ia-ultimate' and len(d['description'].strip())>60
 except Exception:e.append('invalid YAML')
 for token in ('uma etapa por vez','Não repetir pergunta já respondida','Temperatura da luz','medium clouse-up','pode escolher por mim','## Construção e entrega'):
  if token not in text:e.append('missing contract '+token)
 try:
  rows=json.loads((root/'docs/coverage.json').read_text())
  for source,count in [('ebook',56),('guide',32)]:
   assert sorted(x['page'] for x in rows if x['source']==source)==list(range(1,count+1))
   t=(root/B/f'references/{source}-source.md').read_text()
   assert len(re.findall(r'^## Página PDF \d+$',t,re.M))==count
  for x in rows:
   for p in [x['text_reference'],x['visual_reference']]+x['topic_references']:assert (root/p).exists()
  cat=json.loads((root/B/'assets/technique-catalog.json').read_text());assert len(cat)==28
  for x in cat:assert x['term'] in text and x['example_en'] in text and len(x['definition'])>30
 except Exception:e.append('coverage or catalog mismatch')
 for p in root.rglob('*.md'):
  for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
   if '://' in link or link.startswith('#'):continue
   target=(p.parent/link.split('#')[0]).resolve()
   if not target.is_relative_to(root.resolve()) or not target.exists():e.append('bad link '+link)
 for i in range(1,25):
  if f'## T{i:02d} —' not in (root/'tests/acceptance-tests.md').read_text():e.append('missing case')
 return e
if __name__=='__main__':
 e=validate(Path(__file__).resolve().parents[1]);print('\n'.join(e) if e else 'PASS: YAML, links, 28 techniques and 88 page coverage records');sys.exit(bool(e))
