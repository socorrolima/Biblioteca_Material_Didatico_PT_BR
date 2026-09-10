# Especificação da Plataforma Digital de Apoio ao Ensino de Português — Fase 1

**Documento de concepção e especificação conceitual, pedagógica, editorial e funcional**
Versão 1.0 — Fase 1 (Concepção)
Data: 10/09/2026

---

## Convenções de leitura

Ao longo do documento, as afirmações são marcadas para separar o que é fato externo do que é decisão do projeto:

| Marca | Significado |
|---|---|
| **[REFERÊNCIA OFICIAL]** | Conteúdo derivado da documentação oficial da ILR (Interagency Language Roundtable). Representa, de forma resumida em português, o que a fonte descreve. O texto integral e a redação exata estão em https://www.govtilr.org/Skills/Writing.htm |
| **[DECISÃO PEDAGÓGICA]** | Interpretação pedagógica adotada pela equipe para operacionalizar a referência. Não é definição oficial. |
| **[PROPOSTA DE PRODUTO]** | Decisão de produto, editorial, de arquitetura de informação ou de experiência. |
| **[HIPÓTESE A VALIDAR]** | Suposição que orienta o trabalho, mas que precisa de evidência (pesquisa com professores, teste de conteúdo, piloto) antes de ser tratada como certa. |
| **[VALIDAR COM CONTRATANTE]** | Ponto de decisão que depende de definição do contratante (escopo, orçamento, público, marca, jurídico). |

**Regra geral do documento:** quando uma decisão pedagógica e uma decisão tecnológica entram em conflito, a definição pedagógica é resolvida primeiro. A tecnologia (incluindo a escolha por Supabase e Vercel) é tratada como meio de execução, não como fator estruturante do produto.

---

## 1. Resumo executivo

A plataforma é uma **biblioteca digital de conteúdos, atividades e materiais para o ensino de português**, voltada primariamente a **professores** que dão aulas online (particulares, em escolas de idiomas, em programas institucionais ou em contexto de português como língua de acolhimento / língua estrangeira / segunda língua).

Ela **não é um curso**. Não há trilha obrigatória, matrícula, turma ou certificação nesta fase. O professor entra, encontra um material adequado ao seu aluno e à sua aula, e usa esse material — em sala, como tarefa, ou como base de um plano de aula.

O diferencial é a **consistência pedagógica**: todo conteúdo é organizado a partir da pergunta *"o que o aluno consegue fazer com a língua?"*. A referência de proficiência é a **escala de Writing da ILR**, usada como régua de capacidade — e não como lista de tópicos gramaticais. Cada unidade conecta, de forma explícita e pesquisável:

**NÍVEL → CAPACIDADE → FUNÇÃO COMUNICATIVA → GÊNERO → CONTEXTO → TAREFA → PRODUÇÃO → AVALIAÇÃO**

A experiência visual e editorial deve ter a qualidade de uma **publicação digital contemporânea** (revista, portal de jornalismo explicativo), e não a de um "ambiente virtual de aprendizagem" tradicional.

O escopo da Fase 1 é **definir o produto**. Não se desenvolve código, identidade visual definitiva, banco de dados nem funcionalidades de IA nesta etapa.

**Resultado esperado da Fase 1:** este documento, detalhado o suficiente para (a) fundamentar uma proposta comercial e (b) servir de briefing para as fases de UX/UI e de desenvolvimento.

**Pilha tecnológica-alvo (para fases seguintes):** Supabase (banco de dados PostgreSQL, autenticação, armazenamento de arquivos) e Vercel (hospedagem do front-end e funções). Esta escolha é registrada como premissa; ela não influencia as decisões pedagógicas e editoriais abaixo. **[VALIDAR COM CONTRATANTE]** (confirmar orçamento de infraestrutura, requisitos de residência de dados e política de privacidade aplicável, especialmente LGPD).

---

## 2. Problema

### 2.1 Para o professor de português

- **Falta de material organizado por capacidade.** A maioria dos recursos disponíveis é organizada por tópico gramatical ("presente do subjuntivo", "pronomes oblíquos") ou por livro didático. O professor que pensa "meu aluno precisa aprender a escrever um e-mail profissional de reclamação" não tem onde buscar isso diretamente.
- **Tempo de preparação alto.** Montar uma aula boa exige encontrar um texto adequado, adaptar o nível, criar atividades de compreensão, criar uma tarefa de produção e definir como avaliar. Isso se repete a cada aula.
- **Dispersão de fontes.** Textos vêm de um lugar, atividades de outro, critérios de avaliação de lugar nenhum. Não há coerência entre os materiais.
- **Dificuldade de calibrar nível.** Sem uma referência comum, "intermediário" quer dizer coisas diferentes para cada professor e cada escola. Isso dificulta continuidade quando o aluno troca de professor.
- **Pouco material contemporâneo e culturalmente relevante sobre o Brasil** com tratamento pedagógico (vocabulário, estruturas, tarefas, critérios).

### 2.2 Para o aluno (indireto nesta fase)

- Experiências de produção escrita sem critérios claros do que se espera.
- Materiais que ensinam *sobre* a língua, mas dão pouca oportunidade de *fazer* coisas com a língua.
- Progressão pouco transparente: o aluno não sabe o que já consegue fazer nem o que vem a seguir.

### 2.3 Para a instituição / coordenação pedagógica

- Falta de padrão compartilhado de qualidade e de nível entre professores.
- Dificuldade de garantir cobertura de funções comunicativas e gêneros ao longo de um programa.
- Retrabalho: cada professor reconstrói material que outro já fez.

**[HIPÓTESE A VALIDAR]** O gargalo mais caro para o professor é o tempo de preparação e a calibragem de nível — não a falta de textos em si. A pesquisa com professores na Fase 1/início da Fase 2 deve confirmar ou corrigir essa priorização.

---

## 3. Objetivos

### 3.1 Objetivo geral

Oferecer a professores de português uma biblioteca digital coerente, pesquisável e reutilizável de conteúdos e atividades, ancorada numa referência de proficiência (ILR Writing) e organizada pela pergunta *"o que o aluno consegue fazer com a língua?"*.

### 3.2 Objetivos específicos do produto

1. Reduzir o tempo de preparação de uma aula de produção escrita para menos de 15 minutos quando existir material adequado na biblioteca. **[HIPÓTESE A VALIDAR]** (meta a testar no piloto)
2. Permitir que o professor encontre conteúdo por **capacidade + contexto + gênero + duração**, e não apenas por tópico gramatical.
3. Garantir que todo conteúdo publicado traga: objetivo em termos de capacidade, nível ILR de referência, função comunicativa, gênero, contexto, tarefa de produção e critérios de avaliação.
4. Fornecer uma **rubrica operacional** de produção escrita, derivada das quatro dimensões da ILR, que o professor consiga aplicar em poucos minutos.
5. Oferecer material pronto para uso em dois formatos: **material do aluno** (para compartilhar) e **material do professor** (com orientações e gabarito).
6. Manter consistência de nível entre conteúdos por meio de um processo editorial padronizado.
7. Entregar uma experiência de navegação e leitura com qualidade de publicação digital.

### 3.3 Objetivos explicitamente fora do escopo da Fase 1

- Desenvolver código, back-end, banco de dados.
- Criar identidade visual definitiva.
- Implementar funcionalidades de IA.
- Definir modelo de negócio / precificação em detalhe (registrado como ponto para o contratante).
- Produzir a biblioteca completa de conteúdos (apenas o modelo e o dimensionamento do piloto).

### 3.4 Indicadores de sucesso (para as fases seguintes) — [PROPOSTA DE PRODUTO]

| Dimensão | Indicador | Fonte |
|---|---|---|
| Adoção | nº de professores ativos / semana | analytics |
| Utilidade | % de sessões que terminam em "Usar em aula" ou download | analytics |
| Eficiência | tempo médio entre busca e uso de um conteúdo | analytics |
| Qualidade percebida | nota média de utilidade do conteúdo (avaliação do professor) | feedback in-app |
| Cobertura | % de células da matriz pedagógica com pelo menos 1 conteúdo publicado | painel editorial |
| Retenção | % de professores que voltam em 30 dias | analytics |

---

## 4. Público-alvo

### 4.1 Público primário — Professor de português (usuário e decisor de uso)

**[PROPOSTA DE PRODUTO]** Personas de trabalho (a validar em pesquisa):

- **Professor particular online (freelancer).** Dá aulas 1:1 por videochamada. Alunos adultos, muitos estrangeiros ou brasileiros no exterior. Precisa de material que funcione em tela compartilhada e como tarefa. Sensível a preço. Valoriza autonomia e rapidez.
- **Professor de escola de idiomas / programa de português para estrangeiros.** Segue um currículo, mas complementa com material próprio. Precisa de material alinhável a um referencial e a um plano de curso. Coordenação pode exigir padrão.
- **Professor de português como língua de acolhimento** (migrantes, refugiados). Turmas heterogêneas, foco em uso funcional imediato (formulários, bilhetes, serviços públicos, trabalho). Recursos limitados, necessidade de material para download e impressão.
- **Professor de português em contexto acadêmico / preparação para fins específicos** (por exemplo, proficiência para pós-graduação, português para negócios, para diplomacia). Precisa de níveis mais altos, gêneros formais e critérios de avaliação defensáveis.

**Contexto de uso comum a todos:** aula online, tela compartilhada, preparação entre atendimentos, uso em dispositivos variados (notebook predominante; tablet e celular para consulta).

### 4.2 Público secundário — Aluno (usuário de conteúdo, não gerido nesta fase)

Adulto, majoritariamente. Aprende português como língua estrangeira / segunda língua / de herança / de acolhimento. Acessa o material que o professor indica. Na Fase 1/MVP **não tem conta**; consome material do aluno por link ou arquivo. **[DECISÃO PEDAGÓGICA]** O aluno é destinatário do conteúdo, mas a plataforma é desenhada para o professor decidir o quê e quando.

### 4.3 Público terciário — Coordenação pedagógica / instituição

Interessada em padrão de qualidade, cobertura curricular e economia de retrabalho. Na Fase 1/MVP é atendida indiretamente (pelo padrão editorial e pelas coleções). Funcionalidades institucionais (turmas, gestão de professores, relatórios) ficam para a Fase 3.

### 4.4 Fora do público-alvo nesta fase

- Autoaprendizes sem professor (podem usar, mas não são o alvo do desenho).
- Crianças em alfabetização inicial em português como L1.
- Instituições que queiram LMS completo com matrícula e certificação.

**[VALIDAR COM CONTRATANTE]** Qual desses públicos primários é prioritário para o piloto? A resposta muda a matriz temática, a faixa de níveis a cobrir primeiro e a necessidade de material para impressão.

---

## 5. Conceito do produto

### 5.1 Definição em uma frase

**[PROPOSTA DE PRODUTO]** Uma biblioteca digital editorialmente curada de conteúdos e atividades de português, organizada por capacidade comunicativa e ancorada na escala ILR Writing, feita para o professor encontrar e usar material de qualidade em minutos.

### 5.2 O que o produto é

- Uma **coleção navegável e pesquisável** de unidades pedagógicas independentes.
- Cada unidade é **autossuficiente**: dá para usar sozinha, sem pré-requisitos obrigatórios.
- Cada unidade tem **metadados pedagógicos completos** (nível, capacidade, função, gênero, contexto, tema, duração, tipo de produção, critérios).
- Uma **camada editorial**: os conteúdos têm voz, cuidado de redação, curadoria de temas e qualidade visual de publicação.
- Um **conjunto de ferramentas leves para o professor**: filtros, busca, coleções, "usar em aula", materiais para download, rubrica de avaliação.

### 5.3 O que o produto não é

- Não é um curso nem uma trilha obrigatória.
- Não é um LMS (sem matrícula, notas, turmas, frequência nesta fase).
- Não é um banco de exercícios de gramática descontextualizada.
- Não é uma cópia dos sites de referência (ver 6.4): estes inspiram *organização e tipos de recurso*, não conteúdo nem layout.
- Não é uma ferramenta de correção automática por IA (Fase 3, se justificado).

### 5.4 Princípio organizador

**[DECISÃO PEDAGÓGICA]** Todo conteúdo responde primeiro a *"o que o aluno consegue fazer?"*. A gramática, o vocabulário e as estruturas aparecem **a serviço** de uma capacidade de uso — nunca como o ponto de partida da organização. A cadeia pedagógica da unidade é:

> **Nível** (referência ILR de proficiência)
> → **Capacidade** (o que o aluno consegue fazer, em termos observáveis)
> → **Função comunicativa** (identificar, informar, descrever, argumentar…)
> → **Gênero** (bilhete, e-mail, relato, artigo de opinião…)
> → **Contexto** (pessoal, profissional, público…)
> → **Tarefa** (o enunciado do que o aluno vai produzir)
> → **Produção** (o texto que o aluno entrega)
> → **Avaliação** (rubrica nas quatro dimensões da ILR)

### 5.5 Proposta de valor por público

| Público | "Uso isto porque…" |
|---|---|
| Professor freelancer | encontro material bom e pronto em minutos, com critério de avaliação junto |
| Professor de escola | tenho material alinhado a um referencial que a coordenação aceita |
| Professor de acolhimento | tenho material funcional, imprimível, sobre situações reais |
| Professor acadêmico / fins específicos | tenho níveis altos, gêneros formais e rubrica defensável |
| Coordenação | garanto padrão de nível e cobertura sem que cada professor refaça tudo |

### 5.6 Tom e experiência

**[PROPOSTA DE PRODUTO]** A experiência de leitura e navegação deve lembrar uma **publicação digital de alta qualidade**: tipografia editorial, hierarquia clara, imagens tratadas, textos com autoria e cuidado, tempo de leitura estimado, navegação leve. Deve-se evitar a estética de "plataforma de e-learning" (cores saturadas, ícones genéricos, barras de progresso onipresentes, gamificação).

---

## 6. Referencial pedagógico

### 6.1 A escala ILR Writing como referência de proficiência — [REFERÊNCIA OFICIAL]

A ILR (Interagency Language Roundtable) mantém descritores de habilidade em cinco níveis-base (0 a 5), com níveis "mais" (0+, 1+, 2+, 3+, 4+) que indicam desempenho acima de um nível-base sem alcançar plenamente o próximo. O domínio de um nível pressupõe o domínio dos anteriores.

A ILR descreve a proficiência em quatro aspectos que atravessam todos os níveis:

1. **Habilidade funcional** — os atos comunicativos ou tarefas que a pessoa consegue realizar.
2. **Precisão** — exatidão, amplitude e complexidade da língua.
3. **Conteúdo / significado** — relevância e cobertura substantiva dos temas.
4. **Adequação contextual** — registro, aceitabilidade e adequação da língua ao contexto e ao destinatário.

**Fonte:** https://www.govtilr.org/Skills/Writing.htm — o texto integral e a redação exata dos descritores devem ser consultados diretamente na fonte. As sínteses deste documento são resumos em português para fins de trabalho, não substituem o original.

### 6.2 Como a plataforma usa a ILR — [DECISÃO PEDAGÓGICA]

- A ILR é a **régua de capacidade**: cada conteúdo declara o nível ILR Writing de referência para a produção esperada.
- A ILR **não** é convertida em sequência de tópicos gramaticais. As estruturas linguísticas de uma unidade são listadas como *recursos a serviço da tarefa*, não como o currículo.
- A plataforma trabalha com a **faixa** de níveis, não com uma classificação exata do aluno. Um conteúdo pode ser marcado, por exemplo, como "ILR 1 / 1+" quando serve à transição entre esses níveis.
- Os descritores da plataforma para cada nível (seção 7) separam explicitamente **[REFERÊNCIA OFICIAL]** de **[DECISÃO PEDAGÓGICA]** e de **[PROPOSTA DE PRODUTO]**.

