# Fala do João: slides 6 e 7 (passos 1 e 2, item a)

Versão ampliada da fala do roteiro da equipe. As contas são as mesmas dos slides; só ganharam ligação entre si. Diga com as suas palavras, sem ler. Tempo estimado: 2 min a 2 min 30 s.

## Slide 6: Passo 1, recursão com x[n] = δ[n]

> "Obrigado, André. Eu vou responder o item (a): mostrar de onde vem a fórmula de h[n].
>
> A resposta ao impulso é a saída quando a entrada é o impulso. Então eu troco x[n] por δ[n] e chamo a saída de h[n]. A equação fica **h[n] = a·h[n−1] + δ[n]**, e o repouso me dá **h[−1] = 0**.
>
> Agora é só aplicar amostra por amostra *(apontar a tabela)*:
> em n = 0, h[0] = a·0 + δ[0] = 0 + 1 = **1**. Esse é o único instante em que o impulso entra.
> Em n = 1, h[1] = a·h[0] + δ[1] = a·1 + 0 = **a**.
> Em n = 2, a·a + 0 = **a²**, e assim por diante: a³, a⁴.
>
> A partir de n = 1 o δ[n] já é zero, então só a realimentação trabalha, e cada amostra é **a vezes a anterior**.
>
> Com os valores do enunciado: para a = 0,8 a sequência encolhe (1; 0,8; 0,64; 0,512…); para a = 1,2 ela cresce (1; 1,2; 1,44; 1,728…); e para a = −0,8 temos os mesmos módulos do primeiro caso, mas o sinal alterna, porque potência de número negativo troca de sinal a cada passo.
>
> A tabela sugere h[n] = aⁿ. Mas **padrão não é prova**: são só cinco valores, e n vai até o infinito. Por isso, o passo 2."

## Slide 7: Passo 2, forma fechada por indução

> "Para provar para todo n, uso indução. A ideia é a de uma fila de dominós: se o primeiro cai e cada um derruba o próximo, todos caem.
>
> **Base**, n = 0: h[0] = 1, e 1 = a⁰. Confere.
>
> **Hipótese**: suponho que vale para n − 1, ou seja, h[n−1] = aⁿ⁻¹, para algum n ≥ 1.
>
> **Passo**: pela equação, h[n] = a·h[n−1] + δ[n]. Como n ≥ 1, δ[n] = 0. Usando a hipótese, h[n] = a·aⁿ⁻¹ + 0 = **aⁿ**.
>
> Vale no zero e, sempre que vale num n, vale no seguinte; logo vale para todo n ≥ 0.
>
> Falta n negativo: o sistema parte do repouso e é causal, então não responde antes de a entrada chegar, e h[n] = 0 para n < 0. Quem registra isso é o degrau u[n], que vale 1 para n ≥ 0 e 0 antes. O u[n] não é enfeite: sem ele, aⁿ daria valores diferentes de zero para n negativo.
>
> Isso responde o item (a): **h[n] = aⁿ u[n]**. Passo a palavra para o Manoel, que vai usar essa fórmula para decidir a estabilidade."

## Se travar, lembre das 4 ideias

1. Troco x por δ e parto do repouso: h[−1] = 0.
2. Amostra por amostra: 1, a, a², a³… → padrão aⁿ.
3. Padrão ≠ prova → indução: base, hipótese, passo.
4. n < 0 ⇒ zero, e o u[n] registra isso.

## Perguntas mais prováveis sobre a sua parte

| Pergunta | Resposta curta |
| --- | --- |
| Por que indução, se a tabela já mostra? | A tabela mostra alguns valores; a indução garante para todo n ≥ 0. |
| O que é "em repouso"? | y[−1] = 0. Sem isso a saída tem parcela da condição inicial e não é h[n]. |
| Para que serve o u[n]? | Registra h[n] = 0 para n < 0 (causal + repouso). |
| h[3] para a = −0,8? | (−0,8)³ = −0,512. |
| Por que primeira ordem? | Depende de uma só saída passada, y[n−1]. |
| FIR ou IIR? | IIR: aⁿ nunca zera de vez, por causa da realimentação. |
| E com y[−1] = c? | Soma-se c·aⁿ⁺¹; a saída deixa de ser a resposta ao impulso. |
