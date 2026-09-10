"""
build.py — gera o site a partir dos arquivos em content/licoes/

Para adicionar uma lição nova: crie um arquivo .md em content/licoes/
com o front matter (título, nível, tipo, data, etc.) e rode:

    python3 build.py

A home e a página da lição são geradas sozinhas — nada de editar HTML.
"""
import re
import shutil
from pathlib import Path
from datetime import date

import yaml
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).parent
CONTENT_DIR = ROOT / "content" / "licoes"
TEMPLATES_DIR = ROOT / "templates"
OUTPUT_DIR = ROOT / "output"


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = (text.replace("ã", "a").replace("á", "a").replace("â", "a")
                .replace("é", "e").replace("ê", "e")
                .replace("í", "i")
                .replace("ó", "o").replace("ô", "o")
                .replace("ú", "u").replace("ç", "c"))
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text


def load_licoes():
    licoes = []
    for path in CONTENT_DIR.glob("*.md"):
        raw = path.read_text(encoding="utf-8")
        front_matter, _, body = raw.lstrip("-\n").partition("---")
        meta = yaml.safe_load(front_matter)
        meta["body"] = body.strip()
        if isinstance(meta["date"], str):
            meta["date"] = date.fromisoformat(meta["date"])
        licoes.append(meta)
    # mais recente primeiro — é isso que faz a home ficar sempre atualizada
    licoes.sort(key=lambda x: x["date"], reverse=True)
    return licoes


def main():
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)
    shutil.copytree(ROOT / "static", OUTPUT_DIR / "static")

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    env.filters["slugify"] = slugify

    licoes = load_licoes()

    # home
    index_tpl = env.get_template("index.html")
    (OUTPUT_DIR / "index.html").write_text(
        index_tpl.render(licoes=licoes), encoding="utf-8"
    )

    # uma página por lição, dentro da pasta do seu tipo (nivel/tipo -> pasta)
    licao_tpl = env.get_template("licao.html")
    for licao in licoes:
        folder = OUTPUT_DIR / slugify(licao["type"])
        folder.mkdir(exist_ok=True)
        (folder / f"{licao['slug']}.html").write_text(
            licao_tpl.render(licao=licao), encoding="utf-8"
        )

    print(f"OK: {len(licoes)} lições geradas em {OUTPUT_DIR}/")
    for l in licoes:
        print(f"  - {l['date']}  {l['title']}  -> {slugify(l['type'])}/{l['slug']}.html")


if __name__ == "__main__":
    main()