### 6.3 O que a plataforma NÃO faz com a ILR — [DECISÃO PEDAGÓGICA]

- **Não** estabelece equivalência automática entre ILR e CEFR, ACTFL, Celpe-Bras, níveis escolares ou qualquer outra escala. Onde houver necessidade de "tradução" para outra escala, isso é tratado como projeto editorial específico, com evidência, e marcado como **[HIPÓTESE A VALIDAR]**.
- **Não** apresenta interpretação pedagógica como se fosse definição oficial.
- **Não** reduz a ILR a "quanto de gramática o aluno sabe".

### 6.4 Referências de experiência editorial (organização, não conteúdo) — [PROPOSTA DE PRODUTO]

Sites de materiais para ensino de inglês são usados como referência de **organização e tipos de recurso**, e não devem ser copiados visual ou estruturalmente:

- **eslnewsstories.com/explainers** — referência de: textos explicativos curtos sobre temas de atualidade, organizados por assunto; combinação de texto + vocabulário + atividades; linguagem controlada por nível.
- **listenaminute.com** — referência de: unidades muito curtas e temáticas ("um minuto" sobre um assunto), com bateria consistente de atividades por unidade (compreensão, vocabulário, discussão, escrita); alto volume de temas do cotidiano.

**O que se aproveita como padrão:** unidades curtas e independentes; consistência de estrutura entre unidades; entrada por tema; bateria previsível de atividades; linguagem calibrada.
**O que NÃO se aproveita:** identidade visual, textos, marca, layout, taxonomia específica desses sites.

### 6.5 Princípios pedagógicos adotados — [DECISÃO PEDAGÓGICA]

1. **Uso antes de forma.** A unidade parte de uma tarefa comunicativa real.
2. **Gênero como ponte.** O aluno aprende a produzir textos de um gênero reconhecível, com suas convenções.
3. **Contexto autêntico.** As situações são plausíveis e culturalmente ancoradas (Brasil, mundo lusófono, vida do aprendiz adulto).
4. **Progressão em espiral, não linear.** Uma mesma função (por exemplo, "descrever") reaparece em níveis diferentes, com exigências maiores.
5. **Avaliação transparente.** O aluno sabe, antes de produzir, quais são os critérios.
6. **Autonomia do professor.** A plataforma sugere; o professor decide. Nada é obrigatório.
7. **Carga cognitiva controlada.** Cada unidade tem um foco principal; o restante é suporte.
8. **Acessibilidade.** Linguagem clara, contraste, materiais legíveis, alternativas textuais para mídia.

---

## 7. Matriz ILR (ETAPA 1)

### 7.1 Observações de método

- A coluna **Capacidade / Funções / Critérios** com marca **[REF. OFICIAL]** resume, em português e de forma abreviada, o que a documentação da ILR Writing descreve para o nível. A redação exata está na fonte.
- As colunas **Gêneros possíveis**, **Contextos** e **Tarefas** são majoritariamente **[DECISÃO PEDAGÓGICA]** e **[PROPOSTA DE PRODUTO]**: são caminhos de operacionalização, não definições da ILR.
- **Não há** equivalência com CEFR/ACTFL/níveis escolares em nenhuma linha.
- Níveis 4, 4+ e 5 são apresentados de forma mais sintética: **[VALIDAR COM CONTRATANTE]** se o produto cobrirá esses níveis no piloto (ver seção 20).

### 7.2 Tabela-síntese

| Nível | Capacidade (síntese) | Funções típicas | Gêneros possíveis | Contextos | Tarefas possíveis | Critérios de destaque |
|---|---|---|---|---|---|---|
| **0** `[REF. OFICIAL]` capacidade de escrita ausente ou limitada a letras/palavras isoladas ocasionais | copiar, transcrever, formar caracteres/palavras isoladas | — (pré-textual) | pessoal imediato | copiar o próprio nome, dados básicos, palavras conhecidas | traçado; reconhecimento de forma escrita `[DEC. PED.]` |
| **0+** `[REF. OFICIAL]` escreve palavras e frases memorizadas isoladas; listas simples; produção "telegráfica"; vocabulário muito limitado | listar, rotular, registrar dados pontuais | lista, etiqueta, campo de formulário simples | pessoal, cotidiano | lista de compras; preencher nome/idade/nacionalidade; legendar figuras | presença da informação; vocabulário de sobrevivência `[DEC. PED.]` |
| **1** `[REF. OFICIAL]` produz frases, afirmações e perguntas simples sobre si e o entorno imediato; preenche formulários básicos; escreve bilhetes curtos; erros frequentes; coesão mínima | identificar, preencher, informar (básico), perguntar (básico), descrever (muito simples) | formulário, bilhete, mensagem curta, lista comentada, legenda | pessoal, cotidiano, social básico | preencher ficha de cadastro; deixar bilhete avisando algo; escrever mensagem marcando horário; descrever a própria rotina em frases | informação presente e compreensível apesar dos erros; frases simples `[DEC. PED.]` |
| **1+** `[REF. OFICIAL]` inicia correspondência escrita simples além das necessidades básicas; bom controle de vocabulário de alta frequência; precisão ainda instável fora do previsível | relatar (fatos simples), pedir/agradecer por escrito, descrever com mais detalhe, narrar sequência simples | e-mail/carta pessoal curta, recado, post curto, descrição de pessoa/lugar, relato de um dia | pessoal, cotidiano, social | e-mail a um amigo contando novidades; recado de desculpa; descrição da cidade natal; relato de um passeio | encadeamento de frases; conectivos básicos; adequação mínima de registro (formal/informal) `[DEC. PED.]` |
| **2** `[REF. OFICIAL]` escreve documentos objetivos para necessidades de trabalho e situações do dia a dia; relata fatos e faz descrições diretas; material minimamente coeso | informar, relatar, descrever, instruir, comparar (simples), resumir (curto) | e-mail profissional simples, recado de trabalho, formulário complexo, instrução/procedimento, descrição técnica leve, relato de ocorrência, resumo de notícia | cotidiano, social, profissional, público (básico) | e-mail solicitando informação a um fornecedor; registrar uma ocorrência; escrever instruções de uso; resumir uma notícia em um parágrafo; comparar dois produtos | coesão de parágrafo; clareza factual; registro adequado ao trabalho; precisão em estruturas de alta frequência `[DEC. PED.]` |
| **2+** `[REF. OFICIAL]` comunica-se plenamente em muitos contextos informais e cotidianos; frequentemente produz mensagens coerentes, embora nem sempre com clareza ou consistência | explicar, justificar, expressar opinião, aconselhar, narrar com desenvolvimento, sintetizar | e-mail argumentativo curto, carta de reclamação, postagem de opinião, relato desenvolvido, resposta a solicitação, ata simples | cotidiano, social, profissional, público | reclamar de um serviço por escrito e pedir solução; dar um conselho fundamentado por e-mail; escrever uma opinião sobre um tema local; narrar um episódio com contexto e desfecho | organização em mais de um parágrafo; sustentação de ponto de vista com razões; controle de conectivos de contraste/causa `[DEC. PED.]` |
| **3** `[REF. OFICIAL]` escreve com precisão suficiente sobre temas profissionais e sociais; explica questões, defende posições, produz textos coesos, incluindo relatórios e trabalhos de pesquisa | explicar, argumentar, defender posição, persuadir, comparar/avaliar, resumir textos longos, adaptar registro | relatório, artigo, texto argumentativo, resenha, parecer, e-mail executivo, síntese, proposta | profissional, acadêmico, público, social | escrever um relatório com recomendação; produzir um texto argumentativo sobre uma política pública; resenhar um livro/filme; sintetizar duas fontes divergentes; redigir uma proposta | coesão global; precisão em estruturas complexas; adequação de registro sustentada; desenvolvimento lógico do argumento `[DEC. PED.]` |
| **3+** `[REF. OFICIAL]` escreve em vários estilos de prosa com precisão; usa linguagem culturalmente apropriada; emprega estratégias de discurso complexas em temas profissionais e teóricos | argumentar em profundidade, teorizar, ironizar de forma controlada, editorializar, negociar por escrito | editorial, ensaio, artigo especializado, documento de posição, parecer técnico extenso | acadêmico, público, profissional, especializado | escrever um editorial; produzir um ensaio com tese e contra-argumentação; redigir parecer técnico; documento de negociação | flexibilidade de estilo; nuance; sustentação de registro culto; estratégias retóricas `[DEC. PED.]` |
| **4** `[REF. OFICIAL]` escreve com considerável precisão; linguagem matizada e ajustada ao destinatário; lida com temas complexos, incluindo editoriais e sátira, com controle retórico sofisticado | persuadir com nuance, ironizar, adaptar voz a públicos distintos, sintetizar campos, aconselhar em alto nível | editorial sofisticado, sátira, discurso, artigo de fundo, texto de assessoria | público, especializado, cultural, profissional de alto nível | reescrever um mesmo conteúdo para dois públicos distintos; produzir um texto satírico; redigir um discurso | precisão fina; controle de tom e ironia; ajuste ao destinatário `[DEC. PED.]` |
| **4+** `[REF. OFICIAL]` linguagem articulada, sob medida e matizada; erros raros; usa recursos linguísticos diversos com flexibilidade na maioria dos contextos | — (refinamento do nível 4) | — | — | — | raridade de erro; amplitude de recursos; flexibilidade `[DEC. PED.]` |
| **5** `[REF. OFICIAL]` domínio equivalente ao de um falante culto instruído; escreve com clareza e precisão em praticamente qualquer contexto; integra conceitos com recursos retóricos sofisticados | qualquer função, em qualquer registro | qualquer gênero | qualquer contexto | — | equivalência a redator culto nativo; precisão e clareza plenas `[DEC. PED.]` |

### 7.3 Detalhamento por nível (Etapa 1, item a item)

Para cada nível abaixo: **capacidade funcional**, **tipo de produção esperada**, **autonomia**, **complexidade**, **precisão**, **conteúdo**, **adequação ao contexto**, **gêneros compatíveis**, **tipos de tarefa**. As caracterizações qualitativas de funcionalidade/precisão/conteúdo/adequação são resumos **[REF. OFICIAL]**; os desdobramentos em gêneros e tarefas são **[DEC. PED.]/[PROPOSTA DE PRODUTO]**.

#### ILR 0
- **Capacidade funcional** `[REF. OFICIAL]`: praticamente nenhuma capacidade de escrita funcional; no máximo letras, caracteres ou palavras isoladas ocasionais.
- **Produção esperada** `[DEC. PED.]`: cópia; registro do próprio nome e de dados pessoais mínimos.
- **Autonomia**: nula; depende de modelo para copiar.
- **Complexidade**: pré-frasal.
- **Precisão** `[REF. OFICIAL]`: não avaliável de forma significativa.
- **Conteúdo**: apenas dados pessoais isolados.
- **Adequação ao contexto**: não se aplica.
- **Gêneros compatíveis** `[DEC. PED.]`: nenhum gênero textual pleno; atividades de pré-escrita.
- **Tarefas** `[PROPOSTA DE PRODUTO]`: copiar palavras conhecidas; associar palavra escrita a imagem; escrever o próprio nome e nacionalidade.
- **Nota de produto**: nível provavelmente **fora do escopo do MVP** (público adulto já alfabetizado em algum sistema de escrita). `[VALIDAR COM CONTRATANTE]`

#### ILR 0+
- **Capacidade funcional** `[REF. OFICIAL]`: escreve algumas palavras e expressões memorizadas e isoladas; produz listas simples; escrita "telegráfica".
- **Produção esperada** `[DEC. PED.]`: listas, rótulos, preenchimento de campos com palavra única.
- **Autonomia**: muito baixa; produção baseada em repertório memorizado.
- **Complexidade**: palavras e sintagmas; sem oração completa consistente.
- **Precisão** `[REF. OFICIAL]`: vocabulário extremamente limitado; ortografia instável; estruturas praticamente ausentes.
- **Conteúdo**: necessidades imediatas de sobrevivência.
- **Adequação ao contexto**: incipiente.
- **Gêneros compatíveis** `[DEC. PED.]`: lista, etiqueta, campo de formulário simples, legenda de uma palavra.
- **Tarefas** `[PROPOSTA DE PRODUTO]`: lista de compras; preencher ficha com nome, idade, nacionalidade, telefone; rotular objetos de uma imagem; escrever os dias da semana com um compromisso em cada.

#### ILR 1
- **Capacidade funcional** `[REF. OFICIAL]`: escreve frases, afirmações e perguntas simples sobre si mesmo e o ambiente imediato; preenche formulários; escreve bilhetes curtos e simples.
- **Produção esperada** `[DEC. PED.]`: bilhetes, mensagens curtas, formulários, descrições muito simples em frases soltas.
- **Autonomia**: baixa; precisa de modelo e de tema previsível.
- **Complexidade**: frases simples, curtas; coesão mínima (e, mas, porque).
- **Precisão** `[REF. OFICIAL]`: erros frequentes, inclusive em estruturas básicas; ainda assim, a mensagem essencial costuma passar em contextos previsíveis.
- **Conteúdo**: vida pessoal, rotina, entorno imediato, necessidades concretas.
- **Adequação ao contexto** `[REF. OFICIAL]`: noção incipiente de formal/informal.
- **Gêneros compatíveis** `[DEC. PED.]`: formulário, bilhete, mensagem de aplicativo, lista comentada, legenda, mini-descrição.
- **Tarefas** `[PROPOSTA DE PRODUTO]`: preencher cadastro de biblioteca; bilhete avisando que saiu e volta às 18h; mensagem marcando um encontro; escrever 5 frases sobre a própria rotina; três perguntas para conhecer um colega novo.

#### ILR 1+
- **Capacidade funcional** `[REF. OFICIAL]`: inicia correspondência escrita simples além das necessidades básicas imediatas; começa a lidar com assuntos um pouco menos previsíveis.
- **Produção esperada** `[DEC. PED.]`: e-mail/carta pessoal curta, recado, descrição desenvolvida, relato simples.
- **Autonomia**: baixa a média; ainda se apoia em modelos, mas já recombina.
- **Complexidade**: várias frases encadeadas; parágrafo curto começa a aparecer.
- **Precisão** `[REF. OFICIAL]`: bom controle do vocabulário de alta frequência; precisão cai quando o tema sai do familiar.
- **Conteúdo**: experiências pessoais, planos, preferências, descrições de pessoas e lugares.
- **Adequação ao contexto**: distingue registro informal (amigo) de um pouco mais formal (professor, colega novo).
- **Gêneros compatíveis** `[DEC. PED.]`: e-mail pessoal, recado, post curto, descrição, relato de experiência.
- **Tarefas** `[PROPOSTA DE PRODUTO]`: e-mail contando as novidades do mês a um amigo; recado pedindo desculpa por um atraso e propondo remarcar; descrição da própria cidade para alguém que vai visitar; relato de um dia marcante.

