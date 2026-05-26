MDR ECOSYSTEM — DOCUMENTO DE MELHORIAS E FUTURAS INTEGRAÇÕES

Autor: João Victor Viana Oliveira Silva
Status atual: MVP local validado
Objetivo deste documento: registrar, organizar e priorizar as melhorias e integrações futuras planejadas para o MDR Ecosystem, com base no MVP atual.

============================================================
1. VISÃO GERAL
============================================================

O MDR Ecosystem já possui uma base funcional robusta para operação, controle por blocos, rastreabilidade de pedidos, análise técnica e gestão. A próxima etapa do projeto é amadurecer a estrutura do sistema, reduzir complexidade no módulo principal, melhorar a experiência operacional e preparar o ecossistema para integração com SharePoint, Power Automate e outras tecnologias.

A evolução do projeto deve seguir a lógica:

MVP local validado
→ melhoria de estrutura e usabilidade
→ consolidação dos dados e relatórios
→ integração com SharePoint e automações
→ expansão para arquitetura mais robusta

============================================================
2. MELHORIAS ESTRUTURAIS DO PROJETO
============================================================

2.1. Separar a Página 2 em um projeto próprio
------------------------------------------------------------
A Página 2 (XML x OC / Técnica) deixará de fazer parte do MDR Ecosystem principal e passará a ser um projeto separado.

Objetivos:
- manter o ecossistema principal mais focado na operação e gestão;
- reduzir complexidade do sistema principal;
- facilitar manutenção e evolução do módulo técnico;
- permitir que o projeto técnico tenha repositório e backlog próprios.

Resultado esperado:
- o MDR Ecosystem fica mais enxuto e focado;
- a análise XML x OC passa a ter vida própria e evolução independente.


2.2. Permitir exclusão de bloco na Página 1
------------------------------------------------------------
Atualmente existe a função de limpar entradas do bloco, mas ainda não há exclusão completa do bloco.

Melhoria desejada:
- adicionar opção para excluir o bloco na seção “Controle de Blocos por Dia”.

Regra sugerida:
- permitir exclusão apenas de blocos não arquivados;
- exigir confirmação antes de excluir;
- ao excluir o bloco ativo, selecionar automaticamente outro bloco aberto, se existir.

Benefício:
- maior flexibilidade operacional;
- correção rápida de blocos criados por engano.


2.3. Remover complexidade desnecessária do sistema principal
------------------------------------------------------------
Com a saída da Página 2 para um projeto separado, o ecossistema principal deve ser reorganizado para reforçar:
- operação do dia;
- gestão consolidada;
- integração futura com SharePoint;
- rastreabilidade dos pedidos.

============================================================
3. EVOLUÇÃO DA IMPORTAÇÃO E DOS DADOS
============================================================

3.1. Utilizar importação por relatório real
------------------------------------------------------------
A importação por CSV precisa evoluir para trabalhar com relatórios reais da operação.

Necessidades:
- mapear o formato real dos arquivos;
- entender nomes de colunas e estrutura dos relatórios;
- validar formatos de data e valores monetários;
- entender campos obrigatórios e opcionais;
- padronizar modelo oficial de importação.

Objetivo:
- permitir entrada de dados confiável por relatório operacional;
- reduzir cadastro manual;
- padronizar a alimentação do sistema.

Resultado esperado:
- modelo de importação alinhado ao processo real;
- menor retrabalho manual;
- aumento de velocidade na carga de dados.


3.2. Integrar banco de dados
------------------------------------------------------------
O sistema hoje usa persistência local no navegador. A evolução natural é adicionar uma camada de persistência externa.

Primeira opção sugerida:
- SharePoint como base de dados inicial.

Objetivos:
- manter histórico fora do navegador;
- permitir consultas reais e compartilhadas;
- suportar múltiplos usuários futuramente;
- viabilizar integrações e automações.

Possível evolução posterior:
- backend dedicado;
- banco relacional ou outra estrutura de dados mais robusta.

============================================================
4. INTEGRAÇÃO COM SHAREPOINT E POWER AUTOMATE
============================================================

