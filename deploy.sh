#!/bin/bash
set -e

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
OUTPUT_DIR="output"

echo "Branch atual: $CURRENT_BRANCH"

# Verifica alterações não commitadas
if ! git diff-index --quiet HEAD --; then
    echo "Você tem alterações não commitadas. Faça o commit antes de publicar."
    exit 1
fi

# Gera o site com as configurações de produção
echo "Gerando o site..."
uv run pelican content -s publishconf.py

# Troca para gh-pages
echo "Trocando para gh-pages..."
git checkout gh-pages

# Remove arquivos gerados antigos (preserva .git, CNAME, .nojekyll, .gitignore e output/)
echo "Limpando arquivos antigos..."
find . -maxdepth 1 \
    ! -name '.' \
    ! -name '.git' \
    ! -name 'CNAME' \
    ! -name '.nojekyll' \
    ! -name '.gitignore' \
    ! -name "$OUTPUT_DIR" \
    -exec rm -rf {} +

# Copia os novos arquivos gerados
echo "Copiando novos arquivos..."
cp -r "$OUTPUT_DIR"/. .

# Garante que CNAME, .nojekyll e .gitignore existem
echo "anapaula.org" > CNAME
touch .nojekyll
echo "output/" > .gitignore

# Commit e push
echo "Publicando..."
git add .
git commit -m "Publicar site - $(date '+%Y-%m-%d %H:%M')"
git push origin gh-pages

# Volta para a branch original
git checkout "$CURRENT_BRANCH"

echo ""
echo "Publicado com sucesso! O site estará disponível em https://anapaula.org em alguns instantes."