#### ILR 2
- **Capacidade funcional** `[REF. OFICIAL]`: escreve documentos objetivos e diretos para necessidades rotineiras de trabalho e do dia a dia; relata fatos e faz descrições diretas; lida com trocas correntes.
- **Produção esperada** `[DEC. PED.]`: e-mail profissional simples, relato, instrução, descrição, resumo curto, comparação simples.
- **Autonomia**: média; escreve sem modelo em temas conhecidos, com apoio pontual em temas novos.
- **Complexidade**: parágrafos coesos; organização por tópicos; conectivos de sequência, causa e contraste.
- **Precisão** `[REF. OFICIAL]`: precisão suficiente nas estruturas de alta frequência; erros em estruturas complexas não costumam impedir a compreensão.
- **Conteúdo**: trabalho rotineiro, serviços, vida prática, atualidades acessíveis.
- **Adequação ao contexto** `[REF. OFICIAL]`: controla registro adequado a situações de trabalho e cotidianas.
- **Gêneros compatíveis** `[DEC. PED.]`: e-mail profissional, recado de trabalho, instrução/procedimento, descrição técnica leve, relato de ocorrência, resumo de notícia, comparação simples, formulário complexo.
- **Tarefas** `[PROPOSTA DE PRODUTO]`: e-mail a um fornecedor pedindo prazo e condições; instruções para um colega executar uma tarefa; registro de uma ocorrência para o RH; resumo de uma notícia em um parágrafo; comparação de dois planos de celular com recomendação.

#### ILR 2+
- **Capacidade funcional** `[REF. OFICIAL]`: comunica-se plenamente em muitos contextos informais e cotidianos; produz com frequência mensagens coerentes, ainda que nem sempre com clareza ou consistência plenas.
- **Produção esperada** `[DEC. PED.]`: e-mail argumentativo curto, carta de reclamação, texto de opinião, relato desenvolvido, aconselhamento por escrito.
- **Autonomia**: média-alta em temas concretos; mais frágil em temas abstratos.
- **Complexidade**: texto de vários parágrafos; introdução e fechamento reconhecíveis; subordinação mais variada.
- **Precisão** `[REF. OFICIAL]`: coerência frequente; lapsos de clareza e de consistência ainda ocorrem, sobretudo sob demanda de abstração.
- **Conteúdo**: questões práticas com alguma complexidade, opiniões sobre temas próximos, situações de conflito e negociação leve.
- **Adequação ao contexto**: ajusta registro a reclamação formal, pedido, aconselhamento.
- **Gêneros compatíveis** `[DEC. PED.]`: e-mail argumentativo, carta de reclamação, post de opinião, relato desenvolvido, resposta a solicitação, ata simples.
- **Tarefas** `[PROPOSTA DE PRODUTO]`: reclamar formalmente de uma cobrança indevida e pedir estorno; e-mail aconselhando um colega sobre uma decisão, com razões; texto de opinião sobre uma mudança no bairro; relato de um episódio de trabalho com contexto, problema e desfecho.

#### ILR 3
- **Capacidade funcional** `[REF. OFICIAL]`: escreve com precisão suficiente sobre temas de interesse prático, social e profissional; explica questões complexas, defende pontos de vista, produz textos coesos e bem organizados, incluindo relatórios e trabalhos de pesquisa.
- **Produção esperada** `[DEC. PED.]`: relatório, texto argumentativo, artigo, resenha, parecer, síntese de fontes, proposta.
- **Autonomia**: alta; escreve sem apoio em ampla gama de temas.
- **Complexidade**: estrutura global controlada; parágrafos articulados por progressão temática; recursos de coesão e de modalização.
- **Precisão** `[REF. OFICIAL]`: erros esporádicos, sobretudo em estruturas raras ou aspectos idiomáticos; não comprometem a comunicação e raramente perturbam o leitor nativo.
- **Conteúdo** `[REF. OFICIAL]`: cobre temas concretos e abstratos ligados a interesses profissionais e sociais com substância.
- **Adequação ao contexto** `[REF. OFICIAL]`: controla registro e convenções de gênero; adapta o texto ao destinatário e à finalidade.
- **Gêneros compatíveis** `[DEC. PED.]`: relatório com recomendação, texto argumentativo, artigo, resenha crítica, parecer, síntese, proposta, e-mail executivo.
- **Tarefas** `[PROPOSTA DE PRODUTO]`: relatório sobre um problema com diagnóstico e recomendação; texto argumentativo sustentando uma posição sobre política pública, com contra-argumento; resenha crítica de uma obra; síntese de duas fontes divergentes com posicionamento; proposta de projeto para uma coordenação.

#### ILR 3+
- **Capacidade funcional** `[REF. OFICIAL]`: escreve em diversos estilos de prosa com precisão; emprega estratégias discursivas complexas; trata temas profissionais e teóricos.
- **Produção esperada** `[DEC. PED.]`: editorial, ensaio, artigo especializado, documento de posição, parecer extenso.
- **Autonomia**: muito alta.
- **Complexidade**: alternância deliberada de estilo; ironia e ênfase controladas; arquitetura argumentativa elaborada.
- **Precisão** `[REF. OFICIAL]`: erros raros; linguagem culturalmente apropriada na maior parte do tempo.
- **Conteúdo**: temas abstratos, teóricos e especializados.
- **Adequação ao contexto** `[REF. OFICIAL]`: uso de linguagem culturalmente apropriada; sensibilidade a nuance e a implícito.
- **Gêneros compatíveis** `[DEC. PED.]`: editorial, ensaio, artigo especializado, parecer técnico, documento de negociação.
- **Tarefas** `[PROPOSTA DE PRODUTO]`: editorial sobre um tema controverso; ensaio com tese, desenvolvimento e refutação; parecer técnico; documento de posição institucional.

#### ILR 4, 4+, 5 (síntese)
- **4** `[REF. OFICIAL]`: escreve com precisão considerável; linguagem matizada e ajustada ao destinatário; controle retórico sofisticado, inclusive editorial e sátira. `[DEC. PED.]` Tarefas: adaptar um mesmo conteúdo a públicos distintos; produzir texto satírico; redigir discurso.
- **4+** `[REF. OFICIAL]`: linguagem articulada, sob medida e matizada; erros raros; grande flexibilidade de recursos.
- **5** `[REF. OFICIAL]`: domínio equivalente ao de um falante culto e instruído; clareza e precisão em praticamente qualquer contexto; integração sofisticada de conceitos.
- **Nota de produto** `[VALIDAR COM CONTRATANTE]`: sugere-se que o piloto cubra **0+ a 3/3+**; níveis 4–5 entram em fase posterior, com curadoria especializada.

### 7.4 Quatro dimensões da ILR aplicadas — [REF. OFICIAL] + [DEC. PED.]

| Dimensão | O que observa `[REF. OFICIAL]` | Como a plataforma usa `[DEC. PED.]` |
|---|---|---|
| Funcionalidade | qual tarefa comunicativa a pessoa realiza | define o **objetivo** e a **tarefa** da unidade |
| Precisão | exatidão, amplitude, complexidade | define as **estruturas linguísticas** e o critério de **precisão** da rubrica |
| Conteúdo | relevância e substância dos temas | define **tema**, **contexto** e o critério de **conteúdo/desenvolvimento** |
| Adequação | registro, aceitabilidade, adequação ao destinatário | define **gênero**, **destinatário** e o critério de **adequação** da rubrica |

---

## 8. Matriz de funções comunicativas (ETAPA 2)

### 8.1 Método — [DECISÃO PEDAGÓGICA]

- Uma **função comunicativa** é o que o texto *faz* (informar, pedir, argumentar).
- **Nenhuma função pertence a um único nível.** A mesma função reaparece em níveis diferentes, com exigências crescentes de precisão, extensão, abstração e controle de registro.
- A matriz abaixo indica, para cada função: a **faixa de níveis** em que costuma ser trabalhada de forma central, a **habilidade** dominante, os **gêneros** típicos, **contexto/tema** ilustrativos, uma **tarefa**, a **produção esperada**, a **complexidade**, o **vocabulário** e as **estruturas** relevantes, e os **critérios de avaliação** em destaque.
- "Faixa central" não significa exclusividade: por exemplo, "descrever" aparece já em ILR 1 (descrição telegráfica) e continua em ILR 3 (descrição técnica precisa).

### 8.2 Progressão e sobreposição (visão geral)

| Função | Aparece a partir de (aprox.) | Torna-se central em | Continua exigida até |
|---|---|---|---|
| identificar / rotular | 0+ | 0+–1 | sempre (subjacente) |
| preencher | 1 | 1–2 | sempre |
| informar | 1 | 1+–2 | sempre |
| perguntar (por escrito) | 1 | 1–2+ | 3+ |
| descrever | 1 | 1+–2 | 3+ |
| narrar | 1+ | 1+–2+ | 3 |
| relatar | 1+ | 2–2+ | 3+ |
| instruir | 2 | 2 | 3 |
| explicar | 2 | 2+–3 | 4 |
| comparar | 2 | 2+–3 | 3+ |
| resumir / sintetizar | 2 | 3 | 4+ |
| expressar opinião | 1+ (simples) | 2+ | 3+ |
| defender posição | 2+ | 3 | 4 |
| argumentar | 2+ | 3–3+ | 5 |
| persuadir | 3 | 3+–4 | 5 |
| negociar (por escrito) | 3 | 3+ | 4+ |
| aconselhar | 2 | 2+–3 | 4 |
| adaptar registro | 1+ (noção) | 3 | 5 |

### 8.3 Matriz operacional por função

Legenda de colunas: **Nível (faixa central)** · **Habilidade** · **Gênero(s)** · **Contexto / tema exemplo** · **Tarefa** · **Produção esperada** · **Complexidade** · **Vocabulário** · **Estruturas** · **Critérios em destaque**.

Todas as linhas são **[DECISÃO PEDAGÓGICA]** na organização e **[PROPOSTA DE PRODUTO]** nos exemplos.

| Função | Faixa central | Habilidade | Gêneros | Contexto / tema | Tarefa | Produção esperada | Complexidade | Vocabulário | Estruturas | Critérios |
|---|---|---|---|---|---|---|---|---|---|---|
| **Identificar / rotular** | 0+–1 | escrita | lista, legenda, campo de formulário | cotidiano / casa, mercado | rotular objetos de uma imagem da cozinha | 8–12 palavras/sintagmas corretos | palavra e sintagma | campos semânticos concretos | artigo + substantivo; gênero e número | informação correta; ortografia de alta frequência |
| **Preencher** | 1–2 | escrita | formulário, ficha, cadastro | público / serviços; profissional / RH | preencher ficha de matrícula e um campo de "observações" com 2 frases | formulário completo + microtexto | frase simples | dados pessoais, datas, endereços | presente; numerais; datas; ordem frásica | completude; adequação do campo aberto ao solicitado |
| **Informar** | 1+–2 | escrita | bilhete, recado, e-mail curto, aviso | pessoal; profissional | e-mail avisando a equipe sobre mudança de horário de uma reunião | 1 parágrafo claro | frase a parágrafo curto | tempo, lugar, motivo | presente/futuro; marcadores temporais; conectivo de causa | clareza factual; registro adequado ao destinatário |
| **Perguntar** | 1–2+ | escrita | mensagem, e-mail, formulário de contato | cotidiano; profissional | e-mail a uma escola pedindo informações sobre um curso (4 perguntas) | e-mail com saudação, perguntas ordenadas, fecho | frases interrogativas encadeadas | vocabulário do tema; fórmulas de cortesia | interrogativas diretas e indiretas; modalização (poderia, gostaria de saber) | clareza das perguntas; cortesia; organização |
| **Descrever** | 1+–2 (segue até 3+) | escrita | descrição de pessoa/lugar/objeto/processo | Brasil / cidades; ciência / natureza | descrever uma cidade brasileira para quem vai visitá-la | 2–3 parágrafos organizados (geral → específico) | parágrafo com progressão | adjetivos, localização, comparação | há/existe; adjetivação; orações relativas; comparativos | organização espacial/lógica; precisão adjetival; vivacidade |
| **Narrar** | 1+–2+ | escrita | relato pessoal, narrativa breve, post | pessoal; cultural / festas | narrar uma festa ou viagem marcante | narrativa com situação inicial, complicação, desfecho | vários parágrafos; sequência temporal | tempos do passado; marcadores temporais | pretérito perfeito x imperfeito; conectivos temporais; discurso indireto | progressão narrativa; contraste de tempos passados; coesão |
| **Relatar** | 2–2+ | escrita | relato de ocorrência, ata simples, relatório de visita | profissional; público | relatar uma ocorrência no trabalho para registro | relato objetivo, cronológico, impessoal | parágrafos factuais | vocabulário técnico do contexto; verbos de ação | voz passiva; nominalizações; pretérito; conectivos de sequência | objetividade; completude factual; impessoalidade adequada |
| **Instruir** | 2 | escrita | instrução, tutorial, procedimento, receita | cotidiano; profissional | escrever instruções para um colega executar uma rotina | lista de passos + observações de segurança | imperativo/infinitivo consistentes | verbos de ação; advérbios de modo; sequenciadores | imperativo; infinitivo impessoal; ordem sequencial; condicionais simples | clareza operacional; ordem correta; consistência de forma verbal |
| **Explicar** | 2+–3 | escrita | texto explicativo, verbete, e-mail esclarecedor | ciência; sociedade | explicar como funciona um serviço público (ex.: SUS, transporte integrado) | texto expositivo com definição, funcionamento, exemplo | 3–5 parágrafos; relações de causa e finalidade | conectivos explicativos; terminologia acessível | orações causais, finais, consecutivas; aposto explicativo; presente genérico | precisão conceitual; clareza para leigo; encadeamento causal |
| **Comparar** | 2+–3 | escrita | comparação, quadro comparativo comentado, resenha comparativa | cotidiano / compras; acadêmico | comparar duas soluções e recomendar uma | texto com critérios explícitos, semelhanças, diferenças, conclusão | estrutura ponto a ponto ou bloco a bloco | conectivos de contraste e semelhança; vocabulário avaliativo | comparativos/superlativos; conectivos concessivos; enquanto/ao passo que | critérios explícitos; equilíbrio; conclusão fundamentada |
| **Resumir / sintetizar** | 3 (começa em 2) | leitura→escrita | resumo, síntese, abstract | acadêmico; profissional | resumir um artigo em 150 palavras; sintetizar duas fontes | texto condensado, fiel, sem opinião (resumo) / com articulação de fontes (síntese) | reformulação, hierarquização | verbos de citação; nominalizações | discurso indireto; nominalização; orações reduzidas; conectivos de adição/contraste | fidelidade; concisão; hierarquia de ideias; integração de fontes (síntese) |
| **Expressar opinião** | 2+ (simples em 1+) | escrita | comentário, post de opinião, carta do leitor | público; cultura | escrever um comentário opinando sobre um tema local | opinião + 2 razões + exemplo | parágrafo(s) com tese e sustentação | verbos de opinião; modalizadores | "acho que / considero que"; subjuntivo em opinião negada; conectivos de justificativa | clareza da tese; pertinência das razões; registro |
| **Defender posição** | 3 | escrita | texto argumentativo, carta aberta, parecer | público; acadêmico | defender uma posição sobre uma política, respondendo a uma objeção | tese, argumentos, refutação, conclusão | argumentação em vários parágrafos | conectivos argumentativos; vocabulário abstrato | concessivas; "embora / ainda que" + subjuntivo; período composto; modalização | força argumentativa; tratamento do contra-argumento; coesão global |
| **Argumentar** | 3–3+ | escrita | ensaio, artigo de opinião, editorial | público; especializado | escrever um artigo de opinião com dados e contra-argumento | texto autoral com progressão argumentativa e fechamento | arquitetura argumentativa; hierarquia de argumentos | conectivos sofisticados; léxico abstrato e avaliativo | subordinação múltipla; recursos de ênfase; citação e paráfrase | consistência lógica; densidade argumentativa; estilo |
| **Persuadir** | 3+–4 | escrita | editorial, texto publicitário-institucional, discurso, carta de defesa | público; cultural | escrever um texto para convencer um público específico a mudar de comportamento | texto ajustado ao público-alvo, com apelo e razões | retórica deliberada; ajuste ao destinatário | recursos afetivos e retóricos; vocabulário de valor | perguntas retóricas; paralelismo; gradação; imperativo estratégico | adequação ao público; eficácia retórica; ética do apelo |
| **Negociar (por escrito)** | 3+ | escrita | e-mail de negociação, proposta com contrapartidas, ata de acordo | profissional | conduzir por e-mail uma negociação de prazo e escopo | sequência de mensagens com concessões e limites claros | gestão de face; modalização fina | fórmulas de negociação; hedging | condicionais; futuro do pretérito; orações concessivas; atenuação | clareza de interesses; preservação da relação; encaminhamento a acordo |
| **Aconselhar** | 2+–3 | escrita | e-mail de aconselhamento, coluna de conselhos, parecer orientativo | pessoal; profissional | responder a um pedido de conselho com recomendação fundamentada | diagnóstico + opções + recomendação + ressalvas | modalização; estrutura problema-solução | verbos de recomendação; conectivos condicionais | imperativo atenuado; "se eu fosse você"; futuro do pretérito; condicionais | pertinência do conselho; tato; clareza da recomendação |
| **Adaptar registro** | 3 (noção desde 1+) | escrita | reescrita de um mesmo conteúdo em versões formal/informal | profissional; social | reescrever um mesmo aviso para um chefe e para um colega próximo | duas versões com escolhas lexicais e sintáticas distintas | controle consciente de registro | pares de registro (pedir/solicitar; dar um help/auxiliar) | tratamento (você/senhor); nominalização x verbo; contrações; elipse | consistência de registro; adequação ao destinatário; preservação do conteúdo |