4.1. Enviar item para lista SharePoint ao preencher data de emissão
------------------------------------------------------------
Ao preencher a data de emissão, o sistema deve poder enviar o pedido para a lista do SharePoint.

Comportamento esperado:
- ao preencher data de emissão, permitir disparo automático ou por botão;
- criar item na lista do SharePoint;
- registrar o pedido inicialmente na coluna “LIBERADAS”.


4.2. Espelhamento entre SharePoint e painel de cards/colunas
------------------------------------------------------------
O painel visual do sistema deve refletir o mesmo comportamento das colunas do SharePoint.

Colunas esperadas:
- LIBERADAS;
- EM EXPEDIÇÃO;
- FINALIZADAS.

Objetivo:
- manter consistência entre o sistema local e o fluxo operacional refletido no SharePoint;
- permitir leitura visual dos pedidos tanto no ecossistema quanto na lista corporativa.

Fluxo esperado:
- ao liberar: cria item em LIBERADAS;
- ao entrar em expedição: move para EM EXPEDIÇÃO;
- ao finalizar: move para FINALIZADAS.


4.3. Power Automate
------------------------------------------------------------
O Power Automate deve ser considerado como camada de automação futura.

Possíveis usos:
- criar ou atualizar item no SharePoint;
- enviar notificações por e-mail ou Teams;
- alertar processos atrasados;
- avisar quando chamado seguir aberto por mais de 1 dia;
- movimentar cartões e atualizar campos automaticamente.

============================================================
5. MELHORIAS DE IMPRESSÃO E RELATÓRIOS
============================================================

5.1. Amadurecer impressões e relatórios
------------------------------------------------------------
As impressões e relatórios atuais já existem, mas ainda precisam de mais estrutura, clareza visual e objetivo operacional/gerencial.

Melhorias desejadas:
- cabeçalho mais profissional;
- separação por seções;
- agrupamento visual melhor;
- resumos executivos;
- melhor padronização para impressão;
- relatórios com leitura mais organizada;
- relatório por bloco mais forte;
- relatório gerencial consolidado com melhor narrativa visual.

Objetivo:
- transformar a saída impressa em documento realmente útil para operação e gestão.

============================================================
6. MELHORIAS DA PÁGINA 3 — GESTÃO
============================================================

6.1. Ampliar os cálculos de média entre etapas
------------------------------------------------------------
A Página 3 deve oferecer indicadores mais completos sobre o tempo do processo.

Métricas desejadas:
- média de tempo entre pedido criado e entrada em separação;
- média de tempo entre em separação e faturamento;
- média de tempo entre faturamento e expedição.

Objetivo:
- identificar gargalos por etapa;
- medir eficiência do processo operacional;
- apoiar decisões de melhoria contínua.


6.2. Pesquisa pela observação na consulta consolidada
------------------------------------------------------------
A consulta consolidada da Página 3 deve permitir pesquisa por observação do pedido.

Observação:
- no MVP atual isso já está parcialmente contemplado na lógica de busca, mas deve ser mantido como requisito funcional oficial.

Objetivo:
- facilitar rastreabilidade;
- melhorar consulta por contexto operacional.

============================================================
7. FLUXO VISUAL POR PEDIDO
============================================================

7.1. Criar um fluxo visual que mostre o caminho do pedido
------------------------------------------------------------
Cada pedido deve exibir visualmente seu estágio dentro do fluxo operacional.

Informações desejadas no fluxo visual:
- etapas do processo;
- status atual destacado;
- tempo no status atual;
- possibilidade de exibir etapas já concluídas;
- término visual em “Expedidas” ou etapa final equivalente.

Sugestão de conceito:
- barra de progresso;
- trilha de status;
- marcador visual por etapa;
- layout ligado diretamente ao campo de status atual.

Objetivo:
- melhorar leitura operacional;
- reduzir dependência de texto puro;
- facilitar entendimento rápido do estágio do pedido.

============================================================
8. EVOLUÇÃO DO STATUS CHAMADO
============================================================

