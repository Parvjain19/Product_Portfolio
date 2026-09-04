import urllib.request
import json
import os
import hashlib
import re

def verify_hash(filepath, expected_hash):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest() == expected_hash

print("Fetching JSON source...")
req = urllib.request.Request("https://threeui.com/source-code/kage-landing-page.json")
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode('utf-8'))

for file in data['files']:
    path = file['path']
    code = file.get('code')
    if code is not None:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        # Edit kage.html to include Parv Jain
        if path.endswith("kage.html"):
            code = code.replace("Kage — Where stillness reveals the unseen", "PARV JAIN - Product Management Portfolio")
            code = code.replace("KAGE", "PARV JAIN")
            code = code.replace("HIDDEN REALMS OF KYOTO", "PRODUCT MANAGEMENT PORTFOLIO")
            code = code.replace("Chapter 00 — The Hidden Gate", "PARV JAIN - College")
            code = code.replace("Kage &mdash; Where stillness reveals the unseen", "PARV JAIN - Product Management Portfolio")
            code = code.replace("Chapter 00 &mdash; The Hidden Gate", "PARV JAIN - College")
        
        with open(path, "w") as f:
            f.write(code)
        print(f"Written source file {path}")

# Binary assets
binary_assets = [
    ("public/landing-pages/secret-pathways-assets/generated/kage-sanmon-preview.webp", "23937f8c8350c55730c3bd17066a250548b2d29aad0e6ffb96218c1354b6db43"),
    ("public/landing-pages/secret-pathways-assets/generated/kage-approach.webp", "39ff338936097e1bde0c4eadcf09805b9890862703186e67314942de7e0bc36c"),
    ("public/landing-pages/secret-pathways-assets/generated/kage-lantern-court.webp", "c0a6ff7da1cd6909d66e2f3f690b0d524a693e01d2222ab846d0074a90f47471"),
    ("public/landing-pages/secret-pathways-assets/generated/kage-moonwater.webp", "b8c8060c51c87a103bae619b3a4cc8b8b80632649d83f1f2c2299051e7f9b400"),
    ("public/landing-pages/secret-pathways-assets/foreground/png/temple-wall.webp", "41c00f017e4ecf2147ee468d74da955bb4e2dad773f75a575022842eaf7609ce"),
    ("public/landing-pages/secret-pathways-assets/foreground/png/pine-tree.webp", "79b233716d067bbc64c1507f79e4a30ba5f445995158c78562cc5b81f607ede7"),
    ("public/landing-pages/secret-pathways-assets/foreground/png/tall-grass.webp", "8db0b5fbd160a7225391a6283a99681e346e205f24191031657285ef85ef12d2"),
    ("public/landing-pages/secret-pathways-assets/foreground/png/sakura-branch.webp", "48564194d40496090dbf3bba2a68785cf91fafb655dc8d43ac16f6678aff196d"),
    ("public/landing-pages/secret-pathways-assets/foreground/png/maple-leaves.webp", "35a90fec62c1a6bbfbbe73cd5d7b1acb889e80546d404182ef9a45fe417b531f"),
    ("public/landing-pages/secret-pathways-assets/foreground/png/stone-lantern.webp", "d5f3c881bc9d92b72eaaff2b709614d66e21a19e14025d2b9b16a15ab52df3bc"),
    ("public/landing-pages/secret-pathways-assets/foreground/png/garden-bush.webp", "707e2516ebc0108041fe0ddc26d8bff0a69dc9700641f837765018b64e9ff15e"),
    ("public/landing-pages/secret-pathways-assets/foreground/png/basalt-stones.webp", "150f1c87e181d651c318168c271bb65c9c8abac6dea6f2421fdd081c5b740471"),
    ("public/landing-pages/secret-pathways-assets/foreground/png/hill.webp", "ffba816244bcba98e4e33c6ee56165edfe4048db4af122ef3f5822180a85edbc"),
    ("public/landing-pages/secret-pathways-assets/foreground/png/shrine-ruins.webp", "77006e58f2066e6fa9bfc504df396db49b1c7977858fa52d34dd2dad5feced77"),
]

base_url = "https://threeui.com/"

print("Downloading binary assets...")
for path, expected_hash in binary_assets:
    url = base_url + path.replace("public/", "")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    urllib.request.urlretrieve(url, path)
    if verify_hash(path, expected_hash):
        print(f"Downloaded and verified {path}")
    else:
        print(f"Hash mismatch for {path}")
