# Nach jeder Änderung an index.html oder den Sprachaufnahmen ausführen: python3 werkzeug/sw-erneuern.py
# (gibt dem Offline-Speicher eine neue Version, damit Handys die Änderung sicher bekommen)
import os,json,hashlib,re
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Repo-Ordner
src=open(R+'/sw.js').read()
h=hashlib.md5(open(R+'/index.html','rb').read()+''.join(sorted(os.listdir(R+'/a'))).encode()).hexdigest()[:8]
clips=['a/'+f for f in sorted(os.listdir(R+'/a'))]
src=re.sub(r"const VER='ws-[0-9a-f]+';",f"const VER='ws-{h}';",src)
src=re.sub(r"const CLIPS=\[.*?\];",lambda m:'const CLIPS='+json.dumps(clips)+';',src,flags=re.S)
open(R+'/sw.js','w').write(src);print('sw',h,len(clips))
