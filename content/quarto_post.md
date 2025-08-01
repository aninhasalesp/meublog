Title: Como criei meu blog 💁‍♀️💓
Date: 2025-07-28
Category: dev
Summary: Um passo a passo de como coloquei meu blog no ar usando o Pelican, GitHub Pages e um tema personalizado.

---

Ter um espaço só meu, fora de redes sociais, longe dos algoritmos, era um desejo antigo. Um cantinho para escrever sobre o que gosto, do meu jeito, sem pressa. 
E foi assim que nasceu o [meu blog](https://anapaula.org/). 💛

Neste post, compartilho como tirei a ideia do papel, desde a escolha da stack até o deploy.

## ✨ A stack que escolhi

Optei por usar o [Pelican](https://blog.getpelican.com/), um gerador de site estático escrito em Python. Ele me atraiu por vários motivos:

- É feito com Python 🐍
- Gera HTML puro (leve, rápido e fácil de hospedar)
- A estrutura é simples de customizar
- Permite escrever os posts em Markdown 📝
- A documentação... é meio confusa, mas fui até o fim mesmo assim 😅

---

## 🛠️ Passo a passo

### 1. Criar o ambiente e instalar o Pelican

Comecei criando um ambiente virtual com o [uv](https://github.com/astral-sh/uv):

```bash
uv venv .venv
source .venv/bin/activate
```

Depois instalei o Pelican com suporte a Markdown:

```bash
uv pip install "pelican[markdown]"
```

E então criei a estrutura base com:

```bash
pelican-quickstart
```
---

### 2. Organização do projeto

Segui as perguntas do setup e logo já tinha uma estrutura básica criada. A partir disso, organizei o repositório com o seguinte foco:

- `content/` → onde ficam os posts em Markdown
- `output/` → site gerado (HTML)
- `theme/` → arquivos do tema e personalizações

O repositório está disponível aqui: [github.com/aninhasalesp/meublog](https://github.com/aninhasalesp/meublog)

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

O conteúdo gerado vai pra pasta `output/`, que é servida diretamente no GitHub Pages.

---

### 9. Domínio personalizado 🌐

Registrei o domínio `anapaula.org` e fiz as seguintes configurações:

- Apontei o DNS para os servidores do GitHub Pages
- Criei um arquivo `CNAME` dentro da pasta `output/` com o conteúdo:

```
anapaula.org
```

- Ativei o HTTPS no painel do GitHub Pages

---

# Conclusão

O processo teve tropeços (a documentação do Pelican podia ser melhor 😅), mas valeu demais. Ter um espaço meu, com o meu nome e com a minha cara, era um desejo antigo que finalmente saiu do papel.

Se você também pensa em criar um blog, seja técnico ou pessoal, recomendo muito! E se eu puder ajudar de alguma forma, é só me chamar. 💛


O código-fonte do blog está no GitHub: [aninhasalesp/meublog](https://github.com/aninhasalesp/meublog) 🌱