### 8.4 Como a matriz de funções alimenta o produto — [PROPOSTA DE PRODUTO]

- Cada **unidade pedagógica** declara **uma função principal** e, opcionalmente, funções secundárias.
- A **busca** e os **filtros** usam a função como eixo (ver seções 15 e 16).
- O **painel editorial** usa a matriz para monitorar cobertura: quais funções ainda têm pouco conteúdo em cada faixa de nível.

---

## 9. Matriz de gêneros (ETAPA 3)

### 9.1 Método — [DECISÃO PEDAGÓGICA]

Para cada gênero: **função(ões) comunicativa(s) dominante(s)**, **contextos de uso**, **faixa de níveis** em que costuma aparecer, **exemplos de tarefas**, **complexidade esperada**. A faixa de níveis indica onde o gênero é *produtível pelo aluno*, não onde ele pode ser *lido*.

### 9.2 Matriz

| Gênero | Função(ões) dominante(s) | Contextos de uso | Faixa de níveis (produção) | Exemplos de tarefa | Complexidade esperada |
|---|---|---|---|---|---|
| **Lista** | identificar, organizar | pessoal, cotidiano, profissional | 0+–1 | lista de compras; lista de tarefas priorizada | itens nominais; sem sintaxe complexa |
| **Formulário** | preencher, informar | público, profissional, acadêmico | 1–2 | ficha de cadastro; formulário de solicitação com campo aberto | dados + 1–3 frases no campo aberto |
| **Bilhete** | informar, pedir, avisar | pessoal, cotidiano | 1–1+ | bilhete avisando ausência; bilhete pedindo um favor | 2–4 frases; saudação e assinatura simples |
| **Mensagem (app/chat)** | informar, perguntar, combinar | pessoal, social, profissional | 1–2 | combinar um encontro; remarcar um compromisso com desculpa | turnos curtos; registro informal a neutro |
| **E-mail pessoal** | narrar, informar, manter relação | pessoal, social | 1+–2 | contar novidades; agradecer uma hospedagem | saudação, corpo em parágrafos, fecho; registro informal |
| **E-mail profissional** | solicitar, informar, responder, encaminhar | profissional, público | 2–3+ | pedir orçamento; responder a uma reclamação; encaminhar um problema com resumo | assunto, saudação formal, 1–3 parágrafos objetivos, fecho protocolar |
| **Descrição** | descrever | pessoal, Brasil/cultural, ciência | 1+–3+ | descrever um lugar; descrição técnica de um processo | progressão do geral ao específico; precisão adjetival/técnica |
| **Narrativa** | narrar | pessoal, cultural, literário | 1+–3 | narrar um episódio; conto curto com base em um disparador | enredo com situação, conflito, desfecho; contraste de passados |
| **Relato** | relatar | profissional, público, acadêmico | 2–3 | relato de ocorrência; relato de experiência profissional; diário de campo | objetividade; cronologia; impessoalidade quando pertinente |
| **Instrução** | instruir | cotidiano, profissional | 2 | passo a passo de um procedimento; regras de uso de um espaço | forma verbal consistente; sequência; avisos condicionais |
| **Resumo** | resumir | acadêmico, profissional | 2+–3+ | resumir uma notícia; resumo de artigo; ata-resumo de reunião | fidelidade; concisão; hierarquização |
| **Comparação** | comparar | cotidiano, acadêmico, profissional | 2+–3 | comparar dois produtos/soluções/textos com recomendação | critérios explícitos; estrutura paralela; conclusão |
| **Relatório** | relatar, explicar, recomendar | profissional, acadêmico, público | 3–3+ | relatório com diagnóstico e recomendação; relatório técnico | seções (contexto, dados, análise, recomendação); coesão global |
| **Artigo** | explicar, argumentar | público, cultural, especializado | 3–3+ | artigo de divulgação; artigo de opinião | tese/enfoque; desenvolvimento; fechamento; estilo autoral |
| **Texto argumentativo** | defender posição, argumentar | público, acadêmico | 3 | dissertação argumentativa com contra-argumento | tese, argumentos hierarquizados, refutação, conclusão |
| **Resenha** | resumir + avaliar | cultural, acadêmico | 3–3+ | resenha crítica de livro/filme/exposição | síntese + juízo fundamentado + recomendação |
| **Editorial** | argumentar, persuadir | público | 3+–4 | editorial sobre um tema controverso, em nome de uma publicação | voz institucional; posição clara; retórica controlada |
| **Ensaio** | argumentar, refletir | acadêmico, cultural, especializado | 3+–4+ | ensaio com tese autoral e diálogo com objeções | livre organização; profundidade; estilo |
| **Texto especializado** | explicar, argumentar em campo específico | especializado, acadêmico, profissional | 3+–5 | parecer técnico; nota técnica; artigo de área | terminologia de domínio; convenções da área; precisão |
| **Texto literário** | narrar, descrever, expressar | cultural, literário | 2+–5 (com fins didáticos desde 1+) | conto curto; crônica; poema com estrutura dada | recursos expressivos; ritmo; escolha estética |

### 9.3 Uso no produto — [PROPOSTA DE PRODUTO]

- Cada unidade declara **um gênero-alvo de produção**.
- Cada gênero tem uma **ficha de gênero** reutilizável (convenções, estrutura típica, marcas linguísticas, exemplos anotados, armadilhas comuns). A ficha é referenciada por todas as unidades daquele gênero — evita repetição e garante consistência.
- Filtro por gênero é **essencial no MVP** (ver seção 15).

---

## 10. Matriz de contextos (ETAPA 4)

### 10.1 Os oito contextos — [DECISÃO PEDAGÓGICA]

| # | Contexto | Definição de trabalho | Destinatários típicos |
|---|---|---|---|
| 1 | **Pessoal** | vida privada, família, amizades, identidade, rotina | você mesmo, amigos, familiares |
| 2 | **Cotidiano** | transações práticas do dia a dia | prestadores de serviço, comércio, vizinhos |
| 3 | **Social** | convívio, comunidade, associações, redes | grupos, colegas, comunidade |
| 4 | **Profissional** | trabalho, carreira, organização | colegas, chefia, clientes, fornecedores |
| 5 | **Acadêmico** | estudo, pesquisa, formação | professores, colegas de curso, banca, revistas |
| 6 | **Público** | vida cívica, direitos, serviços do Estado, debate público | órgãos públicos, imprensa, sociedade |
| 7 | **Cultural** | arte, memória, patrimônio, identidades, expressões | público de eventos, leitores, comunidades culturais |
| 8 | **Especializado** | domínios técnicos e profissionais específicos | pares de uma área, entidades técnicas |

### 10.2 Situações reais de comunicação por contexto — [PROPOSTA DE PRODUTO]

**1. Pessoal**
- apresentar-se por escrito; contar novidades; combinar um encontro; pedir desculpa; agradecer; manter um diário; descrever a própria trajetória; escrever uma mensagem de apoio.

**2. Cotidiano**
- deixar um bilhete; reclamar de um produto; pedir um orçamento; combinar com o síndico; escrever para um serviço de atendimento; avaliar um serviço; instruir alguém a fazer uma tarefa doméstica.

**3. Social**
- convidar para um evento; organizar uma vaquinha; escrever num grupo de moradores; propor uma ação comunitária; responder a um convite; redigir um comunicado de uma associação.

**4. Profissional**
- solicitar informação; responder a uma solicitação; apresentar um resultado; escrever um relatório; fazer uma recomendação; apresentar uma proposta; registrar uma ocorrência; encaminhar um problema; dar retorno a um cliente; escrever uma mensagem de desligamento ou boas-vindas.

**5. Acadêmico**
- escrever um resumo; resenhar um texto; sintetizar fontes; redigir uma justificativa de projeto; responder a uma questão dissertativa; escrever um e-mail a um professor/orientador; elaborar um argumento com referências.

**6. Público**
- escrever a um órgão público; registrar uma reclamação formal; assinar uma carta aberta; comentar uma consulta pública; escrever uma carta do leitor; explicar um direito a outra pessoa; produzir um texto de opinião sobre política pública.

**7. Cultural**
- resenhar uma obra ou exposição; descrever uma manifestação cultural; contar uma história de família ligada a um lugar; escrever um texto de divulgação sobre patrimônio; produzir uma crônica.

**8. Especializado**
- redigir um parecer técnico; escrever uma nota técnica; documentar um procedimento de área; produzir um artigo para pares; traduzir um conceito técnico para não especialistas.

### 10.3 Cruzamento contexto × nível — [DEC. PED.] / [HIPÓTESE A VALIDAR]

| Contexto | Predominância de níveis no piloto | Observação |
|---|---|---|
| Pessoal | 0+–2 | porta de entrada; alto volume de conteúdo básico |
| Cotidiano | 1–2+ | funcional; forte para português de acolhimento |
| Social | 1+–3 | transição do concreto ao argumentativo |
| Profissional | 2–3+ | núcleo de demanda de mercado `[HIPÓTESE A VALIDAR]` |
| Acadêmico | 2+–3+ | resumo, síntese, argumentação |
| Público | 2+–3+ | opinião, argumentação, cidadania |
| Cultural | 1+–3+ | editorial rico; conteúdo sobre o Brasil |
| Especializado | 3–5 | fase posterior; curadoria por área |

---

## 11. Matriz temática (ETAPA 5)

### 11.1 Princípio editorial — [PROPOSTA DE PRODUTO]

Os temas existem para **ensinar português por meio de conteúdo relevante**. Prioriza-se: (a) relevância cultural e cívica; (b) potencial de gerar tarefas de escrita autênticas em várias faixas de nível; (c) durabilidade (evitar excesso de conteúdo perecível); (d) diversidade de vozes e regiões do Brasil e do mundo lusófono.

### 11.2 Arquitetura hierárquica de temas

Estrutura em três níveis: **Eixo → Tema → Subtema**. Cada subtema deve render conteúdos em pelo menos duas faixas de nível.

#### Eixo A — BRASIL
- **A1. Cidades e territórios**: capitais e interior; periferias e centros; cidades históricas; planejamento urbano (ex.: Brasília); vida em cidade pequena.
- **A2. Regiões**: as cinco regiões; contrastes e estereótipos; migrações internas; identidades regionais.
- **A3. Cultura e expressões**: música (samba, forró, MPB, rap, sertanejo); literatura; cinema e novela; carnaval e festas populares; culturas indígenas; culturas afro-brasileiras.
- **A4. Alimentação**: comida regional; feira e mercado; comer fora; hábitos alimentares; comida e memória.
- **A5. Festas e calendário**: festas juninas, Círio, Bumba meu boi, Réveillon, festas religiosas e sincréticas; feriados e seus sentidos.
- **A6. Patrimônio e memória**: patrimônio material e imaterial; museus; lugares de memória; preservação e conflito.
- **A7. Diversidade**: povos indígenas; população negra; imigração histórica e recente; línguas do Brasil; regionalismos.
- **A8. História e presente**: períodos e marcos; memória da escravidão; redemocratização; desigualdade.

#### Eixo B — SOCIEDADE
- **B1. Trabalho**: mundo do trabalho; informalidade; trabalho remoto; direitos; carreiras; empreender.
- **B2. Educação**: escola pública e privada; universidade; educação de jovens e adultos; ensino de línguas.
- **B3. Mobilidade**: transporte público; trânsito; bicicleta; deslocamentos pendulares; acessibilidade urbana.
- **B4. Comunicação e mídia**: redes sociais; jornalismo; desinformação; privacidade.
- **B5. Comportamento e convívio**: etiqueta; conflitos de vizinhança; consumo; tempo livre.
- **B6. Vida urbana**: moradia; custo de vida; segurança; espaços públicos; gentrificação.
- **B7. Saúde e bem-estar**: sistema de saúde; saúde mental; alimentação e atividade física; envelhecimento.
- **B8. Direitos e cidadania**: serviços públicos; participação; justiça no cotidiano; direitos do consumidor.

#### Eixo C — CIÊNCIA E NATUREZA
- **C1. Amazônia**: floresta; povos; desmatamento; bioeconomia; rios.
- **C2. Cerrado e outros biomas**: Cerrado, Caatinga, Pantanal, Mata Atlântica, Pampa; serviços ecossistêmicos.
- **C3. Biodiversidade**: fauna e flora; espécies ameaçadas; unidades de conservação.
- **C4. Clima**: mudança climática; eventos extremos; energia; adaptação.
- **C5. Ciência e pesquisa**: como a ciência funciona; ciência brasileira; divulgação científica.
- **C6. Tecnologia**: digitalização; inteligência artificial no cotidiano; inclusão digital.
- **C7. Água e cidades**: saneamento; crise hídrica; rios urbanos.

#### Eixo D — COTIDIANO
- **D1. Casa**: morar; dividir apartamento; contas; consertos; vizinhança.
- **D2. Transporte**: pegar ônibus/metrô; aplicativos; viajar de avião; pedir informação de trajeto.
- **D3. Compras**: mercado; feira; compras online; trocas e devoluções; reclamações.
- **D4. Restaurante e bar**: pedir; reclamar; avaliar; reservar; dividir a conta.
- **D5. Viagens**: planejar; hospedar-se; imprevistos; contar a viagem.
- **D6. Serviços**: banco; telefonia; correios; cartório; serviços públicos digitais.
- **D7. Trabalho doméstico e cuidado**: rotina; combinação de tarefas; cuidado de crianças e idosos.

#### Eixo E — LÍNGUA
- **E1. Vocabulário**: campos semânticos; formação de palavras; falsos amigos (esp./ing. → port.).
- **E2. Expressões**: expressões idiomáticas; gírias e regionalismos; provérbios.
- **E3. Gramática em contexto**: tempos do passado; subjuntivo; regência; colocação pronominal — sempre a serviço de um gênero.
- **E4. Registro**: formal/informal; você/senhor; oralidade x escrita; linguagem inclusiva `[VALIDAR COM CONTRATANTE]` (política editorial).
- **E5. Escrita**: planejamento; parágrafo; coesão; revisão; pontuação.
- **E6. Pronúncia e ortografia**: relação som–grafia; acentuação; variação de pronúncia (apoio à escrita, não foco em fala).
- **E7. Variação**: português do Brasil x de Portugal x de África; variação social e regional.

