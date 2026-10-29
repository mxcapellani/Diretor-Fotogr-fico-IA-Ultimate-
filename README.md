# Diretor Fotográfico IA

Uma skill prática de direção fotográfica e criação de prompts para imagens com IA. Ela transforma uma intenção visual em instruções claras de enquadramento, luz, lente, ângulo e pose; propõe exemplos e variações controladas; e revisa a coerência do resultado.

## Como usar

Descreva a imagem que deseja — tema, personagem ou produto, contexto, atmosfera e finalidade. Se algum detalhe estiver em aberto, a skill deve fazer poucas perguntas objetivas ou declarar as escolhas que está assumindo. Em seguida, deve:

1. **Definir a intenção.** Resumir o assunto, a ação, a emoção e a história em uma frase. Identificar o que precisa chamar a atenção primeiro.
2. **Escolher a linguagem fotográfica.** Determinar plano e composição, ponto de vista, lente e perspectiva, iluminação, pose, paleta e profundidade de campo. Cada escolha deve apoiar a intenção, não apenas acumular termos técnicos.
3. **Montar o prompt.** Organizar as decisões em uma descrição visual concreta, com o assunto e a ação primeiro, seguida das instruções de fotografia, ambiente, cor e acabamento.
4. **Checar a coerência.** Procurar instruções conflitantes, relações espaciais impossíveis, iluminação incompatível ou detalhes que desviem do foco.
5. **Iterar com controle.** Manter as decisões que funcionam e alterar uma variável por vez, explicando o que mudou e o efeito esperado.

## Direção fotográfica

Use estas escolhas como ferramentas narrativas:

| Elemento | O que especificar | Efeito que pode produzir |
| --- | --- | --- |
| **Enquadramento** | plano geral, plano médio, close-up; espaço negativo; posição do assunto; linhas e equilíbrio | situa, aproxima, isola ou conduz o olhar |
| **Ângulo** | altura dos olhos, plongée, contra-plongée, perfil, três quartos | altera a relação de intimidade, vulnerabilidade ou presença |
| **Lente e perspectiva** | distância focal aproximada e distância da câmera; perspectiva ampla ou comprimida | controla distorção, campo de visão e separação entre planos |
| **Iluminação** | fonte, direção, tamanho/difusão, contraste e temperatura de cor | estabelece volume, hora, atmosfera e hierarquia visual |
| **Pose e gesto** | orientação do corpo, posição das mãos, direção do olhar e ação | comunica intenção e dá naturalidade ou energia |
| **Foco e profundidade** | plano de foco, fundo nítido ou desfocado, profundidade de campo | separa o assunto ou preserva informações do ambiente |
| **Cor e acabamento** | paleta, contraste, textura e caráter fotográfico | reforça o clima e mantém unidade entre imagens |

Especifique a lente junto com a perspectiva pretendida, não como garantia de um resultado óptico exato. Por exemplo, uma câmera próxima com lente grande-angular tende a exagerar a perspectiva; uma câmera mais distante com teleobjetiva tende a comprimi-la. Para retratos naturais, indique também a distância e evite pedir uma grande-angular muito próxima do rosto.

## Estrutura de prompt

Adapte esta sequência ao gerador utilizado; remova os campos que não forem relevantes:

> **[Assunto e ação]**, em **[local e contexto]**. **[Enquadramento e composição]**, câmera **[altura/ângulo e posição]**, perspectiva de **[lente aproximada e distância]**. **[Fonte, direção e qualidade da luz]**, com **[contraste e temperatura]**. **[Pose, gesto e direção do olhar]**. **[Plano de foco e profundidade de campo]**. Paleta **[cores]**, atmosfera **[clima]**, acabamento **[caráter visual]**. **[Restrições essenciais e elementos a evitar]**.

Prefira descrições observáveis e específicas a sequências de adjetivos. Inclua apenas restrições úteis — por exemplo, “duas mãos visíveis, sem objetos extras” — e evite instruções vagas ou contraditórias. Termos de estilo devem complementar, não substituir, a descrição da cena e da fotografia.

## Exemplo completo

**Intenção:** retrato editorial intimista de uma florista encerrando o trabalho, com sensação de calma e fim de tarde.

**Prompt:**

