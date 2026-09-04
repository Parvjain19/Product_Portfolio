import urllib.request
import json
import os
import shutil

print("Fetching JSON...")
req = urllib.request.Request("https://threeui.com/source-code/kage-landing-page.json")
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode('utf-8'))

for file in data['files']:
    path = file['path']
    code = file.get('code')
    if code is not None:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(code)
        print(f"Written {path}")

# Extract package
os.system("npm pack @designcodeio/threeui")
import glob
tarball = glob.glob("designcodeio-threeui-*.tgz")
if tarball:
    os.system(f"tar -xzf {tarball[0]}")
    if os.path.exists("package"):
        for root, dirs, files in os.walk("package/public/landing-pages/secret-pathways-assets"):
            for file in files:
                src = os.path.join(root, file)
                dst = src[len("package/"):]
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(src, dst)
                print(f"Copied {dst}")
        # Also copy threeui.css and fonts if needed. Wait, fonts are in secret-pathways-assets