### 11.3 Regras editoriais da matriz temática — [PROPOSTA DE PRODUTO]

1. Todo conteúdo tem **1 tema principal** e até **2 secundários**.
2. Cada subtema deve, ao final do piloto, ter conteúdo em **pelo menos 2 faixas de nível**.
3. Temas perecíveis (atualidade) recebem etiqueta de **revisão periódica** e data de referência.
4. Curadoria busca **equilíbrio regional** e **diversidade de vozes**.
5. Eixo E (Língua) nunca é ensinado isolado: sempre ancorado num gênero e num contexto.

### 11.4 Pontos para o contratante

- **[VALIDAR COM CONTRATANTE]** Priorização dos eixos para o piloto (sugestão: D + B + A).
- **[VALIDAR COM CONTRATANTE]** Política editorial sobre temas sensíveis (política partidária, religião, questões raciais e de gênero): abordagem, limites, processo de revisão.
- **[VALIDAR COM CONTRATANTE]** Uso de conteúdo de terceiros (notícias, imagens, obras): orçamento de licenciamento ou opção por conteúdo original/domínio público/Creative Commons.

---

## 12. Modelo de unidade pedagógica (ETAPA 6)

### 12.1 Estrutura padrão (18 componentes) — [PROPOSTA DE PRODUTO] + [DECISÃO PEDAGÓGICA]

| # | Componente | Descrição | Obrigatório |
|---|---|---|---|
| 1 | **Título** | nome editorial da unidade, orientado à capacidade | sim |
| 2 | **Introdução** | 2–4 frases situando o tema e a relevância; tom editorial | sim |
| 3 | **Nível** | faixa ILR Writing de referência da produção esperada | sim |
| 4 | **Objetivo** | o que o aluno vai conseguir fazer ao final (verbo observável) | sim |
| 5 | **Função comunicativa** | função principal (+ secundárias) | sim |
| 6 | **Contexto** | 1 dos 8 contextos | sim |
| 7 | **Gênero** | gênero-alvo de produção (referencia a ficha de gênero) | sim |
| 8 | **Conteúdo principal** | o material editorial: texto(s), áudio, imagem, infográfico — o "conteúdo de leitura/entrada" | sim |
| 9 | **Vocabulário** | 8–20 itens-chave com definição breve e exemplo; agrupados por campo | sim |
| 10 | **Estruturas linguísticas** | 2–4 estruturas a serviço da tarefa, com explicação curta e exemplos | sim |
| 11 | **Atividade de compreensão** | verifica entendimento do conteúdo principal | sim |
| 12 | **Atividade controlada** | prática guiada das estruturas/vocabulário (baixo risco) | sim |
| 13 | **Atividade de produção** | a tarefa de escrita, com enunciado, destinatário, extensão, contexto | sim |
| 14 | **Orientação para revisão** | checklist de autorrevisão para o aluno + roteiro de revisão por pares | sim |
| 15 | **Critérios de avaliação** | rubrica da unidade (derivada da rubrica geral, seção 18), ajustada ao gênero/nível | sim |
| 16 | **Material do aluno** | versão limpa, compartilhável/imprimível (conteúdo + atividades, sem gabarito) | sim |
| 17 | **Orientação para o professor** | como conduzir; tempo; agrupamentos; erros comuns; variações; gabarito; extensões | sim |
| 18 | **Materiais complementares** | leituras extras, modelos anotados, versões de nível adjacente, links | não |

**Metadados adicionais (não exibidos como seção, mas usados em busca/filtro):** tema(s); duração estimada; faixa etária; modalidade (individual / dupla / grupo / assíncrona); complexidade (baixa/média/alta); tipo de produção (curta / parágrafo / texto estruturado / texto longo); pré-requisitos sugeridos (opcionais); data de publicação e de última revisão; autoria; status editorial.

### 12.2 Princípios de design da unidade — [DECISÃO PEDAGÓGICA]

- **Um foco principal por unidade.** Uma função, um gênero, um objetivo de produção.
- **Entrada → prática → produção → revisão → avaliação.** Sequência estável, previsível para o professor.
- **Autossuficiência.** Sem pré-requisito obrigatório; pré-requisitos são apenas sugestões.
- **Tempo realista.** A unidade declara duração de uma aula típica (30, 45, 60, 90 min) e o que é possível fazer como tarefa assíncrona.
- **Reuso.** Fichas de gênero, listas de critérios e bancos de vocabulário são componentes referenciados, não recopiados.

### 12.3 Exemplo completo A — ILR 1 / 1+

> **1. Título:** "Um bilhete que resolve: avisar, pedir e combinar"
>
> **2. Introdução:** No dia a dia, a gente escreve bilhetes o tempo todo: para avisar que saiu, pedir um favor ao vizinho, combinar um horário. Um bilhete curto e claro evita mal-entendidos. Nesta unidade, você vai escrever bilhetes que a outra pessoa entende de primeira.
>
> **3. Nível:** ILR 1 / 1+ (referência). `[REF. OFICIAL]` nesta faixa o aluno escreve frases e bilhetes curtos e simples; erros são frequentes, mas a mensagem essencial passa em contextos previsíveis.
>
> **4. Objetivo:** Ao final, você vai conseguir escrever um bilhete de 3 a 5 frases para avisar algo, fazer um pedido simples e combinar um horário, com saudação e assinatura adequadas.
>
> **5. Função comunicativa:** informar / pedir / combinar (principais). Secundária: descrever brevemente uma situação.
>
> **6. Contexto:** cotidiano (vizinhança, casa).
>
> **7. Gênero:** bilhete (ver Ficha de Gênero "Bilhete").
>
> **8. Conteúdo principal:**
> Três bilhetes curtos, anotados:
> - *Bilhete 1 (aviso):* "Oi, Dona Marta. Saí para o mercado e volto às 11h. Se chegar uma encomenda, pode deixar com o porteiro. Obrigada! — Ana (ap. 32)"
> - *Bilhete 2 (pedido):* "Rafael, tudo bem? Você pode regar minhas plantas no sábado? Viajo sexta e volto domingo à noite. Deixo a chave com você hoje. Qualquer coisa, me manda mensagem. Abraço, Camila"
> - *Bilhete 3 (combinar):* "Seu João, podemos marcar o conserto da torneira para quinta de manhã, umas 9h? Se não puder, sugere outro horário. Estou no ap. 51. Obrigado! — Pedro"
> Anotações destacam: saudação, corpo (o quê + quando + o quê fazer), fecho, assinatura/identificação.
>
> **9. Vocabulário:** avisar; pedir um favor; combinar; marcar (um horário); encomenda/entrega; deixar (com alguém); qualquer coisa (= se precisar); porteiro; síndico; volto às ___ ; estou no ap. ___. Cada item com uma frase-exemplo.
>
> **10. Estruturas linguísticas:**
> - *Presente e futuro imediato para avisos:* "Saí…", "Volto às 11h", "Viajo sexta".
> - *Pedido educado com "poder" + infinitivo:* "Você pode regar as plantas?", "Podemos marcar para quinta?"
> - *Condicional simples com "se":* "Se chegar uma encomenda, pode deixar com o porteiro."
> - *Marcadores de tempo:* hoje, sábado, de manhã, às 9h, sexta, domingo à noite.
>
> **11. Atividade de compreensão:**
> a) Para cada bilhete, responda: quem escreve? para quem? qual é o pedido ou aviso? qual é o prazo/horário?
> b) Verdadeiro ou falso: "Camila volta no sábado." / "Pedro sugere quinta às 9h." / "Ana volta às 10h."
>
> **12. Atividade controlada:**
> a) Complete com "poder" no presente: "Você ____ me ajudar amanhã?"; "Nós ____ marcar para terça?"
> b) Reescreva como pedido educado: "Regue minhas plantas." → ____ ; "Me avise quando chegar." → ____
> c) Ordene as partes de um bilhete embaralhado (saudação, corpo, fecho, assinatura).
>
> **13. Atividade de produção (tarefa):**
> Escolha **uma** situação e escreva um bilhete de 3 a 5 frases:
> 1. Você vai sair e espera uma entrega. Peça a um vizinho para receber.
> 2. Você viaja no fim de semana. Peça a alguém para cuidar do seu gato.
> 3. Você precisa marcar com o síndico um horário para consertar algo no apartamento.
> Inclua: saudação, o aviso/pedido, o horário ou prazo, um fecho e sua identificação (nome e apartamento).
> Extensão: 3 a 5 frases. Destinatário: um vizinho / o síndico. Registro: educado e direto.
>
> **14. Orientação para revisão:**
> *Checklist do aluno:* Tem saudação? Está claro o que eu quero? Falei o horário ou o prazo? Tem fecho e meu nome? Reli em voz alta?
> *Revisão por pares:* Troque o bilhete com um colega. O colega marca: (1) uma coisa que entendeu bem; (2) uma coisa que ficou em dúvida; (3) uma frase que dava para deixar mais curta.
>
> **15. Critérios de avaliação (rubrica da unidade):**
> - *Funcionalidade:* o leitor entende o aviso/pedido e sabe o que fazer e quando. (peso maior)
> - *Adequação:* tem saudação, fecho e identificação; o tom é educado e apropriado a um vizinho.
> - *Conteúdo:* inclui todos os elementos pedidos (o quê, quando, identificação).
> - *Precisão:* frases simples compreensíveis; erros não impedem o entendimento; "poder + infinitivo" usado para o pedido.
> Escala sugerida por critério: *ainda não / quase lá / alcançado* (ver seção 18).
>
> **16. Material do aluno:** os três bilhetes anotados + vocabulário + estruturas + atividades 11 a 14 + checklist, sem gabarito, em formato limpo para tela e impressão.
>
> **17. Orientação para o professor:**
> - *Tempo:* 30–40 min em aula; produção pode ir para casa.
> - *Aquecimento:* pergunte quando foi a última vez que o aluno deixou ou recebeu um bilhete.
> - *Condução:* leia o bilhete 1 junto, identificando as partes; deixe o aluno analisar os bilhetes 2 e 3.
> - *Erros comuns:* omitir o horário/prazo; esquecer a identificação; usar registro alto demais ("venho por meio deste"); traduzir literal do idioma do aluno ("faça-me um favor de…").
> - *Gabarito:* 11a — B1: Ana→Dona Marta, aviso de saída + pedido sobre encomenda, volta 11h; B2: Camila→Rafael, regar plantas, sáb–dom; B3: Pedro→Seu João, marcar conserto, quinta 9h. 11b — F / V / F. 12a — "pode" / "podemos".
> - *Variações:* nível 1 — dê um modelo para completar; nível 1+ — peça um segundo bilhete respondendo ao primeiro.
> - *Extensão:* transformar o bilhete em mensagem de aplicativo e discutir o que muda no registro.
>
> **18. Materiais complementares:** ficha de gênero "Bilhete"; versão ILR 2 ("Recado profissional"); lista de fórmulas de saudação e fecho por registro.

### 12.4 Exemplo completo B — ILR 3

> **1. Título:** "Relatório com recomendação: do problema à proposta"
>
> **2. Introdução:** No trabalho, muitas decisões dependem de um bom relatório: alguém identifica um problema, analisa e recomenda um caminho. Um relatório eficaz é objetivo, mostra o raciocínio e termina com uma recomendação clara e viável. Nesta unidade, você vai escrever um relatório curto que sustenta uma recomendação.
>
> **3. Nível:** ILR 3 (referência). `[REF. OFICIAL]` nesta faixa o aluno escreve com precisão suficiente sobre temas profissionais, explica questões, defende posições e produz textos coesos, incluindo relatórios; erros esporádicos em estruturas complexas não comprometem a comunicação.
>
> **4. Objetivo:** Ao final, você vai conseguir redigir um relatório de 350–500 palavras que apresenta um problema de trabalho, analisa causas e evidências e sustenta uma recomendação, com estrutura em seções e coesão global.
>
> **5. Função comunicativa:** relatar + explicar + recomendar (principais). Secundária: comparar alternativas.
>
> **6. Contexto:** profissional.
>
> **7. Gênero:** relatório (ver Ficha de Gênero "Relatório").
>
> **8. Conteúdo principal:**
> - Um **caso** (cerca de 250 palavras): uma equipe de atendimento com aumento de reclamações sobre prazos; dados fornecidos (volume de chamados por mês, tempo médio de resposta, taxa de rechamada, número de atendentes, sazonalidade).
> - Um **relatório-modelo anotado** (400 palavras) sobre um caso análogo (fila de uma unidade de saúde), com marcações das seções: *Contexto e objetivo · Método/fontes · Achados · Análise · Recomendação · Próximos passos*.
> - Um **quadro de conectivos** de causa, consequência, concessão e conclusão, com exemplos.
>
> **9. Vocabulário:** gargalo; demanda x capacidade; indicador; tendência; sazonalidade; hipótese; evidência; causa raiz; trade-off; viabilidade; priorizar; mitigar; escalonar; prazo (SLA); rechamada; retrabalho; a curto/médio/longo prazo. Com exemplos de uso em frase de relatório.
>
> **10. Estruturas linguísticas:**
> - *Nominalização para objetividade:* "houve um aumento das reclamações" / "o aumento das reclamações decorre de…".
> - *Orações causais e consecutivas:* "uma vez que…", "de modo que…", "o que resultou em…".
> - *Concessão para reconhecer limites:* "embora os dados sejam parciais, …", "ainda que a contratação resolva o pico, …".
> - *Modalização da recomendação:* "recomenda-se", "seria conveniente", "a alternativa mais viável parece ser…".
> - *Coesão referencial:* uso de "esse", "tal", "a medida", "essa alternativa" para retomar sem repetir.
>
> **11. Atividade de compreensão:**
> a) A partir dos dados do caso, identifique: qual é o problema em uma frase? quais dados sustentam que ele existe? qual dado sugere sazonalidade?
> b) No relatório-modelo, sublinhe a frase que expressa a recomendação e as duas frases que a sustentam.
> c) Distinga, no modelo, o que é *achado* (fato) do que é *análise* (interpretação).
>
> **12. Atividade controlada:**
> a) Reescreva com nominalização: "As respostas atrasaram e por isso os clientes ligaram de novo." → ____
> b) Complete com conector adequado (causa, consequência, concessão): "____ a equipe esteja no limite, contratar sem rever processos apenas adia o problema."
> c) Transforme em recomendação modalizada: "Contrate dois atendentes." → ____
> d) Ordene as seções de um relatório desmontado.
>
> **13. Atividade de produção (tarefa):**
> Com base nos dados do caso, escreva um **relatório de 350–500 palavras** dirigido à coordenação da área, com as seções: *Contexto e objetivo · Achados · Análise (causas prováveis) · Recomendação (uma principal + uma alternativa) · Próximos passos e riscos*.
> Requisitos: usar pelo menos três dados do caso; apresentar uma causa raiz; reconhecer uma limitação (concessão); terminar com recomendação clara e viável.
> Destinatário: coordenação (não conhece os detalhes operacionais). Registro: profissional, objetivo, impessoal.
>
> **14. Orientação para revisão:**
> *Checklist do aluno:* O problema está em uma frase logo no início? Cada afirmação de análise se apoia em um dado? A recomendação é específica e viável? Eu reconheci alguma limitação? Há conclusão? Cortei repetições e frases longas demais? O registro é impessoal e consistente?
> *Revisão por pares:* o colega marca: (1) a recomendação está clara? (2) a análise decorre dos achados ou há salto lógico? (3) algum trecho é opinião sem evidência? (4) dois pontos onde a coesão pode melhorar.
>
> **15. Critérios de avaliação (rubrica da unidade):**
> - *Funcionalidade:* o relatório cumpre sua função — a coordenação entende o problema e tem uma recomendação acionável. Estrutura em seções presente e funcional.
> - *Conteúdo:* uso pertinente dos dados; análise com causa raiz; alternativa considerada; limitação reconhecida; recomendação viável.
> - *Precisão:* controle de período composto, nominalização e conectivos; erros esporádicos em estruturas complexas são tolerados se não perturbam a leitura.
> - *Adequação:* registro profissional e impessoal sustentado; convenções do gênero relatório respeitadas; texto ajustado a um leitor que não conhece a operação.
> Escala por critério: *ainda não / quase lá / alcançado / consolidado* (ver seção 18).
>
> **16. Material do aluno:** caso + dados + relatório-modelo anotado + quadro de conectivos + atividades 11 a 14 + checklists, sem gabarito.
>
> **17. Orientação para o professor:**
> - *Tempo:* 60–90 min (1–2 aulas); produção assíncrona recomendada, revisão por pares na aula seguinte.
> - *Condução:* comece pela leitura crítica do relatório-modelo (o que funciona? o que cortaria?); depois trabalhe os dados do caso coletivamente para extrair o problema; só então a escrita individual.
> - *Erros comuns:* misturar achado e opinião; recomendação genérica ("melhorar o processo"); ausência de limitação; excesso de subordinação que quebra a clareza; registro que oscila entre impessoal e coloquial; introdução longa sem enunciar o problema.
> - *Gabarito (chave):* 11a — problema: o tempo médio de resposta cresceu e elevou a taxa de rechamada; sazonalidade sugerida pelo pico em meses específicos. 12a — "O atraso nas respostas gerou novo contato dos clientes." 12b — "Embora". 12c — "Recomenda-se avaliar a contratação de dois atendentes, condicionada à revisão do fluxo de triagem."
> - *Variações:* ILR 2+ — fornecer um roteiro de seções mais detalhado e reduzir a exigência de refutação; ILR 3+ — pedir análise de trade-off entre duas recomendações e uma projeção de impacto.
> - *Extensão:* transformar a recomendação do relatório em um e-mail executivo de 120 palavras para a diretoria.
>
> **18. Materiais complementares:** ficha de gênero "Relatório"; unidade "E-mail executivo: pedir decisão em 120 palavras" (ILR 3); banco de conectivos argumentativos; modelo de sumário executivo.