> Retrato editorial de uma florista adulta organizando um buquê na bancada de sua pequena loja ao fim do expediente. Plano médio vertical, pessoa posicionada no terço direito e espaço negativo suave à esquerda; câmera na altura dos olhos, ângulo de três quartos. Perspectiva natural de uma lente de retrato de aproximadamente 50 mm, câmera a uma distância confortável. Luz quente de fim de tarde entrando por uma janela à esquerda, difusa por uma cortina; sombras suaves e preenchimento discreto do ambiente. Postura relaxada, mãos ocupadas ajustando uma haste, olhar dirigido ao buquê. Foco nos olhos e nas mãos, fundo da loja suavemente desfocado, flores ao fundo ainda reconhecíveis. Paleta de verdes apagados, creme e âmbar, textura fotográfica natural, atmosfera serena e espontânea. Manter anatomia natural e uma única pessoa; sem texto, logotipos ou objetos duplicados.

O exemplo conecta as escolhas: a janela lateral motiva a direção das sombras, o gesto sustenta a narrativa e o fundo desfocado mantém a atenção no rosto e nas mãos.

## Variações controladas

Congele o assunto, a ação, o local, a pose, a paleta e o acabamento; varie apenas o elemento indicado. Isso facilita comparar resultados e identificar a causa de uma mudança.

**Prompt-base fixo:** use o exemplo da florista acima sem alterar assunto, ação, composição, pose, paleta ou acabamento.

| Versão | Única variável | Alteração |
| --- | --- | --- |
| A | Iluminação | Trocar a luz difusa da janela por uma luz lateral mais marcada, mantendo a mesma direção e temperatura; preservar detalhe nas sombras. |
| B | Enquadramento | Trocar o plano médio por um close-up que inclua rosto e mãos; manter o ângulo e a posição da câmera. |
| C | Perspectiva | Usar uma perspectiva um pouco mais comprimida com câmera mais distante e lente mais longa; manter o mesmo tamanho aparente do assunto no quadro. |
| D | Ângulo | Mover a câmera da altura dos olhos para um ângulo ligeiramente acima; manter lente, distância, luz e composição. |
| E | Pose | Manter todo o restante e mudar apenas o olhar: da flor para a câmera, sem alterar a ação das mãos. |

Ao entregar uma série, forneça o prompt-base e liste cada variação como uma substituição explícita. Não misture alterações independentes em uma mesma versão. Se o usuário pedir exploração livre, separe as direções em opções distintas em vez de apresentar uma combinação como comparação controlada.

## Revisão de coerência visual

Revise o prompt antes de entregar e, quando houver uma imagem gerada, compare o resultado com a intenção:

- **Leitura:** o assunto e a ação principal estão claros e recebem prioridade visual?
- **Enquadramento:** plano, orientação e espaço negativo são compatíveis com o uso pretendido?
- **Geometria:** distância, lente, perspectiva, posição da câmera e escala dos elementos fazem sentido em conjunto?
- **Luz:** direção, dureza, cor, sombras e reflexos são consistentes com as fontes descritas?
- **Pose:** gesto, mãos, olhar e ação parecem possíveis e contam a história desejada?
- **Foco:** o plano de foco favorece o assunto sem apagar informação necessária?
- **Continuidade:** em uma série, permanecem estáveis identidade, roupa, cenário, paleta, luz e linguagem visual que não foram escolhidos para variar?
- **Conflitos:** há instruções incompatíveis, como “luz suave sem sombras” junto de “sombras duras”, ou “fundo totalmente nítido” junto de “profundidade de campo muito rasa”?

Se encontrar um problema, indique o que está incoerente e proponha uma correção localizada. Preserve as escolhas aprovadas e altere somente o necessário. Não prometa controle perfeito do gerador: quando um detalhe crítico não for garantido por texto, diga isso e sugira uma nova geração ou ajuste iterativo.

## Formato de resposta sugerido

1. **Direção:** uma frase com a intenção visual e as decisões principais.
2. **Prompt pronto:** texto contínuo, fácil de copiar e adaptar.
3. **Variações:** opções identificadas, cada uma mudando uma variável por vez.
4. **Revisão:** conflitos encontrados ou confirmação breve de coerência e aspectos que podem exigir iteração.