8.1. Melhorar o tratamento do status CHAMADO
------------------------------------------------------------
Hoje o status CHAMADO existe, mas precisa amadurecer para se tornar um fluxo acompanhado.

Melhoria desejada:
Ao selecionar CHAMADO, abrir campo complementar para registro de:
- número do chamado;
- motivo do chamado;
- andamento do chamado.

Pode ser:
- um campo único estruturado;
- ou campos separados.


8.2. Notificação de andamento no dia seguinte
------------------------------------------------------------
Se o pedido continuar em status CHAMADO no dia seguinte, o sistema deve alertar o usuário para registrar andamento.

Comportamento esperado:
- aviso ou notificação ao abrir o sistema;
- solicitação de atualização;
- complemento no mesmo campo do chamado ou em histórico próprio.

Objetivo:
- evitar que o pedido fique parado sem acompanhamento;
- aumentar rastreabilidade do tratamento do chamado.

Observação técnica:
- no MVP local, esse aviso pode acontecer quando o sistema é aberto;
- com Power Automate, isso pode virar notificação real automática.

============================================================
9. EVOLUÇÃO DO STATUS CANCELADO
============================================================

9.1. Exigir motivo do cancelamento
------------------------------------------------------------
Quando o pedido for colocado em status CANCELADO, o sistema deve exigir registro complementar.

Campo desejado:
- motivo do cancelamento.

Objetivo:
- melhorar rastreabilidade;
- qualificar análise gerencial;
- permitir entendimento posterior da causa do cancelamento.

============================================================
10. OUTRAS INTEGRAÇÕES FUTURAS
============================================================

10.1. n8n
------------------------------------------------------------
Pode ser utilizado no futuro para automações mais flexíveis, principalmente fora do fluxo exclusivamente Microsoft.

Possíveis usos:
- integração com múltiplos sistemas;
- rotinas automáticas;
- notificações personalizadas;
- sincronização entre dados e processos.


10.2. Docker
------------------------------------------------------------
Pode ser utilizado quando o projeto sair do modelo puramente local e passar a ter backend, API ou serviços auxiliares.

Funções futuras:
- padronizar ambiente;
- facilitar deploy;
- garantir consistência entre máquinas e servidores.


10.3. Figma
------------------------------------------------------------
Pode ser usado para padronização visual do ecossistema.

Usos futuros:
- criar design system;
- padronizar componentes;
- melhorar layout do fluxo visual por pedido;
- documentar evolução visual do projeto.


10.4. Flutter
------------------------------------------------------------
Pode ser considerado se o sistema evoluir para versão mobile, desktop ou multiplataforma mais madura.

Possíveis cenários:
- app interno de operação;
- conferência mobile;
- painel operacional multiplataforma.

============================================================
11. PRIORIDADE SUGERIDA DE EVOLUÇÃO
============================================================

Curto prazo:
1. separar a Página 2 em projeto próprio;
2. permitir excluir bloco;
3. melhorar status CHAMADO;
4. melhorar status CANCELADO;
5. amadurecer relatórios e impressões;
6. ampliar KPIs da Página 3;
7. criar fluxo visual por pedido.

Médio prazo:
8. padronizar importação por relatório;
9. consolidar estrutura de dados;
10. integrar SharePoint como base inicial;
11. criar sincronização com cards/colunas.

Longo prazo:
12. Power Automate;
13. n8n;
14. Docker;
15. Figma como padrão visual;
16. Flutter, se houver necessidade real de app.

============================================================
12. CONCLUSÃO
============================================================

O MDR Ecosystem já possui uma base sólida como MVP local validado. As próximas evoluções devem focar em:
- simplificação do sistema principal;
- amadurecimento da operação;
- melhoria visual e gerencial;
- preparação para persistência externa;
- integração gradual com o ecossistema Microsoft;
- estruturação para automações futuras.

A visão de longo prazo é transformar o projeto de um sistema local validado em uma plataforma operacional e gerencial mais integrada, rastreável e escalável.
