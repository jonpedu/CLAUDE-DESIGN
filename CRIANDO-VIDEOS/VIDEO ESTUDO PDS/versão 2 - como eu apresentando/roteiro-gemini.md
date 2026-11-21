# Versão 2: roteiro para gerar no Gemini (João apresentando os slides 6 e 7)

Gere **dois áudios**, um por slide, e salve nesta pasta como `slide6.wav` e `slide7.wav`.
A fala está escrita como se lê em voz alta (a matemática por extenso), para a voz não tropeçar nos símbolos.

**Instrução de estilo (cole antes do texto no AI Studio):**
Leia em português do Brasil, como um estudante apresentando um seminário de engenharia: tom calmo, seguro e claro, ritmo moderado, sem pressa. Faça uma pausa curta entre os parágrafos e uma pausa um pouco maior depois de cada conta.

---

## Áudio 1: slide6.wav (Passo 1, recursão)

Obrigado, André. Eu vou responder o item a: mostrar de onde vem a fórmula de h de n.

A resposta ao impulso é a saída quando a entrada é o impulso. Então eu troco x de n por delta de n, e chamo a saída de h de n. A equação fica: h de n, igual a a vezes h de n menos um, mais delta de n. E o repouso me dá h de menos um igual a zero.

Agora é só aplicar a equação amostra por amostra.

Em n igual a zero: h de zero é a vezes h de menos um, que é zero, mais delta de zero, que é um. Resultado: um. Esse é o único instante em que o impulso entra.

Em n igual a um: a vezes h de zero, que é um, mais delta de um, que é zero. Resultado: a.

Em n igual a dois: a vezes a, mais zero. a ao quadrado. E assim por diante: a ao cubo, a à quarta.

A partir de n igual a um, o delta já é zero. Então só a realimentação trabalha, e cada amostra é a vezes a anterior.

Com os valores do enunciado: para a igual a 0,8, a sequência encolhe: um; 0,8; 0,64; 0,512. Para a igual a 1,2, ela cresce: um; 1,2; 1,44; 1,728. E para a igual a menos 0,8, temos os mesmos valores do primeiro caso, mas o sinal alterna, porque a potência de um número negativo troca de sinal a cada passo.

A tabela sugere que h de n é a elevado a n. Mas padrão não é prova: são só cinco valores, e n vai até o infinito. Por isso, o passo dois.

---

## Áudio 2: slide7.wav (Passo 2, indução)

Para provar que vale para todo n, eu uso indução. A ideia é a de uma fila de dominós: se o primeiro cai, e cada um derruba o próximo, todos caem.

Base, n igual a zero: h de zero é um, e um é a elevado a zero. Confere.

Hipótese: suponho que vale para n menos um. Ou seja, h de n menos um é igual a a elevado a n menos um, para algum n maior ou igual a um.

Passo: pela equação, h de n é a vezes h de n menos um, mais delta de n. Como n é pelo menos um, delta de n é zero. Usando a hipótese, h de n é a vezes a elevado a n menos um, mais zero. Ou seja, a elevado a n.

Vale no zero e, sempre que vale num n, vale no seguinte. Logo, vale para todo n maior ou igual a zero.

Falta o caso de n negativo. O sistema parte do repouso e é causal: não responde antes de a entrada chegar. Então h de n é zero para todo n negativo. Quem registra isso é o degrau, u de n, que vale um para n maior ou igual a zero, e zero antes. O u de n não é enfeite: sem ele, a elevado a n daria valores diferentes de zero para n negativo.

Isso responde o item a: h de n, igual a a elevado a n, vezes u de n.

Passo a palavra para o Manoel, que vai usar essa fórmula para decidir a estabilidade.
