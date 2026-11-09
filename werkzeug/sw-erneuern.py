# Nach jeder Änderung an index.html oder den Sprachaufnahmen ausführen: python3 werkzeug/sw-erneuern.py
# (gibt dem Offline-Speicher eine neue Version, damit Handys die Änderung sicher bekommen)
import os,json,hashlib,re
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Repo-Ordner
src=open(R+'/sw.js').read()
hh=hashlib.md5(open(R+'/index.html','rb').read())
for f in sorted(os.listdir(R+'/n')): hh.update(f.encode()); hh.update(open(R+'/n/'+f,'rb').read())  # auch neu aufgenommene Clips mit gleichem Namen zählen
h=hh.hexdigest()[:8]
clips=['n/'+f for f in sorted(os.listdir(R+'/n'))]
src=re.sub(r"const VER='ws-[0-9a-f]+';",f"const VER='ws-{h}';",src)
src=re.sub(r"const CLIPS=\[.*?\];",lambda m:'const CLIPS='+json.dumps(clips)+';',src,flags=re.S)
open(R+'/sw.js','w').write(src);print('sw',h,len(clips))
