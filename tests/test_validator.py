import unittest,tempfile,shutil,json
from pathlib import Path
from validate_skill import validate,B
ROOT=Path(__file__).resolve().parents[1]
class Tests(unittest.TestCase):
 def setUp(self):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);self.r=Path(t.name)/'repo';shutil.copytree(ROOT,self.r)
 def change(self,p,a,b):
  q=self.r/p;q.write_text(q.read_text().replace(a,b,1))
 def test_valid(self):self.assertEqual(validate(self.r),[])
 def test_wrong_name(self):
  self.change(B/'SKILL.md','name: diretor-fotografico-ia-ultimate','name: wrong');self.assertTrue(validate(self.r))
 def test_duplicate_yaml(self):
  self.change(B/'SKILL.md','name: diretor-fotografico-ia-ultimate','name: diretor-fotografico-ia-ultimate\nname: duplicate');self.assertTrue(validate(self.r))
 def test_missing_reference(self):
  (self.r/B/'references/framing.md').unlink();self.assertTrue(validate(self.r))
 def test_missing_coverage_page(self):
  p=self.r/'docs/coverage.json';d=json.loads(p.read_text());d.pop();p.write_text(json.dumps(d));self.assertTrue(validate(self.r))
 def test_missing_source_page(self):
  self.change(B/'references/ebook-source.md','## Página PDF 50','## Removed');self.assertTrue(validate(self.r))
 def test_missing_technique(self):
  p=self.r/B/'assets/technique-catalog.json';d=json.loads(p.read_text());d.pop();p.write_text(json.dumps(d));self.assertTrue(validate(self.r))
 def test_missing_guided_contract(self):
  self.change(B/'SKILL.md','uma etapa por vez','all at once');self.assertTrue(validate(self.r))
 def test_missing_case(self):
  self.change('tests/acceptance-tests.md','## T24 —','## Removed —');self.assertTrue(validate(self.r))
 def test_missing_notice(self):
  (self.r/'NOTICE.md').unlink();self.assertTrue(validate(self.r))
if __name__=='__main__':unittest.main()