---

## 13. Arquitetura de informação (ETAPA 7)

### 13.1 Princípios — [PROPOSTA DE PRODUTO]

- **Dois modos de uso, uma biblioteca.** Aluno e Professor veem a mesma coleção de conteúdos, com navegação e ferramentas diferentes.
- **Entrada por múltiplos caminhos:** por nível, por tema, por função, por gênero, por contexto, por busca livre. Nenhum caminho é "o" caminho.
- **Conteúdo no centro.** A página de conteúdo é o destino; tudo converge para ela.
- **Profundidade rasa.** Máximo de 3 cliques da home a qualquer unidade.

### 13.2 Estrutura de topo

```
Home
├── Explorar (entrada editorial: destaques, coleções temáticas, novidades)
├── Níveis (0+ … 3/3+ no piloto)
│   └── página de nível → conteúdos + explicação do que se faz nesse nível
├── Temas (Eixo → Tema → Subtema)
│   └── página de subtema → conteúdos
├── Funções comunicativas
│   └── página de função → conteúdos + progressão da função entre níveis
├── Gêneros
│   └── página de gênero → ficha de gênero + conteúdos
├── Contextos
│   └── página de contexto → situações + conteúdos
├── Buscar (busca livre + filtros)
└── Área do Professor  [requer login no MVP]
    ├── Biblioteca (mesma coleção, com ações de professor)
    ├── Minhas coleções
    ├── Planejar aula
    ├── Materiais para download
    └── Avaliação (rubrica e guias)
```

### 13.3 Navegação do ALUNO

| Item | Conteúdo da página | Ações |
|---|---|---|
| **Explorar** | destaques editoriais, coleções ("Escrever no trabalho", "Português para o dia a dia"), novidades | abrir conteúdo, abrir coleção |
| **Níveis** | lista de níveis; cada nível tem uma página explicando *o que você já consegue fazer* e *o que vem a seguir*, + conteúdos | filtrar por tema/gênero dentro do nível |
| **Temas** | árvore Eixo → Tema → Subtema; página de subtema com conteúdos e um texto de abertura | filtrar por nível/gênero |
| **Atividades** | conteúdos com foco em prática (compreensão + controlada) e tarefas de produção | filtrar por tipo de atividade, nível |
| **Produção** | tarefas de escrita organizadas por gênero e nível; cada tarefa liga à unidade de origem e aos critérios | abrir tarefa, ver critérios, baixar material do aluno |
| **Progresso** | **[VERSÃO MÍNIMA NO MVP — [VALIDAR COM CONTRATANTE]]** sem conta de aluno, "progresso" = histórico local do navegador (o que já abriu/marcou). Progresso real com conta = Fase 3 |

### 13.4 Navegação do PROFESSOR

| Item | Conteúdo da página | Ações |
|---|---|---|
| **Biblioteca** | toda a coleção, visão de professor (mostra metadados pedagógicos completos, material do professor, gabarito) | filtrar, buscar, abrir, "Usar em aula", adicionar à coleção, baixar |
| **Buscar materiais** | busca livre + todos os filtros; busca combinada tipo "ILR 2 + trabalho + e-mail + 30 min" | salvar busca; ver resultados com cartão detalhado |
| **Planejar aula** | monta uma sequência: arrasta 1–4 unidades/atividades, define ordem e tempo, adiciona notas próprias, gera um roteiro de aula (visualização + download) | salvar plano; duplicar; exportar PDF; compartilhar link `[VALIDAR COM CONTRATANTE]` |
| **Minhas coleções** | pastas do professor com conteúdos salvos; coleções podem ser privadas ou (Fase 3) compartilhadas | criar/renomear/excluir coleção; mover itens |
| **Atividades** | as atividades destacadas das unidades, filtráveis, para uso avulso | abrir, baixar, adicionar ao plano |
| **Materiais para download** | central de arquivos: material do aluno (PDF), material do professor (PDF com gabarito), fichas de gênero, rubricas | baixar individual ou em lote (por plano/coleção) |
| **Avaliação** | rubrica geral, rubricas por gênero, guia de uso, exemplos de textos comentados por nível | abrir, baixar, imprimir |

### 13.5 Página de conteúdo (unidade) — layout conceitual

**[PROPOSTA DE PRODUTO]**

```
[Cabeçalho editorial]
  Título · Introdução
  Barra de metadados: Nível ILR · Função · Gênero · Contexto · Tema · Duração · Tipo de produção
  Ações (professor): [Usar em aula] [Salvar em coleção] [Baixar materiais]
  Ações (aluno): [Baixar material do aluno] [Ver critérios]

[Corpo — leitura editorial]
  8. Conteúdo principal (texto/mídia, tipografia de publicação, tempo de leitura)
  9. Vocabulário (bloco lateral ou ao fim da seção)
  10. Estruturas linguísticas

[Atividades] (abas ou seções)
  11. Compreensão
  12. Prática controlada
  13. Produção (tarefa) — com enunciado, destinatário, extensão
  14. Orientação para revisão (checklist do aluno + revisão por pares)

[Avaliação]
  15. Critérios (rubrica da unidade)

[Rodapé da unidade]
  17. Orientação para o professor (colapsável; visível só no modo professor OU sob aviso)
  18. Materiais complementares · unidades relacionadas (mesmo gênero, nível adjacente)
```

O **modo professor** (logado) revela: gabaritos, orientação para o professor, metadados completos, ações de planejamento. O **modo aluno / visitante** vê conteúdo, atividades sem gabarito, critérios e material do aluno.

### 13.6 Página de atividade (uso avulso)

Enunciado · contexto e destinatário · tempo · nível · vínculo com a unidade de origem · (professor) gabarito e notas · botões: adicionar ao plano, baixar, abrir unidade completa.

### 13.7 Área do professor — requisitos de acesso

- **[DECISÃO DE PRODUTO]** No MVP, criar coleções, planos e salvar buscas exige **conta de professor** (e-mail + senha, ou login social). Navegar e ver conteúdo **não** exige login. **[VALIDAR COM CONTRATANTE]**: conteúdo é totalmente aberto, parcialmente aberto (amostra) ou fechado atrás de login/assinatura?

---

## 14. Sistema de navegação (ETAPA 7, complemento)

### 14.1 Menu principal — [PROPOSTA DE PRODUTO]

**Barra superior (persistente):**
`Explorar · Níveis · Temas · Funções · Gêneros · Contextos · Buscar` + alternância `Aluno / Professor` + `Entrar`.

Na área do professor, a barra passa a:
`Biblioteca · Buscar · Planejar aula · Minhas coleções · Downloads · Avaliação` + `Explorar`.

### 14.2 Categorias e subcategorias

- **Níveis:** 0+ · 1 · 1+ · 2 · 2+ · 3 · 3+  (piloto). Cada um com página-explicação.
- **Temas:** 5 eixos → ~35 temas → ~120 subtemas (arquitetura da seção 11).
- **Funções:** 18 funções (seção 8), cada uma com página de progressão.
- **Gêneros:** 20 gêneros (seção 9), cada um com ficha.
- **Contextos:** 8 contextos (seção 10).

### 14.3 Padrões de navegação

- **Breadcrumbs** em todas as páginas internas (ex.: Temas › Brasil › Alimentação › Comida regional).
- **Navegação facetada**: a partir de qualquer página de categoria, aplicar filtros adicionais sem sair.
- **Conteúdos relacionados** ao pé de cada unidade: mesmo gênero em nível adjacente; mesma função em outro contexto; mesmo tema em outro nível.
- **"Continuar de onde parei"** (histórico local no MVP).
- **Estado vazio** informativo: quando um filtro não retorna nada, sugerir afrouxar um critério específico.

### 14.4 Navegação móvel

- Menu recolhido; busca com destaque; filtros em painel deslizante; cartões de conteúdo empilhados; leitura da unidade otimizada para coluna única. Ações de professor acessíveis, mas o **planejamento de aula é priorizado para desktop** no MVP. `[HIPÓTESE A VALIDAR]`

---

## 15. Sistema de filtros (ETAPA 8)

### 15.1 Inventário de filtros

| Filtro | Valores | MVP? | Observação |
|---|---|---|---|
| **Nível ILR** | 0+, 1, 1+, 2, 2+, 3, 3+ (multi-seleção; opção "faixa") | **Essencial** | filtro âncora |
| **Função comunicativa** | 18 valores (seção 8) | **Essencial** | eixo central do produto |
| **Gênero** | 20 valores (seção 9) | **Essencial** | |
| **Contexto** | 8 valores (seção 10) | **Essencial** | |
| **Tema** | eixo / tema / subtema | **Essencial** (ao menos eixo+tema) | subtema pode entrar iterativamente |
| **Duração** | ≤15, ~30, ~45, ~60, 90+ min | **Essencial** | critério prático decisivo para o professor |
| **Tipo de material** | conteúdo completo, atividade avulsa, ficha de gênero, rubrica, modelo anotado | **Essencial** | |
| **Habilidade** | escrita (foco); compreensão de leitura; vocabulário; (fala/escuta se houver) | Desejável | no piloto quase tudo é "escrita"; ganha valor com o catálogo |
| **Tipo de produção** | palavra/frase, parágrafo, texto estruturado, texto longo | Desejável | ajuda a calibrar esforço |
| **Complexidade** | baixa, média, alta | Desejável | subjetivo; precisa de critério editorial |
| **Faixa etária** | adolescentes, adultos, todos | Desejável | maioria "adultos" no piloto |
| **Modalidade** | individual, dupla, grupo, assíncrona | Desejável | |
| **Idioma de apoio / L1 do aluno** | — | Fase 2+ | só se houver glossários/notas contrastivas |
| **Data / atualidade** | recentes, perenes | Fase 2 | para temas perecíveis |
| **Licença / uso** | livre para impressão, uso em sala, etc. | Fase 2 | relevante se houver conteúdo de terceiros |

### 15.2 Filtros essenciais do MVP (resumo)

**Nível ILR · Função · Gênero · Contexto · Tema (eixo+tema) · Duração · Tipo de material.**

Esses sete permitem a busca-alvo do professor descrita na Etapa 9 ("ILR 2 + trabalho + e-mail + 30 min").

### 15.3 Comportamento dos filtros — [PROPOSTA DE PRODUTO]

- **Combináveis** (AND entre filtros, OR dentro do mesmo filtro).
- **Contadores** ao lado de cada valor (quantos conteúdos existem).
- **Filtros ativos** visíveis como "chips" removíveis.
- **URL compartilhável** com o estado dos filtros (bom para o professor salvar/enviar).
- **Ordenação** dos resultados: relevância, mais recentes, menor duração, nível crescente.
- **Busca salva** (professor logado).

### 15.4 Segunda fase

Habilidade detalhada, tipo de produção, complexidade, faixa etária, modalidade, L1 de apoio, atualidade, licença, e **filtros derivados de uso** ("mais usados por professores", "bem avaliados").

---

## 16. Experiência do professor (ETAPA 9)

### 16.1 Cenário-base

O professor tem uma aula em 1 hora com um aluno de nível intermediário que trabalha numa empresa e precisa escrever e-mails em português. Ele quer material para ~30 minutos da aula.

### 16.2 Fluxo

1. **Entra** na Área do Professor → **Buscar materiais**.
2. **Monta a busca:** Nível `ILR 2` · Contexto `Profissional` · Gênero `E-mail profissional` · Duração `~30 min`.
3. **Resultados:** lista de cartões. Cada **cartão de conteúdo** mostra:
   - Título
   - Nível ILR
   - Objetivo (1 linha)
   - Duração
   - Habilidades / função
   - Tipo de produção (ex.: "e-mail de 6–10 linhas")
   - Materiais disponíveis (ícones: material do aluno PDF, material do professor PDF, ficha de gênero, rubrica)
   - Tema
   - (opcional) nota de utilidade de outros professores
4. **Abre um conteúdo.** Vê a unidade completa em modo professor: conteúdo principal, vocabulário, estruturas, as três atividades, orientação para revisão, critérios, orientação para o professor com gabarito.
5. **Decide usar.** Clica em **"Usar em aula"**.

### 16.3 O que acontece ao clicar em "Usar em aula" — [PROPOSTA DE PRODUTO]

Abre um painel "Sessão de aula" com:

- **Resumo da unidade** (título, nível, objetivo, duração).
- **Seleção de componentes:** o professor marca o que vai usar (ex.: conteúdo principal + atividade de compreensão + tarefa de produção; deixa de fora a atividade controlada).
- **Ordem e tempo:** ajusta a sequência e o tempo de cada parte; o painel soma o tempo total.
- **Modo de apresentação:** gera uma **visão de aula** limpa (para compartilhar tela) — só o conteúdo do aluno, um componente por vez, navegação simples.
- **Material do aluno:** botão para baixar/enviar o PDF do aluno (só os componentes escolhidos) ou gerar um **link** para o aluno `[VALIDAR COM CONTRATANTE]`.
- **Material do professor:** roteiro com gabarito e notas, para o professor ter ao lado.
- **Salvar:** a sessão vira um item em **"Planejar aula"** / **"Minhas coleções"**, reutilizável e duplicável.
- **Registrar uso** (opcional): marca a unidade como "usada em (data)" no histórico do professor — alimenta "conteúdos que já usei" e métricas de utilidade.

Nenhuma dessas ações envolve conta de aluno, turma ou nota. É uma ferramenta de **preparação e condução**, não de gestão.

### 16.4 Outros fluxos do professor

