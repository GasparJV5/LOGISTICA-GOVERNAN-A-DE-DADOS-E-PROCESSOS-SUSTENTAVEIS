# 🌐 MDR Ecosystem — Projeto Final Validado# 🌐 MDR Ecosystem um sistema web em **HTML, CSS e JavaScript puro**, desenvolvido para centralizar e padronizar rotinas operacionais da logística em um único ambiente.

O projeto foi estruturado para funcionar localmente, com persistência no navegador, controle por blocos diários, análise técnica de documentos e visão gerencial consolidada.

---

## 🎯 Objetivo do Projeto

Criar um ambiente único para:

- controlar pedidos por bloco/dia;
- acompanhar o fluxo operacional;
- registrar e rastrear status;
- evitar duplicidade de pedido e NF;
- analisar XML x OC;
- gerar indicadores operacionais e gerenciais;
- apoiar tomada de decisão com histórico e tempos de processo.

---

## 🧩 Estrutura do Sistema

O sistema está dividido em **3 páginas principais**:

### 1. Operação / Blocos do Dia
Responsável pelo controle operacional diário.

#### Funcionalidades:
- criação e carregamento de blocos por data;
- cadastro manual de processos;
- edição em linha;
- importação de pedidos via CSV;
- bloqueio de pedido repetido;
- bloqueio de NF repetida;
- atualização automática de status;
- painel visual em colunas (Kanban);
- resumo do bloco ativo;
- impressão do bloco atual.

---

### 2. XML x OC / Técnica
Módulo técnico separado da operação principal.

#### Funcionalidades:
- leitura de arquivo XML;
- leitura de arquivo OC (CSV ou XML);
- comparação automática entre XML e OC;
- classificação do resultado em:
  - **CONFORME**
  - **PARCIAL**
  - **DIVERGENTE**
- geração de histórico técnico;
- emissão de parecer técnico;
- lista de destino simulada para SharePoint.

---

### 3. Gestão / Consulta
Módulo gerencial consolidado com base em todos os blocos criados.

#### Funcionalidades:
- visão geral dos processos;
- filtros por:
  - status;
  - data;
  - urgência;
  - coluna SharePoint;
- indicadores gerenciais;
- consulta consolidada;
- visualização de blocos arquivados;
- rastreabilidade completa dos processos;
- relatório gerencial para impressão.

---

## 🔁 Fluxo Operacional

O sistema trabalha com os seguintes status:

```text
NOVO
→ AGUARDANDO REQUISIÇÃO
→ EM SEPARAÇÃO
→ NF INFORMADA
→ LIBERADA PARA EXPEDIÇÃO
→ EM EXPEDIÇÃO
→ CONCLUÍDO

## 📌 Visão Geral



Também existem status especiais:

CHAMADO
CANCELADO

Regras aplicadas:

não permite regressão indevida no fluxo;
exige campos obrigatórios para avanço de etapa;
sincroniza status com a coluna operacional;
protege consistência da operação.


📊 Indicadores do Sistema
Página 1 — Operação

total de pedidos criados;
aguardando requisição;
em separação;
notas faturadas;
liberadas à expedição;
chamados;
cancelados.

Página 2 — Técnica

total de análises;
conformes;
parciais;
divergentes.

Página 3 — Gestão

média de tempo criado × liberado;
média até concluir;
total de processos;
concluídos;
faturadas;
em expedição;
chamados;
cancelados;
urgentes.


🚨 Regras e Inteligência Implementadas
O sistema possui automações operacionais e regras de consistência:

ao preencher a requisição, o status pode avançar para EM SEPARAÇÃO;
ao preencher a NF, o status pode avançar para NF INFORMADA;
ao preencher a data de emissão, o status pode avançar para LIBERADA PARA EXPEDIÇÃO;
ao mover a coluna SharePoint, o status é sincronizado automaticamente quando aplicável;
pedidos com mais de 1 dia sem faturamento geram alerta;
o sistema solicita o motivo da demora no faturamento;
o pedido atrasado recebe marcação visual.


✅ Funcionalidades Principais

controle por blocos diários;
cadastro e edição de processos;
validação de duplicidade de pedido;
validação de duplicidade de NF;
importação CSV inteligente;
exportação JSON;
exportação CSV;
backup local automático;
cronômetro por status;
histórico completo de alterações;
painel estilo Kanban;
impressão de blocos;
relatório gerencial;
arquivamento de blocos fechados;
análise técnica XML x OC.


💾 Persistência de Dados
O sistema funciona localmente utilizando:

localStorage
chave principal de armazenamento;
chave de backup redundante;
exportação manual em JSON para segurança adicional.


Observação: por ser um MVP local, recomenda-se exportar a base periodicamente.


🛠 Tecnologias Utilizadas

HTML5
CSS3
JavaScript Vanilla
localStorage para persistência local


▶️ Como Executar

Abra o arquivo .html no navegador;
Crie ou carregue um bloco do dia;
Cadastre processos manualmente ou importe via CSV;
Atualize o andamento conforme a operação;
Consulte indicadores e histórico.


📁 Modelo de Importação CSV
O sistema espera colunas como:
Plain Textpedido;destinatario;uf;requisicao;nf;valor;status;operacao;dataEntrada;responsavel;carga;urgente;observacao;dataEmissao;sharePointLane;motivoAtrasoMostrar mais linhas

📌 Características do MVP
Este MVP foi construído com foco em:

operação local;
praticidade;
rastreabilidade;
clareza visual;
robustez de regra de negócio;
validação do processo antes de integração com sistemas externos.


🔮 Evoluções Futuras
Possíveis próximos passos do projeto:

integração com SharePoint;
integração com Power Automate;
persistência em banco de dados;
backend com API;
multiusuário;
autenticação;
automações com n8n;
padronização visual em Figma;
empacotamento com Docker;
futura evolução para app com Flutter.


👨‍💻 Autor
João Victor Viana Oliveira Silva