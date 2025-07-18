# 📝 Blog Pessoal da Ana Paula

Este é o repositório do meu blog pessoal, onde compartilho ideias, textos, projetos e aprendizados sobre tecnologia, escrita e o que mais me atravessar.

O blog é construído com [Pelican](https://blog.getpelican.com/), um gerador de site estático escrito em Python.

---

## ✨ Funcionalidades

- 📚 Publicação de artigos em formato estático  
- 🧩 Organização de conteúdos por categorias e tags  
- 📅 URLs baseadas na data dos posts  
- 🎨 Layout simples, limpo e fácil de manter  

---

## 🚀 Como rodar localmente

Se você quiser rodar o blog localmente na sua máquina, siga estes passos:

```bash
# Clone o repositório
git clone https://github.com/aninhasalesp/meublog.git
cd meublog

# Crie um ambiente virtual
python3 -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

# Instale as dependências
pip install -r requirements.txt

# Gere os arquivos estáticos
pelican content

# Rode o servidor local
pelican --listen