- **Planejar uma aula do zero:** vai a "Planejar aula", cria um plano, busca e arrasta 2–3 unidades/atividades, adiciona notas, exporta.
- **Montar uma coleção temática** ("E-mails no trabalho — ILR 2 a 3") para reusar com vários alunos.
- **Baixar um pacote** (todos os PDFs de uma coleção) para uso offline.
- **Encontrar a rubrica** e um exemplo de texto comentado para dar devolutiva ao aluno.
- **Salvar uma busca** frequente ("ILR 1+ / cotidiano / ≤30 min").

### 16.5 Requisitos de UX derivados

- Cartões de resultado ricos e escaneáveis (decisão em segundos).
- Pré-visualização rápida sem sair da lista.
- "Usar em aula" acessível a partir do cartão **e** da página da unidade.
- Geração de PDF fiel ao conteúdo (tipografia, sem elementos de navegação).
- Tudo que o professor cria é **editável e duplicável**.
- Estados vazios que ensinam a afrouxar filtros.

---

## 17. Experiência do aluno (ETAPA 7/13, complemento)

### 17.1 Como o aluno chega

- Por **link direto** enviado pelo professor (unidade, atividade ou material do aluno).
- Por **navegação livre** (Explorar, Temas, Níveis, Produção).

### 17.2 O que o aluno vê

- Conteúdo principal com **qualidade de leitura editorial** (tipografia, imagem, tempo de leitura).
- Vocabulário e estruturas de forma consultável.
- Atividades **sem gabarito**; produção com enunciado, destinatário e extensão claros.
- **Critérios de avaliação** antes de produzir ("o que se espera de mim").
- Checklist de autorrevisão e roteiro de revisão por pares.
- Botão para **baixar o material do aluno**.

### 17.3 O que o aluno NÃO tem no MVP

- Conta, perfil, histórico persistente entre dispositivos.
- Envio de produção pela plataforma / correção.
- Trilha, metas, gamificação.
- "Progresso" real (fica como histórico local do navegador; progresso com conta = Fase 3).

### 17.4 Princípios de UX para o aluno

- Uma unidade = uma página coerente; leitura primeiro, atividades depois.
- Linguagem de interface simples (o aluno pode ter proficiência baixa).
- Acessibilidade: contraste, tamanho de fonte ajustável, alternativa textual a mídia, navegação por teclado.
- Nada que dependa de o aluno "entender a ILR": o nível aparece de forma discreta; o que importa é o objetivo em linguagem clara ("você vai conseguir escrever…").

---

## 18. Modelo de avaliação (ETAPA 10)

### 18.1 Base — [REF. OFICIAL] + [DECISÃO PEDAGÓGICA]

A rubrica usa as **quatro dimensões da ILR** como eixos: **funcionalidade, precisão, conteúdo, adequação**. **Não** é uma cópia da escala oficial: é uma **ferramenta operacional** para o professor dar uma devolutiva rápida e consistente sobre uma produção escrita, dentro do nível-alvo da unidade.

### 18.2 Rubrica geral de produção escrita — [PROPOSTA DE PRODUTO]

Cada dimensão é avaliada **em relação ao nível-alvo da tarefa** (não em termos absolutos) numa escala de 4 pontos:

**Escala:** `1 — ainda não` · `2 — quase lá` · `3 — alcançado` · `4 — consolidado`
(*"alcançado" = cumpre o esperado para o nível-alvo da unidade.*)

| Dimensão | Pergunta-guia | 1 — ainda não | 2 — quase lá | 3 — alcançado | 4 — consolidado |
|---|---|---|---|---|---|
| **Funcionalidade** | O texto cumpre a tarefa? O leitor consegue fazer o que precisa com ele? | a tarefa não se cumpre; o leitor não entende o propósito ou não pode agir | cumpre em parte; exige esforço ou releitura do leitor | cumpre a tarefa de forma clara para o destinatário previsto | cumpre com eficácia; antecipa dúvidas do leitor; escolhas eficientes |
| **Precisão** | A língua está correta e adequada em amplitude e complexidade para o nível-alvo? | erros impedem a compreensão de partes centrais | erros frequentes em estruturas esperadas para o nível, mas o sentido se recupera | erros esporádicos, sobretudo em estruturas além do nível-alvo; não perturbam | controle amplo; erros raros; variação de estruturas apropriada |
| **Conteúdo** | As ideias são pertinentes, suficientes e bem desenvolvidas para a tarefa? | conteúdo insuficiente, fora do tema ou incompreensível | ideias pertinentes, mas pouco desenvolvidas ou incompletas | conteúdo suficiente e pertinente; desenvolvimento adequado à tarefa | conteúdo rico, bem selecionado e articulado; profundidade apropriada |
| **Adequação** | O registro, o gênero e o ajuste ao destinatário estão corretos? | registro/gênero inadequados; texto não reconhecível como o gênero pedido | convenções do gênero parcialmente atendidas; registro oscila | gênero reconhecível; registro adequado e majoritariamente consistente; ajuste ao destinatário | domínio das convenções; registro preciso e consistente; ajuste fino ao destinatário e ao propósito |

### 18.3 Regras de uso — [DECISÃO PEDAGÓGICA]

- **Avaliar sempre contra o nível-alvo da unidade.** Um texto ILR 2 não é penalizado por não ter sofisticação de ILR 3.
- **Peso configurável.** Cada unidade indica a dimensão de maior peso (ex.: no bilhete ILR 1, peso maior em *funcionalidade* e *adequação*; no relatório ILR 3, em *conteúdo* e *funcionalidade*).
- **Devolutiva, não nota.** A saída padrão é qualitativa (os quatro níveis + comentário). Uma pontuação numérica é opcional e local.
- **Foco em 1–2 prioridades.** O professor escolhe, junto com o aluno, uma ou duas dimensões para trabalhar na próxima produção.

### 18.4 Instrumentos que a plataforma oferece

1. **Rubrica geral** (acima), em versão para tela, impressão e preenchimento.
2. **Rubricas por gênero** — a rubrica geral especificada para bilhete, e-mail, relato, resumo, texto argumentativo, relatório etc. (descritores concretos por dimensão).
3. **Rubrica da unidade** — instância curta dentro de cada unidade (componente 15), já ajustada ao nível e ao gênero.
4. **Exemplos comentados** — para cada faixa de nível, 1–2 produções reais anotadas nas quatro dimensões (banco crescente).
5. **Checklist de autorrevisão do aluno** e **roteiro de revisão por pares** (componente 14 das unidades).
6. **Guia rápido de devolutiva** — como dar retorno em 5 minutos: 1 elogio específico, 1 prioridade, 1 ação concreta.

### 18.5 O que a rubrica não é

- Não é um teste de nivelamento (não classifica o aluno na ILR).
- Não é correção automática.
- Não substitui o julgamento do professor; organiza-o.

---

## 19. Arquitetura conceitual dos conteúdos (ETAPA 11)

### 19.1 Entidades principais (modelo conceitual — sem implementação)

| Entidade | Descrição | Atributos-chave (conceituais) |
|---|---|---|
| **Conteúdo / Unidade** | a unidade pedagógica (seção 12) | título, introdução, objetivo, status editorial, duração, complexidade, tipo de produção, datas, autoria |
| **Nível** | faixa ILR Writing de referência | código (0+…5), descrição pedagógica, "o que se faz", "o que vem a seguir" |
| **Função comunicativa** | o que o texto faz | nome, definição, progressão entre níveis |
| **Gênero** | tipo de texto a produzir | nome, ficha de gênero (convenções, estrutura, marcas linguísticas, armadilhas) |
| **Contexto** | esfera de uso | nome (1 de 8), definição, situações típicas |
| **Tema** | assunto editorial | eixo, tema, subtema, texto de abertura, política de revisão, data de referência |
| **Atividade** | tarefa dentro ou fora de uma unidade | tipo (compreensão / controlada / produção / revisão), enunciado, destinatário, extensão, tempo, gabarito |
| **Vocabulário (Item lexical / Conjunto)** | itens-chave | termo, definição breve, exemplo, campo semântico; agrupável em conjuntos reutilizáveis |
| **Estrutura linguística** | recurso gramatical/discursivo a serviço da tarefa | nome, explicação curta, exemplos, funções que serve |
| **Mídia** | texto de leitura, áudio, imagem, infográfico | tipo, arquivo/fonte, crédito, licença, transcrição/alt |
| **Material do professor** | versão com orientação e gabarito | conteúdo, arquivo PDF derivado |
| **Material do aluno** | versão limpa compartilhável | conteúdo, arquivo PDF derivado |
| **Avaliação / Rubrica** | instrumento de avaliação | dimensões (4), descritores por nível, pesos, vínculo com gênero e/ou unidade |
| **Exemplo comentado** | produção anotada | texto, anotações por dimensão, nível |
| **Coleção** | agrupamento feito por editor ou por professor | nome, descrição, tipo (editorial / do professor), itens, visibilidade |
| **Plano de aula / Sessão** | sequência montada pelo professor | itens selecionados, ordem, tempos, notas, exportações |
| **Professor (Usuário)** | conta de professor | identificação, coleções, planos, buscas salvas, histórico de uso |
| **Ficha de gênero** | documento reutilizável por gênero | (ver Gênero) |

### 19.2 Relacionamentos (conceituais)

- **Conteúdo** *tem referência de* **1 Nível** (e pode indicar faixa entre dois).
- **Conteúdo** *realiza* **1 Função principal** e *0..n Funções secundárias*.
- **Conteúdo** *tem como alvo de produção* **1 Gênero**.
- **Conteúdo** *situa-se em* **1 Contexto**.
- **Conteúdo** *aborda* **1 Tema principal** e *0..2 Temas secundários*.
- **Conteúdo** *contém* **1..n Atividades** (1 de compreensão, 1 controlada, 1 de produção, 1 de revisão — mínimo).
- **Conteúdo** *inclui* **1 Conjunto de vocabulário** e *1..n Estruturas linguísticas*.
- **Conteúdo** *usa* **1..n Mídias**.
- **Conteúdo** *gera* **1 Material do aluno** e **1 Material do professor**.
- **Conteúdo** *é avaliado por* **1 Rubrica de unidade**, *derivada de* **1 Rubrica de gênero**, *derivada da* **Rubrica geral**.
- **Gênero** *tem* **1 Ficha de gênero** e *pode ter* **1 Rubrica de gênero**.
- **Função** *tem* **1 descrição de progressão** que *atravessa* **vários Níveis**.
- **Atividade** *pode existir* isolada (uso avulso) *ou* *pertencer a* **1 Conteúdo**.
- **Coleção** *agrupa* **0..n Conteúdos e/ou Atividades**; *pertence a* **1 Editor** ou **1 Professor**.
- **Plano de aula** *referencia* **1..n Conteúdos/Atividades**; *pertence a* **1 Professor**.
- **Professor** *cria* **0..n Coleções, Planos, Buscas salvas**; *registra* **histórico de uso** de Conteúdos.
- **Exemplo comentado** *ilustra* **1 Nível** e *pode vincular-se a* **1 Gênero**.
- **Vocabulário** e **Estrutura** *podem ser reutilizados* por vários Conteúdos (biblioteca compartilhada).

### 19.3 Diagrama textual (visão simplificada)

```
                 ┌────────── Nível
                 │
Tema ───────────►│           Função ──── progressão ──► (Níveis)
                 │            │
Contexto ───────►│  CONTEÚDO ─┼─► Gênero ──► Ficha de gênero
                 │  (Unidade) │         └──► Rubrica de gênero ──► Rubrica geral
Mídia ──────────►│            │
                 │            ├─► Atividades (compreensão / controlada / produção / revisão)
                 │            ├─► Vocabulário (conjunto reutilizável)
                 │            ├─► Estruturas linguísticas (reutilizáveis)
                 │            ├─► Material do aluno (PDF)   Material do professor (PDF)
                 │            └─► Rubrica da unidade
                 │
   Coleção ◄─────┴─────► Plano de aula ◄──── Professor ────► Buscas salvas / Histórico
        ▲                                        
        └──── Editorial (curadoria)              Exemplo comentado ──► Nível / Gênero
```

### 19.4 Observações — [DECISÃO PEDAGÓGICA]

- O modelo é **conceitual**. A implementação (tabelas, chaves, JSON, relações no PostgreSQL/Supabase) é objeto da Fase 2.
- **Reuso** é um princípio: fichas de gênero, rubricas, conjuntos de vocabulário e estruturas não são recopiados em cada unidade.
- **Versionamento editorial**: cada Conteúdo tem status (rascunho, em revisão, publicado, em atualização, arquivado) e histórico de revisão.

---

## 20. Escopo do MVP (ETAPA 12)

### 20.1 Pergunta que o MVP responde

> Qual é a menor versão desta plataforma que já entrega valor real ao professor?

**[PROPOSTA DE PRODUTO]** Resposta: **uma biblioteca pesquisável de ~40–60 unidades pedagógicas completas, com filtros essenciais, material do aluno e do professor para download, rubrica de avaliação, e uma área do professor mínima com coleções e "Usar em aula".** Sem IA. Sem conta de aluno. Sem turmas.

### 20.2 Funcionalidades obrigatórias (MVP)

**Conteúdo e navegação**
- Catálogo de unidades no modelo da seção 12 (18 componentes).
- Páginas de: Explorar, Nível, Tema (eixo+tema+subtema), Função, Gênero, Contexto.
- Página de conteúdo (unidade) com modo aluno e modo professor.
- Página de atividade avulsa.
- Fichas de gênero para os gêneros do piloto.

**Busca e filtros**
- Busca livre (texto).
- Filtros essenciais: Nível ILR, Função, Gênero, Contexto, Tema, Duração, Tipo de material.
- Resultados em cartões ricos; ordenação; filtros ativos como chips; URL compartilhável.

**Área do professor**
- Conta de professor (e-mail/senha ou login social — via Supabase Auth).
- Minhas coleções (criar, adicionar, organizar).
- "Usar em aula": seleção de componentes, ordem/tempo, visão de apresentação, geração de material do aluno.
- Planejar aula: sequência simples de 1–4 itens com notas e exportação PDF.
- Downloads: material do aluno (PDF), material do professor (PDF), fichas de gênero, rubricas.
- Buscas salvas.

**Avaliação**
- Rubrica geral + rubricas por gênero (para os gêneros do piloto) + rubrica em cada unidade.
- Guia rápido de devolutiva.
- 1–2 exemplos comentados por faixa de nível coberta.

**Transversais**
- Design de leitura com qualidade editorial (mesmo com identidade visual provisória).
- Acessibilidade AA (contraste, teclado, alt text, fonte ajustável).
- Responsivo (desktop primeiro; consulta em mobile).
- Analytics de uso (páginas, buscas, "Usar em aula", downloads).
- Coleta de feedback do professor por unidade (útil? / comentário).
- Painel editorial interno (status e cobertura da matriz) — pode ser planilha + view simples no MVP.

### 20.3 Funcionalidades desejáveis (se couber no orçamento/prazo do MVP)

- Pré-visualização rápida do conteúdo a partir do cartão.
- Compartilhar plano/coleção por link.
- Exportar pacote de PDFs de uma coleção.
- Filtro por tipo de produção e por modalidade.
- Modo de apresentação com anotações do professor lado a lado.
- Página "Progresso" do aluno via histórico local.

### 20.4 Fica para depois (pós-MVP / Fase 3)

- Conta de aluno, turmas, atribuição de tarefas.
- Envio e correção de produção escrita pela plataforma.
- IA (geração de atividades, adaptação de nível, feedback automático, busca semântica).
- Compartilhamento social de coleções entre professores / biblioteca comunitária.
- Integrações (Google Classroom, LMS, videoconferência).
- Multi-idioma de interface e notas contrastivas por L1.
- Níveis ILR 4–5.
- App nativo.

