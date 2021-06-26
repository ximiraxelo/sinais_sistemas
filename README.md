# Plotar funções degrau, gate e impulso

Script super simples para plotar funções da matéria de Sinais e Sistemas (ET64A - A41) ministrada pelo Professor Dr. Cristiano Marcos Agulhari.

## Construção

Código criado inteiramente no *Python 3.9.5* com adições das bibliotecas:

<details>
  <summary>NumPy</summary>	

  Biblioteca que adiciona funções matemática como cosseno, seno, tangente, módulo, função teto e logaritmos. Além disso, adiciona constantes matemáticas como número de euler (e) e pi.

  [Veja mais](https://numpy.org/)

</details>

<details>
  <summary>Matplotlib.pyplot</summary>

  Biblioteca usada para plotar gráficos de funções e mostrar a precisão dos métodos a cada iteração.

  [Veja mais](https://matplotlib.org/)

</details>

## Tutorial

Digite a função completa usando sempre a variável $t$
* Para função degrau use: $u(t)$
* Para função gate use: $g(t, \Delta)$ onde delta pode ser qualquer valor e por padrão é $1$
* Para função impulso use: $d(t)$

## Exemplo

$f(t) = u(t+1) - u(t-3) + g(t-3, 3) + 2 \times d(t-6)$ 

![example](example.jpeg)