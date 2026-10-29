# Diretor Fotográfico IA Ultimate
Skill de direção fotográfica e criação de prompts com IA: enquadramento, iluminação, temperatura, lentes, ângulos e posição do modelo. Baseada nos documentos IAShots/Nelson Junior fornecidos, com fontes e correções identificadas.

## Modo guiado é o padrão
A Skill explica, recomenda e pergunta **uma decisão por vez**, aproveitando o que já foi informado. Aceita “escolha por mim” e “somente o prompt”. Não repete perguntas respondidas. Para “medium clouse-up”, reconhece o termo, explica o corte, dá exemplo provisório e conduz as escolhas restantes. Entrega final: resumo, prompt PT-BR e EN equivalentes, justificativa curta.

## Conteúdo detalhado
28 técnicas operacionais: seis enquadramentos, quatro padrões de luz, três temperaturas, quatro lentes, sete ângulos e quatro orientações. Fontes textuais das 56 páginas do eBook e 32 do guia dentro da pasta da Skill; cinco arquivos de guia eram duplicatas. Tabelas, fórmula, exemplos, erros e glossário preservados. 24 prompts das imagens do guia transcritos, além das notas visuais. [Cobertura](docs/CONTENT_COVERAGE.md).

[SKILL.md](.agents/skills/diretor-fotografico-ia-ultimate/SKILL.md) contém núcleo e catálogo completo; referências incluídas guardam os textos detalhados. O pacote não distribui os PDFs nem promete reprodução pixel a pixel. Leitura panorâmica de todas as páginas e ampliação selecionada; validação comportamental continua pendente.

## O que faz
Consulta de técnicas com exemplos, criação a partir de briefing, revisão, complementação integral, combinações, modo didático, variações controladas, análise de referência condicional e refinamento de resultado disponível. Não gera imagens por padrão nem presume integrações. Medidas, EXIF e respostas perfeitas do modelo não são garantidas.

## Instalação, ferramentas e atualização
Copiar toda a pasta `.agents/skills/diretor-fotografico-ia-ultimate` para a mesma estrutura do projeto; reconhecimento depende do host. [Instruções](docs/INSTALLATION.md). Modelo de linguagem basta para texto; visão para analisar fotos e ferramenta externa para gerar. Sem credenciais obrigatórias. Atualizações: preservar mudanças locais, consultar CHANGELOG e repetir testes.

## Testes
```bash
python -m pip install -r tests/requirements.txt
python tests/validate_skill.py
python -m unittest discover -s tests -p 'test_*.py'
```
Testes estruturais verificam YAML, links, 28 técnicas, 88 registros de cobertura, fontes por página e contratos essenciais. Não comprovam semântica de cada resposta, fidelidade óptica ou visual. [Aceitação](tests/acceptance-tests.md), [resultados](tests/validation-results.md), [auditoria](docs/FUNCTIONAL_AUDIT.md).

## Origem e licença
MIT para contribuições originais, com exceção explícita do material de origem. [NOTICE](NOTICE.md) registra autoria IAShots/Nelson Junior. Não é exportação de instruções privadas de GPT, nem versão oficialmente endossada dos PDFs. Simplificações e inconsistências da fonte estão separadas das correções técnicas.
