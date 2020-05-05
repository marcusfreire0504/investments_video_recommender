# Como criar uma solução completa de Data Science (Curso ministrado por Mário Filho)

É extremamente importante definir corretamente o problema a ser abordado, a fim de avaliar a viabilidade de uma solução baseada em dados. O primeiro no início de qualquer projeto dessa natureza deve ser a determinação da sua continuidade. Esse projeto irá utilizar o conhecimento obtido no curso do Cientista de Dados Mário Filho, para criar uma lista de recomendação de vídeos mais relevantes sobre finanças e investimentos. Nas linhas a seguir, serão seguidos os passos indicados pelo instrutor, alterando o escopo do projeto para o assunto de interesse.


## Módulo 1: Definindo o problema

**Problema**
    
   Tenho dificuldades de encontrar vídeos sobre investimentos que sejam do meu interesse, devido ao grande número disponível no youtube.
    
**Qual a solução *ideal*?**
    
   Ter uma lista somente dos vídeos que realmente me interessam.
    
**Como resolver esse problema com Data Science/Machine Learning?**
    
   Podemos criar uma aplicação capaz de recomendar vídeos do youtube.
    
**Como utilizar a solução em produção?**
   
   Há diferentes abordagens possíveis para apresentar a solução:
   
   * Abordagem com "ponto de corte" -> Ex.: Retornar apenas o Top 3 de vídeos.
   * Abordagem de ranking -> Ordenar os vídeos em ordem descrescente de interesse
   
   A apresentação pode ser feita através de um web app com os links para os vídeos, ordenados com base na previsão de interesse.
   

**Como avaliar se a solução está correta?**

Todo projeto real deve ter métricas bem definidas (ainda na fase de planejamento), que servirão para validar o resultado da solução proposta para o problema. Uma abordagem interessante é a definição de uma (única) métrica primária, e algumas métricas secundárias. A medição dessas métricas com a solução pronta permitirá avaliar os ganhos promovidos pela aplicação de Data Science na resolução do problema.

No nosso contexto, podemos definir as seguintes métricas:

* **Métrica Primária:** Quantos vídeos dentre os top N recomendados eu adicionaria à minha lista de *Assistir Depois*?

* **Métrica Secundária (1):** Quanto tempo eu gastaria selecionando vídeos de interesse através da busca nativa no youtube *vs* utilizando a lista recomendada?

* **Métrica Secundária (2):** Quantos vídeos dentre os top N são de canais que já estou inscrito?

A definição correta de métricas permite atestar o valor da solução e provar para o cliente o valor agregado que estamos entregando.







       
   
   
    
    
    
    
