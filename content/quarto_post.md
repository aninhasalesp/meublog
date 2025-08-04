Title: Como criei meu blog 💁‍♀️✨
Date: 2025-07-28
Category: dev
Summary: Um passo a passo de como coloquei meu blog no ar usando o Pelican, GitHub Pages e um tema personalizado.

---

Ter um espaço só meu, fora de redes sociais, longe dos algoritmos, era um desejo antigo. Um cantinho para escrever sobre o que gosto, do meu jeito, sem pressa. 
E foi assim que nasceu o [meu blog](https://anapaula.org/). 💛

Neste post, compartilho como tirei a ideia do papel, desde a escolha da stack até o deploy.

## A stack que escolhi

Optei por usar o [Pelican](https://blog.getpelican.com/), um gerador de site estático escrito em Python. Ele me atraiu por vários motivos:

- É feito com Python 🐍
- Gera HTML puro (leve, rápido e fácil de hospedar)
    - Ou seja: não tem nada sendo processado dinamicamente no servidor; Isso deixa o site mais rápido, seguro e barato/fácil de hospedar (como no GitHub Pages, que só serve arquivos estáticos).
- A estrutura é simples de customizar
- Permite escrever os posts em Markdown 📝
- A documentação... é meio confusa, mas fui até o fim mesmo assim 😅


Além do Pelican, usei o [uv](https://github.com/astral-sh/uv) como gerenciador de pacotes e ambientes virtuais, ele é rápido e prático, e tem substituído o uso manual do venv e do pip.

---

## 🛠️ Passo a passo

### 1. Criar o ambiente e instalar o Pelican

Usei o uv para criar meu ambiente virtual com:

```bash
uv venv
```

Depois disso, ativei o ambiente manualmente com:

```bash
source .venv/bin/activate
```
O `uv venv` já cria o ambiente e ativa os pacotes com isolamento, mas, por hábito (e um pouco de força do costume), usei `source .venv/bin/activate` logo depois. O uv também poderia dispensar esse passo.

Esse passo não é automático, o uv venv cria o ambiente, mas não o ativa. Eu fiz isso por hábito, já que é o modo tradicional que muitos de nós usamos com venv.

No entanto, o uv também oferece uma forma mais moderna (e prática!) de lidar com ambientes virtuais: você pode pular o uv venv e o source, e simplesmente deixar que ele gerencie tudo pra você:

```bash
uv add pelican[markdown] # declara o `pelican` como uma dependência do projeto

uv run pelican-quickstart # executa o comando `pelican-quickstart` dentro do ambiente virtual gerenciado automaticamente pelo `uv`
```

Assim, o uv cria o ambiente e executa os comandos dentro dele automaticamente, sem precisar ativar nada "na mão

Só uma observação: se você preferir usar a forma `uv add ...` e `uv run ...`, o arquivo Makefile precisaria ser alterado, substituindo a linha `PELICAN=pelican` por `PELICAN=uv run pelican` - ou todas as referências a `make <rule>` precisariam virar `PELICAN="uv run pelican" make <rule>`.

---

### 2. Organização do projeto

Segui as perguntas do setup e logo já tinha uma estrutura básica criada. A partir disso, organizei o repositório com o seguinte foco:

- `content/` → onde ficam os posts em Markdown
- `output/` → site gerado (HTML)
- `theme/` → arquivos do tema e personalizações

O repositório está disponível aqui: [github.com/aninhasalesp/meublog](https://github.com/aninhasalesp/meublog)

A pasta `pelican-themes/` foi criada por mim manualmente pra colocar o tema clonado e fazer as modificações.

---

### 3. Escolhendo e personalizando o tema 🎨 

Usei o tema `notmyidea-cms`, que vem com o Pelican, e fui personalizando aos poucos.

No `pelicanconf.py`:

```python
THEME = "pelican-themes/notmyidea-cms"
```

Fiz as seguintes mudanças:

- Rodapé com meu nome e link pro GitHub ❤️
- Comentários com [Utterances](https://utteranc.es)
- Botões de compartilhamento (LinkedIn, WhatsApp e Telegram)
- Ajustes no CSS para espaçamentos, layout e cores

---

### 4. Comentários com Utterances 💬

Usei o [Utterances](https://utteranc.es/) para habilitar comentários nos posts. É leve, usa issues do GitHub, é simples e eficiente:

```html
<div id="comments">
  <script src="https://utteranc.es/client.js"
    repo="aninhasalesp/meublog"
    issue-term="pathname"
    theme="github-light"
    crossorigin="anonymous"
    async>
  </script>
</div>
```
---

### 5. Escrevendo os posts ✍️

Os posts ficam em `content/` e são escritos assim:

```markdown
Title: Primeiro post
Date: 2025-07-20
Category: pessoal
Summary: Um breve texto pra dar boas-vindas ao blog.

---

Esse é o primeiro post do blog! 🎉
```

---

### 6. Customizações no tema

Editei os arquivos dentro de `pelican-themes/notmyidea-cms/` e deixei o blog com mais identidade.

No CSS:

- Ajustei padding e margin
- Alinhei melhor os elementos
- Adicionei ícones e links visuais

No HTML (como o `base.html`):

- Adicionei o rodapé
- Posicionei os botões de compartilhamento

💡 *Fazer as edições direto no tema funcionou bem pra mim, mesmo que não seja o ideal a longo prazo.*

---

### 7. Gerando os arquivos estáticos

Para compilar o blog e gerar os arquivos HTML:

```bash
make html
```

Durante o desenvolvimento, usei o servidor local pra visualizar as mudanças:

```bash
pelican --listen
```

---

### 8. Deploy no GitHub Pages 🚀

Usei GitHub Pages pra hospedar o blog. O processo foi:

1. Gerei os arquivos com `pelican content` ou `make html`
2. Subi a pasta `output/` para o branch `gh-pages`
3. Configurei o domínio personalizado no GitHub e apontei o DNS para os servidores do GitHub


O `Makefile` ajuda bastante, publiquei com:

```bash
make github
```
Esse comando está no meu Makefile e automatiza a geração e envio do conteúdo. Se quiser ver, ele basicamente faz:

```bash
cd output
git checkout -b gh-pages
git add .
git commit -m "Deploy"
git push -f origin gh-pages
```

1. No GitHub, fui na aba Settings > Pages e configurei pra servir o site a partir do branch gh-pages, pasta raiz (/).
2. Adicionei um arquivo CNAME com meu domínio personalizado (anapaula.org)
3. Apontei os DNSs da minha hospedagem pro GitHub Pages
4. Ativei o HTTPS no painel

Se você quiser automatizar esse deploy com GitHub Actions, também dá. Mas como é um blog pessoal que não atualizo todos os dias, preferi o método manual.

---

### 9. Domínio personalizado 🌐

Registrei o domínio `anapaula.org` e configurei para ser usado no meu blog hospedado via GitHub Pages.

O que eu fiz:
No painel da empresa onde registrei o domínio, adicionei os seguintes registros DNS:

Tipo A (IPv4): apontando para os IPs do GitHub Pages:
```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```
- CNAME (se quiser usar subdomínio): apontando para suaconta.github.io

Dentro da pasta `output/` (que é a que vai para o GitHub Pages no branch gh-pages), criei um arquivo CNAME com o conteúdo:

```bash
anapaula.org
```

Isso é necessário para que o GitHub saiba qual domínio deve ser vinculado ao seu site. Esse arquivo é incluído automaticamente no deploy quando rodo `make github`.

No repositório no GitHub, fui em Settings > Pages e:

  - Marquei a opção "Use a custom domain" e coloquei anapaula.org
  - Ativei o HTTPS (pra garantir navegação segura)

Segui a documentação oficial do GitHub Pages para configurar tudo isso:
👉 [documentação github-pages](https://docs.github.com/pt/pages/configuring-a-custom-domain-for-your-github-pages-site)

---

# Conclusão

O processo teve tropeços (a documentação do Pelican podia ser melhor 😅), mas valeu demais. Ter um espaço meu, com o meu nome e com a minha cara, era um desejo antigo que finalmente saiu do papel.

Se você também pensa em criar um blog, seja técnico ou pessoal, recomendo muito! E se eu puder ajudar de alguma forma, é só me chamar. 💛


O código-fonte do blog está no GitHub: [aninhasalesp/meublog](https://github.com/aninhasalesp/meublog) 🌱
