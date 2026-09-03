## kami

<!-- Cada imagem vai dentro de um <a>: imagem solta o GitHub embrulha num link
     target="_blank" para o próprio arquivo, e o clique abre o SVG numa aba nova.

     Os ícones vêm do jsdelivr, NUNCA de raw.githubusercontent.com. O GitHub não
     proxia pelo camo o que já é de domínio dele, então o navegador de quem visita
     busca o raw direto, e o raw responde 429 por IP: em 17/08/2026 os quinze
     ícones e o card de linguagens caíram todos ao mesmo tempo, virando alt text,
     enquanto shields e streak (camo, cache no servidor do GitHub) seguiam de pé.
     Passando pelo jsdelivr a imagem entra no camo e o visitante nunca toca o raw.
     A tag é fixa de propósito: @master invalidaria o cache a cada commit deles. -->
<div>
  <a href="#"><img align="center" alt="JavaScript" title="JavaScript" height="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/javascript/javascript-original.svg"></a>
  <a href="#"><img align="center" alt="TypeScript" title="TypeScript" height="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/typescript/typescript-original.svg"></a>
  <a href="#"><img align="center" alt="React" title="React" height="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/react/react-original.svg"></a>
  <a href="#"><img align="center" alt="Node.js" title="Node.js" height="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/nodejs/nodejs-original.svg"></a>
  <a href="#"><img align="center" alt="HTML5" title="HTML5" height="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/html5/html5-original.svg"></a>
  <a href="#"><img align="center" alt="CSS3" title="CSS3" height="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/css3/css3-original.svg"></a>
  <a href="#"><img align="center" alt="Tailwind CSS" title="Tailwind CSS" height="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/tailwindcss/tailwindcss-original.svg"></a>
  <a href="#"><img align="center" alt="Python" title="Python" height="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/python/python-original.svg"></a>
</div>

<div>
  <a href="#"><img align="center" alt="PostgreSQL" title="PostgreSQL" height="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/postgresql/postgresql-original.svg"></a>
  <a href="#"><img align="center" alt="SQLite" title="SQLite" height="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/sqlite/sqlite-original.svg"></a>
  <a href="#"><img align="center" alt="Supabase" title="Supabase" height="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/supabase/supabase-original.svg"></a>
  <a href="#"><img align="center" alt="Swift" title="Swift" height="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/swift/swift-original.svg"></a>
  <a href="#"><img align="center" alt="Docker" title="Docker" height="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/docker/docker-original.svg"></a>
  <a href="#"><img align="center" alt="Three.js" title="Three.js" height="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/threejs/threejs-original.svg"></a>
  <a href="#"><img align="center" alt="Git" title="Git" height="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/git/git-original.svg"></a>
</div>

##

<div>
  <!-- O logo do envelope vai embutido como data URI: o shields só tem ícones de
       marca, e o e-mail é de domínio próprio, então Gmail ou Mail.ru seria falso. -->
  <a href="mailto:kami@moriwa.ai"><img src="https://img.shields.io/badge/kami@moriwa.ai-EA4335?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0yIDVhMiAyIDAgMCAxIDItMmgxNmEyIDIgMCAwIDEgMiAydjE0YTIgMiAwIDAgMS0yIDJINGEyIDIgMCAwIDEtMi0yVjV6bTIuNC42TDEyIDExbDcuNi01LjRINC40eiIvPjwvc3ZnPg%3D%3D" alt="Email: kami@moriwa.ai"></a>
  <a href="https://www.tiktok.com/@kaminagakura"><img src="https://img.shields.io/badge/TikTok-FE2C55?style=for-the-badge&logo=tiktok&logoColor=white" alt="TikTok"></a>
  <!-- A rota /users/ do Discord espera o ID numérico (snowflake); com o apelido ela
       pode não achar o perfil. Se um dia não abrir, troque "swishi" pelo ID.
       Não dá para conferir por HTTP: o Discord devolve 200 em qualquer caminho,
       porque quem resolve o perfil é o app depois de carregar. -->
  <a href="https://discord.com/users/swishi"><img src="https://img.shields.io/badge/swishi-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord: swishi"></a>
</div>

##

<!-- Gerados por .github/workflows/cards.yml e versionados em profile/, mas servidos
     pelo jsdelivr, não por caminho relativo: "./profile/langs.svg" o GitHub reescreve
     para raw.githubusercontent.com, o mesmo endereço que quebrou os ícones acima.

     O @<sha> NÃO se escreve à mão: quem o troca é o
     scripts/pin-cards.py, chamado pela Action, e o cabeçalho dele explica por quê.
     Em uma frase: o camo do GitHub obedece o max-age de quem entrega (12h no
     jsdelivr), então o único jeito de a tela mostrar HOJE é o ENDEREÇO mudar
     quando o dado muda. Trocar isso por @main devolve o card de ontem.

     Os TRÊS cards são arquivo nosso, e isso é a regra, não uma coincidência. O
     de sequência vinha de um serviço externo até 18/08/2026 e quebrou duas
     vezes em dois dias: o camo desiste de buscar em ~4s, e numa URL nova aquele
     serviço levava 14s, 30s ou 4,4s. Imagem calculada por requisição não tem
     como ser fresca e confiável ao mesmo tempo aqui. Com arquivo, o pior caso
     vira dado velho na tela, nunca buraco. A guarda recusa host novo.
     Para voltar a exibir as estatísticas, que seguem sendo geradas, basta colar:
     <a href="#"><img src="https://cdn.jsdelivr.net/gh/kaminagakur4/kaminagakur4@393686fd96c212f0897a4811192820008b617c85/profile/stats.svg" alt="Estatísticas do GitHub" height="190"></a>
     A sequência sai do scripts/gerar-sequencia.py, que lê a API do GitHub. -->
<a href="#"><img src="https://cdn.jsdelivr.net/gh/kaminagakur4/kaminagakur4@393686fd96c212f0897a4811192820008b617c85/profile/langs.svg" alt="Linguagens mais usadas" height="190"></a>
<a href="#"><img src="https://cdn.jsdelivr.net/gh/kaminagakur4/kaminagakur4@393686fd96c212f0897a4811192820008b617c85/profile/sequencia.svg" alt="Sequência de contribuições" height="190"></a>
