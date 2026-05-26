# 🌐 MDR Ecosystem — Sistema de Gestão Operacional Logística

## 📌 Visão Geral

O **MDR Ecosystem** é um sistema web desenvolvido em HTML, CSS e JavaScript puro, focado na gestão operacional de processos logísticos, com controle completo de:

- Entrada de pedidos
- Requisição, faturamento e expedição
- Rastreabilidade por status
- Gestão por blocos diários
- Análise técnica XML x OC
- Indicadores operacionais e gerenciais

O sistema foi projetado para substituir controles manuais (Excel, papel, e-mails) por um fluxo estruturado, padronizado e auditável.

---

## 🎯 Objetivos do Sistema

- Centralizar a operação em um único ambiente
- Padronizar o fluxo operacional
- Evitar perda de informação
- Melhorar rastreabilidade dos pedidos
- Proporcionar controle gerencial em tempo real

---

## 🧩 Estrutura do Sistema

### 📍 Página 1 — Operação / Blocos do Dia
- Criação e gerenciamento de blocos por data
- Cadastro de processos operacionais
- Edição em linha (inline editing)
- Importação de pedidos via CSV
- Kanban com status operacional
- KPIs operacionais (requisição, faturamento, expedição)

---

### 📍 Página 2 — XML x OC (Análise Técnica)
- Leitura de arquivos XML e OC
- Comparação automática:
  - Produto
  - Código
  - Quantidade
  - Valor
- Classificação:
  - ✅ CONFORME
  - ⚠️ PARCIAL
  - ❌ DIVERGENTE
- Geração de parecer técnico estruturado

---

### 📍 Página 3 — Gestão / Consulta
- Visão consolidada de todos os processos
- Filtros avançados:
  - Status
  - Data
  - Urgência
  - Coluna SharePoint
- KPIs gerenciais:
  - Tempo médio
  - Processos concluídos
  - Faturamento
  - Expedição
- Consulta de blocos arquivados

---

## 🔁 Fluxo Operacional

O sistema segue um fluxo estruturado:

```text
AGUARDANDO REQUISIÇÃO
↓
EM SEPARAÇÃO
↓
NF INFORMADA
↓
LIBERADA PARA EXPEDIÇÃO
↓
EM EXPEDIÇÃO
↓
CONCLUÍDO