### 20.5 Quantidade e tipos de conteúdo do piloto — [PROPOSTA DE PRODUTO]

**Volume recomendado:** **48 unidades** (mínimo viável 40; ideal 60).

**Distribuição sugerida por nível** (piloto cobre 0+ a 3/3+):

| Nível | Unidades | Comentário |
|---|---|---|
| 0+ | 3 | listas, formulários, legendas |
| 1 | 8 | bilhetes, mensagens, formulários, mini-descrições |
| 1+ | 8 | e-mail pessoal, recado, descrição, relato simples |
| 2 | 10 | e-mail profissional, instrução, relato, resumo curto, comparação |
| 2+ | 8 | reclamação, opinião, aconselhamento, relato desenvolvido |
| 3 | 8 | relatório, texto argumentativo, resenha, síntese |
| 3+ | 3 | editorial, ensaio, parecer |

**Distribuição por contexto (piloto):** ênfase em **Profissional (14), Cotidiano (12), Público/Social (10), Cultural/Brasil (8), Acadêmico (4)** — `[VALIDAR COM CONTRATANTE]` conforme público prioritário.

**Cobertura de gêneros no piloto (mínimo):** lista, formulário, bilhete, mensagem, e-mail pessoal, e-mail profissional, descrição, narrativa, relato, instrução, resumo, comparação, relatório, texto argumentativo, resenha, editorial. (16 dos 20 gêneros; artigo, ensaio, texto especializado e texto literário entram parcialmente.)

**Cobertura de funções no piloto:** todas as 18, cada uma em pelo menos 2 unidades, distribuídas em níveis diferentes.

**Tipos de conteúdo necessários no piloto:**
- 48 unidades completas.
- ~16 fichas de gênero.
- 1 rubrica geral + ~10 rubricas por gênero.
- ~12 exemplos comentados (2 por faixa de nível).
- ~48 materiais do aluno + 48 materiais do professor (derivados).
- Textos/mídia originais ou devidamente licenciados para cada unidade.

### 20.6 Estrutura mínima da área do professor (MVP)

```
Área do Professor
├── Biblioteca (busca + filtros + cartões + modo professor na unidade)
├── Minhas coleções (CRUD de coleções e itens)
├── Planejar aula (sequência simples + notas + export PDF)
├── Downloads (arquivos por unidade e por coleção)
├── Avaliação (rubricas + guia + exemplos comentados)
└── Conta (dados básicos, buscas salvas, histórico de uso)
```

### 20.7 Por que não IA no MVP — [DECISÃO PEDAGÓGICA]

O valor central — encontrar material coerente e pronto, com critérios — é entregue por **curadoria humana + boa arquitetura de informação + filtros**. IA agregaria custo, risco de qualidade/segurança, necessidade de moderação e dependência de infraestrutura, sem ser necessária para validar a proposta de valor. IA passa a fazer sentido quando (a) o catálogo for grande o suficiente para busca semântica valer a pena, (b) houver base de uso para treinar/avaliar geração de atividades, (c) houver processo editorial para revisar saídas de IA. Isso é objeto da Fase 3, com justificativa específica por funcionalidade.

---

## 21. Funcionalidades futuras (ETAPA 13, Fase 3)

- **Contas de alunos**: perfil, histórico entre dispositivos, biblioteca pessoal.
- **Turmas**: professor cria turma, adiciona alunos, organiza materiais por turma.
- **Atribuição e entrega**: professor atribui uma tarefa; aluno produz e envia pela plataforma.
- **Acompanhamento**: painel do professor com quem fez o quê; visão de cobertura de funções/gêneros por aluno ao longo do tempo.
- **Avaliação assistida**: rubrica aplicada digitalmente, comentários ancorados no texto, histórico de devolutivas, evolução por dimensão.
- **Busca semântica**: encontrar conteúdo por descrição em linguagem natural ("preciso de algo para ensinar a pedir desmarcação de consulta educadamente").
- **IA — geração de atividades**: a partir de um texto ou tema, gerar rascunhos de atividades de compreensão/controladas, revisados por editor.
- **IA — adaptação de nível**: gerar versões de um mesmo conteúdo em faixas ILR adjacentes.
- **IA — feedback de produção escrita**: devolutiva preliminar nas quatro dimensões, sempre com o professor no circuito; nunca nota final automática.
- **Biblioteca comunitária**: professores publicam e compartilham coleções e adaptações, com curadoria.
- **Integrações**: Google Classroom, Moodle, ferramentas de videochamada.
- **Internacionalização**: interface em vários idiomas; notas contrastivas por L1.
- **Níveis 4–5** e trilhas para fins específicos (diplomacia, negócios, academia).
- **Analytics pedagógico** para coordenações: cobertura curricular, consistência de nível entre professores.

**Regra:** cada funcionalidade de IA só entra com (1) necessidade justificada, (2) processo de revisão editorial, (3) avaliação de risco (privacidade, viés, qualidade), (4) transparência para o professor.

---

## 22. Roadmap (ETAPA 13)

### Fase 1 — Concepção e especificação  *(este documento)*
**Objetivo:** definir o produto.
**Entregas:** especificação pedagógica, editorial, funcional e de arquitetura de informação; matrizes (ILR, funções, gêneros, contextos, temas); modelo de unidade + 2 exemplos; modelo conceitual de dados; escopo do MVP; roadmap; lista de pontos para o contratante.
**Não inclui:** código, identidade visual definitiva, banco de dados, IA.
**Validações necessárias ao fim da fase:** decisões do contratante (seção 24); pesquisa exploratória com 5–8 professores para testar as hipóteses.

### Fase 2 — Design e desenvolvimento do MVP
**Objetivo:** colocar no ar a biblioteca com valor real para o professor.
**Frentes:**
1. **Pesquisa e validação** com professores (entrevistas, teste de conceito, teste de 3–5 unidades-piloto em aula real).
2. **UX/UI**: identidade visual, design system, protótipos, testes de usabilidade das jornadas-chave (buscar → abrir → usar em aula → baixar).
3. **Produção editorial**: 40–60 unidades, fichas de gênero, rubricas, exemplos comentados; processo e guia editorial; controle de qualidade e de nível.
4. **Desenvolvimento**: front-end em Vercel; back-end/dados/auth/storage em Supabase; modelo de dados a partir da seção 19; CMS ou fluxo de publicação editorial; busca e filtros; geração de PDF; analytics; coleta de feedback.
5. **Conformidade**: LGPD (dados do professor), termos de uso, política de privacidade, acessibilidade AA, licenciamento de mídia.
**Marco de lançamento:** MVP com o piloto de conteúdo, aberto a um grupo inicial de professores.
**Métricas de saída:** adoção, % de sessões que terminam em uso/download, tempo busca→uso, cobertura da matriz, retenção 30 dias, NPS/feedback qualitativo.

### Fase 3 — Evolução da plataforma
**Objetivo:** de biblioteca para ambiente de ensino e acompanhamento.
**Blocos (priorização a definir com dados de uso):**
- Contas de aluno + turmas + atribuição/entrega.
- Avaliação assistida e acompanhamento longitudinal.
- Busca semântica.
- IA: geração de atividades → adaptação de nível → feedback de produção (nessa ordem, cada uma com revisão editorial e avaliação de risco).
- Biblioteca comunitária e integrações.
- Expansão de catálogo (mais níveis, fins específicos, mais idiomas de apoio).

**Cronograma indicativo** `[VALIDAR COM CONTRATANTE]` (depende de orçamento e time):
- Fase 1: ~3–5 semanas.
- Fase 2: ~4–7 meses (pesquisa + design + produção editorial em paralelo + desenvolvimento).
- Fase 3: contínua, em ciclos trimestrais orientados por métricas.

---

## 23. Premissas

**Pedagógicas / editoriais**
1. A ILR Writing é referência de proficiência adequada ao público-alvo (adultos, foco em uso funcional e profissional/acadêmico). `[HIPÓTESE A VALIDAR]`
2. Professores querem material organizado por capacidade e contexto, não só por gramática. `[HIPÓTESE A VALIDAR — pesquisa Fase 1/2]`
3. Unidades autossuficientes (sem trilha) atendem melhor o modelo de aula online do público. `[HIPÓTESE A VALIDAR]`
4. O gargalo principal do professor é tempo de preparação e calibragem de nível. `[HIPÓTESE A VALIDAR]`
5. Conteúdo majoritariamente sobre Brasil e mundo lusófono é diferencial competitivo. `[PROPOSTA DE PRODUTO]`
6. Rubrica de 4 dimensões × 4 pontos é aplicável por professores em poucos minutos. `[HIPÓTESE A VALIDAR — teste com professores]`

**De produto / público**
7. O usuário pagante/decisor é o professor (ou a instituição que compra para professores). `[VALIDAR COM CONTRATANTE]`
8. O aluno não precisa de conta no MVP. `[DECISÃO DE PRODUTO]`
9. Desktop é o dispositivo primário de preparação; mobile é consulta. `[HIPÓTESE A VALIDAR]`
10. Português como língua estrangeira/segunda/de acolhimento é o foco; não português como L1 escolar. `[VALIDAR COM CONTRATANTE]`

**Técnicas**
11. Pilha-alvo: **Supabase** (PostgreSQL gerenciado, Auth, Storage, RLS) + **Vercel** (hospedagem do front-end e funções serverless). `[VALIDAR COM CONTRATANTE — orçamento, limites de plano, escalabilidade esperada]`
12. Geração de PDF do material do aluno/professor é requisito de MVP (biblioteca de renderização a definir na Fase 2).
13. Não há requisito de operação offline além do download de PDFs.
14. Residência de dados: dados de professores podem ser hospedados fora do Brasil desde que em conformidade com a LGPD e informado na política de privacidade. `[VALIDAR COM CONTRATANTE]`
15. Não há, no MVP, tratamento de dados pessoais de alunos pela plataforma (o aluno não tem conta).
16. Volume inicial (piloto): dezenas a poucas centenas de professores; catálogo de dezenas de unidades — dentro dos planos iniciais de Supabase/Vercel. `[HIPÓTESE A VALIDAR]`

**De conteúdo / jurídico**
17. Mídia (textos, imagens, áudios) será original, de domínio público ou licenciada (Creative Commons ou licença paga). `[VALIDAR COM CONTRATANTE — orçamento de licenciamento]`
18. Os sites de referência (eslnewsstories, listenaminute) inspiram organização, não conteúdo nem layout; não haverá cópia.
19. Uso da marca/descritores da ILR: citar a fonte e não apresentar interpretação como oficial; verificar se há restrições de uso do nome/descritores para produto comercial. `[VALIDAR COM CONTRATANTE / jurídico]`

**De processo**
20. Haverá uma equipe editorial com revisão pedagógica e de nível antes de publicar qualquer unidade.
21. A identidade visual definitiva é entregue na Fase 2; a Fase 1 usa apenas referências de direção.
22. Haverá pesquisa com professores entre o fim da Fase 1 e o início da Fase 2.

---

## 24. Pontos que precisam ser definidos com o contratante

### 24.1 Estratégia e público
1. **Público prioritário do piloto** (freelancer / escola de idiomas / acolhimento / acadêmico–fins específicos). Impacta matriz temática, faixa de níveis, necessidade de impressão.
2. **Faixa de níveis do MVP** — confirmar 0+ a 3/3+; incluir ou não 4–5.
3. **Português como L2/LE/acolhimento apenas**, ou também apoio a português L1 escolar?
4. **Mundo lusófono**: foco só no Brasil ou também Portugal e países africanos de língua portuguesa?

### 24.2 Modelo de acesso e negócio
5. **Conteúdo aberto, freemium ou fechado** (login/assinatura)?
6. **Modelo de receita**: assinatura individual de professor, licença institucional, gratuito com financiamento, misto?
7. **Preço-alvo e disposição a pagar** do público (a testar na pesquisa).
8. **Há um cliente institucional âncora** (rede de escolas, órgão, universidade) para o piloto?

### 24.3 Conteúdo, editorial e jurídico
9. **Orçamento de produção editorial** (nº de unidades no piloto, autores, revisão).
10. **Orçamento de licenciamento de mídia** vs. produção 100% original/CC.
11. **Política editorial para temas sensíveis** (política, religião, raça, gênero) e para **linguagem inclusiva**.
12. **Uso do nome e dos descritores da ILR** em produto comercial — validação jurídica.
13. **Propriedade intelectual** do conteúdo produzido (do contratante, compartilhada, licença aberta?).
14. **Idioma(s) da interface** no MVP (só português? português + inglês/espanhol?).

### 24.4 Produto e escopo
15. **"Usar em aula"**: gerar **link para o aluno** (exige alguma persistência e página pública de sessão) ou só **PDF/apresentação**?
16. **Compartilhamento** de planos/coleções entre professores no MVP: sim/não.
17. **Página "Progresso" do aluno** no MVP: histórico local apenas, ou fora do MVP?
18. **Painel editorial**: ferramenta dedicada (CMS) ou planilha + views simples no MVP?
19. **Analytics e feedback**: quais eventos são obrigatórios; ferramenta (produto próprio no Supabase, ou serviço externo — implicação LGPD).

### 24.5 Técnico e conformidade
20. **Confirmar Supabase + Vercel**, planos contratados e limites; estratégia de backup e de ambiente (dev/homolog/prod).
21. **LGPD**: encarregado (DPO), base legal para dados de professores, política de privacidade, retenção, cookies/analytics.
22. **Residência de dados** e requisitos de qualquer cliente institucional (alguns órgãos exigem hospedagem no Brasil).
23. **Acessibilidade**: nível-alvo (recomendado WCAG 2.1 AA) e se há exigência legal específica do contratante.
24. **Domínio, marca e nome do produto**; e-mail; identidade visual (briefing e referências).

### 24.6 Processo
25. **Composição da equipe** para a Fase 2 (editorial, UX/UI, desenvolvimento) e quem é o responsável pedagógico final.
26. **Cronograma e orçamento** das Fases 2 e 3.
27. **Critérios de aceitação do MVP** (quais números/qualitativos definem "pronto para lançar").
28. **Plano de pesquisa com professores** (quantos, como recrutar, quando).

---

## Anexo A — Glossário de marcas do documento

- **[REFERÊNCIA OFICIAL]** — resumo em português de conteúdo da ILR Writing (fonte: govtilr.org). Não substitui o texto original.
- **[DECISÃO PEDAGÓGICA]** — escolha da equipe para operacionalizar a referência.
- **[PROPOSTA DE PRODUTO]** — decisão de produto/editorial/UX.
- **[HIPÓTESE A VALIDAR]** — suposição que precisa de evidência.
- **[VALIDAR COM CONTRATANTE]** — decisão que depende do contratante.

## Anexo B — Checklist de prontidão para a Fase 2

- [ ] Decisões da seção 24 respondidas (mínimo: 1, 2, 5, 6, 9, 10, 20, 21).
- [ ] Pesquisa exploratória com professores concluída e hipóteses (seção 23) revisadas.
- [ ] Público e faixa de níveis do piloto congelados.
- [ ] Matriz temática priorizada para o piloto.
- [ ] Guia editorial redigido (voz, nível, estrutura, revisão).
- [ ] Briefing de identidade visual e design system.
- [ ] Backlog de 40–60 unidades definido com nível/função/gênero/contexto/tema por unidade.
- [ ] Arquitetura técnica detalhada (modelo físico de dados, fluxo de publicação, geração de PDF, analytics) a partir da seção 19.
- [ ] Plano de conformidade LGPD e acessibilidade.

---

*Fim do documento — Fase 1.*
