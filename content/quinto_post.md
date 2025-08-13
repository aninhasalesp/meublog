Title: Explorando o livro "Entendendo Algoritmos", cap.1
Date: 2025-08-12
Category: Entendendo algoritmos
Summary: Resumo, análises e exercícios práticos sobre o Capítulo 1 do livro "Entendendo Algoritmos", com sugestões de desafios no LeetCode e Exercism.

Início de uma série de estudos sobre o livro [Entendendo Algoritmos](https://www.kufunda.net/publicdocs/Entendendo%20Algoritmos%20Um%20guia%20ilustrado%20para%20programadores%20e%20outros%20curiosos%20(Aditya%20Y.%20Bhargava).pdf) de Aditya Y. Bhargava. Uma leitura surpreendentemente acessível e fundamental para entender e pensar de forma mais eficiente.

Esse livro foi indicado por uma amiga, [Ana Paula Mendes](https://github.com/anapaulamendes), e eu não imaginava o quanto iria gostar. Ele é simples de entender e mostra como conceitos de ciência da computação estão presentes no nosso dia a dia, mesmo para quem nunca programou.

<img src="{static}/images/livro1.jpg" alt="capa do livro" width="400"/>

---

## A busca binária em resumo

Imagine uma lista telefônica com **1 milhão de nomes**. Já pensou em ter que folheá-la inteira? Existe um jeito de encontrar qualquer nome com no **máximo 20 tentativas**, eliminando a cada passo metade das opções, isso é o que chamamos de **busca binária**.
Na busca binária, cada vez que dobramos o tamanho da lista, precisamos de apenas mais 1 passo.


**Observação importante**: numa lista telefônica física, a gente já sabe pular quase direto para a letra certa, o que lembra mais o funcionamento de um hashmap (ou dict no Python), que encontra um item em tempo constante. Mas no computador, quando temos apenas uma lista ordenada (como `[1, 3, 5, 7, 9, 11, 13]`), não existe esse “pulo mágico”, é aí que a busca binária pode ajudar, cortando a lista ao meio de forma sistemática até encontrar (ou concluir que o elemento não está lá).

Legal né? Isso é ciência da computação 💁‍♀️✨


### Exemplos básicos de busca binária:

Pense em um número entre 1 e 100. Dá para adivinhar em, no máximo, 7 tentativas:

Minha primeira pergunta: "É 50?"

- Se você disser "maior", eu sei que está entre 51 e 100
- Se disser "menor", está entre 1 e 49

Segunda pergunta: Digamos que seja maior que 50. "É 75?" (meio entre 51 e 100)

- Maior? Está entre 76 e 100
- Menor? Está entre 51 e 74

E assim por diante, sempre eliminando metade das possibilidades.

Seguindo a mesma lógica do exemplo anterior, vamos ver como fica com uma quantidade maior de números:


| Itens na lista | Busca linear (tentativas) | Busca binária (tentativas) |
| --- | --- | --- |
| 1.000 | até 1.000 | até 10 |
| 1.000.000 | até 1.000.000 | até 20 |

VINTE tentativas para encontrar algo entre 1 milhão de opções!!


---

**Agora que vimos como ela funciona, vale notar que a busca binária não está restrita a livros, ela aparece em várias situações do nosso dia a dia**


- **Sistemas de busca (Google, WhatsApp, Spotify)**: por trás, usam variações de busca binária em listas ordenadas ou índices.
- **Filtragem de dados**: encontrar rapidamente um registro específico em planilhas ou bases de dados grandes.
- **Depuração de código**: reduzir o espaço do problema pela metade a cada teste para achar onde o bug está.

> Observação: para que a busca binária funcione, os dados precisam estar ordenados.

---

## Vamos praticar rapidinho?

Aqui está uma lista ordenada de números: `[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]`

Tente encontrar o número 22 de duas formas:

1. **Busca linear:** Vá um a um desde o 2.  
2. **Busca binária:** Comece no meio, elimine metade a cada passo.

Compare quantos passos cada método precisou

---

## Curiosidades

- O git tem uma funcionalidade chamada [`git bisect`](https://git-scm.com/docs/git-bisect) que usa busca binária para ajudar desenvolvedores a encontrarem bug
- Se o item que estamos buscando for o primeiro item da lista, esse é o melhor caso na busca linear e o pior caso na busca binária
- A implementação do `sortedcontainers` usa busca binária (a partir do módulo bisect), [veja aqui](https://grantjenks.com/docs/sortedcontainers/_modules/sortedcontainers/sortedlist.html#SortedList)
 

---

## Exercícios recomendados 👩🏻‍💻💞
Para reforçar o aprendizado, aqui vão alguns desafios práticos:

**LeetCode**

- [Binary Search](https://leetcode.com/problems/binary-search/description/) — implementação direta.

- [Search Insert Position](https://leetcode.com/problems/search-insert-position/description/) — variação para encontrar onde inserir um número.

- [First Bad Version](https://leetcode.com/problems/first-bad-version/description/) — busca binária aplicada em API.

**Exercism**

- [Binary Search (Python Track)](https://exercism.org/tracks/python/exercises/binary-search) — implementação e testes.


**Dica: resolva primeiro o problema sem olhar a solução e depois compare com implementações otimizadas.**

E assim começa meu roadmap de estudo: cada capítulo do livro vem acompanhado de exercícios para fixar o conteúdo.