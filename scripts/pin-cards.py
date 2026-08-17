#!/usr/bin/env python3
"""Fixa e confere os endereços das imagens do README.

Por que existe. O GitHub serve imagem de README pelo camo, um cache no servidor
dele que obedece o max-age de quem entrega. Isso vale ouro para quem visita e
veneno para um card de SEQUÊNCIA, que precisa dizer HOJE:

  - o streak-stats manda "cache-control: public, max-age=86400", e manda isso
    até no card de ERRO (a carinha triste), então uma falha de um minuto lá
    congela a tela por 24h;
  - o jsdelivr manda "s-maxage=43200" para ref de branch, ou seja, 12h.

Medido em 17/08/2026: o card na tela tinha sido buscado às 02:59 UTC e dizia
"18 de jun. - 16 de ago." num dia 17, com "age" de 12,6h e validade até o dia
seguinte. Nenhum ajuste de frequência da Action resolve isso, porque o problema
não é o arquivo estar velho, é o camo não ir buscar o novo.

O conserto é o endereço MUDAR quando o dado muda. Endereço novo o camo é
obrigado a buscar. Para os nossos cards a fixação é o commit
(`@<sha>/profile/langs.svg`), que o jsdelivr serve como "immutable"; para o
card de fora, que não tem commit, é um `&v=<sha>` que ele ignora e o camo não.

Dois modos, os dois usados pelo .github/workflows/cards.yml:
  --verificar        guarda: reprova raw, caminho relativo e pino faltando
  --fixar <sha>      troca todos os pinos por <sha>
"""

import argparse
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
README = RAIZ / "README.md"

# Os nossos cards, servidos pelo jsdelivr a partir de um commit deste repo.
NOSSO = re.compile(
    r"(https://cdn\.jsdelivr\.net/gh/kaminagakur4/kaminagakur4@)"
    r"([^/\s\"]+)"
    r"(/profile/[a-z-]+\.svg)"
)
# O card de sequência, o único que vem de serviço externo.
FORA = re.compile(r"(streak-stats\.demolab\.com/\?[^\"\s]*?)(&v=[0-9a-f]{7,40})?(?=\")")
PINO = re.compile(r"^[0-9a-f]{40}$")


def srcs(texto):
    """Só os src, nunca o arquivo todo: o próprio README explica em comentário
    por que o raw não serve, e varrer o texto reprovaria a explicação."""
    return re.findall(r'src="([^"]*)"', texto)


def verificar(texto):
    """Devolve a lista de motivos de reprova. Vazia significa aprovado."""
    ruins = []
    achados = srcs(texto)

    # Amostra vazia é reprova, não aprovação: guarda que não vê nada passa verde.
    if len(achados) < 17:
        ruins.append("poucos src encontrados (%d); a varredura não está vendo o README" % len(achados))

    pinos = set()
    for s in achados:
        if "raw.githubusercontent.com" in s:
            ruins.append("src aponta para raw.githubusercontent.com: %s" % s)
        if s.startswith("/") or s.startswith("./") or s.startswith("../"):
            ruins.append("src relativo; o GitHub o reescreve para o raw: %s" % s)

        m = NOSSO.search(s)
        if m:
            if not PINO.match(m.group(2)):
                ruins.append("card nosso sem pino de commit (achei %r): %s" % (m.group(2), s))
            else:
                pinos.add(m.group(2))

        if "streak-stats.demolab.com" in s:
            v = re.search(r"[?&]v=([0-9a-f]{7,40})", s)
            if not v:
                ruins.append("card de fora sem &v=<sha>; o camo guardaria 24h: %s" % s)
            else:
                pinos.add(v.group(1))

    # Pinos diferentes significam rewrite pela metade, com meia tela velha.
    if len(pinos) > 1:
        ruins.append("pinos divergentes no README: %s" % ", ".join(sorted(pinos)))
    if not pinos:
        ruins.append("nenhum card fixado; nada obrigaria o camo a buscar de novo")
    return ruins


def fixar(texto, sha):
    if not PINO.match(sha):
        raise SystemExit("pino tem de ser um sha de 40 hex, recebi %r" % sha)
    texto = NOSSO.sub(lambda m: m.group(1) + sha + m.group(3), texto)
    texto = FORA.sub(lambda m: m.group(1) + "&v=" + sha, texto)
    return texto


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--verificar", action="store_true")
    p.add_argument("--fixar", metavar="SHA")
    a = p.parse_args()

    texto = README.read_text()

    if a.fixar:
        novo = fixar(texto, a.fixar)
        ruins = verificar(novo)
        if ruins:
            # Nunca gravar um README que a própria guarda reprova.
            for r in ruins:
                print("ERRO apos fixar: %s" % r, file=sys.stderr)
            return 1
        if novo == texto:
            print("pino ja era %s, nada a escrever" % a.fixar[:8])
            return 0
        README.write_text(novo)
        print("pino trocado para %s" % a.fixar[:8])
        return 0

    if a.verificar:
        ruins = verificar(texto)
        for r in ruins:
            print("::error::%s" % r)
        if ruins:
            return 1
        print("aprovado: %d src, nenhum raw, nenhum relativo, todos fixados" % len(srcs(texto)))
        return 0

    p.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
