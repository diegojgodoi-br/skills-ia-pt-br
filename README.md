<div align="center">

<img src="assets/banner.svg" alt="Skills de IA em português — 28 skills prontas para o Claude" width="100%">

<br>

[![Skills](https://img.shields.io/badge/skills-28-1fbf6b?style=for-the-badge)](#-catálogo)
[![Profissões](https://img.shields.io/badge/profissões-14-f5c400?style=for-the-badge)](#-encontre-pela-sua-profissão)
[![Idioma](https://img.shields.io/badge/idioma-PT--BR-0b2a1d?style=for-the-badge)](#)
[![Licença MIT](https://img.shields.io/badge/licença-MIT-555?style=for-the-badge)](LICENSE)

[![Stars](https://img.shields.io/github/stars/diegojgodoi-br/skills-ia-pt-br?style=social)](https://github.com/diegojgodoi-br/skills-ia-pt-br/stargazers)

**Skills prontas para o Claude, escritas em português para a rotina de quem trabalha no Brasil.**<br>
Instale uma vez — o Claude passa a fazer a tarefa sempre do mesmo jeito, com os passos, o formato e os cuidados certos.

[**Instalar**](#-instalação-em-2-minutos) · [**Catálogo**](#-catálogo) · [**Por profissão**](#-encontre-pela-sua-profissão) · [**Site**](https://iacomousar.com.br/skills) · [**Sugerir uma skill**](https://github.com/diegojgodoi-br/skills-ia-pt-br/issues/new?template=sugerir-skill.yml)

</div>

---

## ✨ Por que usar

- **Em português de verdade** — termos, exemplos e contexto brasileiros (Simples Nacional, safra, notificação extrajudicial, DP…).
- **Resultado padronizado** — cada skill define os passos e o formato da entrega, então você não precisa reescrever o prompt toda vez.
- **Automático** — depois de instalada, o Claude usa a skill sozinho quando o seu pedido combinar.
- **Aberto** — licença MIT: use, adapte para a sua empresa e redistribua.

> **O que é uma skill?** Uma pasta com um arquivo `SKILL.md` que ensina o Claude a fazer uma tarefa. Segue o padrão aberto [Agent Skills](https://agentskills.io/).

## 🚀 Instalação em 2 minutos

<details open>
<summary><b>No claude.ai (site ou app)</b></summary>

1. Ative **Execução de código e criação de arquivos** em *Configurações › Capacidades*.
2. Baixe o `.zip` da skill na [página de Releases](https://github.com/diegojgodoi-br/skills-ia-pt-br/releases/latest) ou na página dela em [iacomousar.com.br/skills](https://iacomousar.com.br/skills).
3. Vá em *Personalizar › Skills › + › Enviar uma skill* e escolha o `.zip`.

</details>

<details>
<summary><b>No Claude Code</b></summary>

```bash
git clone https://github.com/diegojgodoi-br/skills-ia-pt-br.git
mkdir -p ~/.claude/skills
cp -r skills-ia-pt-br/skills/*/ ~/.claude/skills/
```

Quer só uma? `cp -r skills-ia-pt-br/skills/analisar-processo-judicial ~/.claude/skills/`

</details>

Depois é só pedir normalmente. Por exemplo:

> *"Compare essas três propostas de fornecedor de internet e me diga qual faz mais sentido."*<br>
> *"Monte o calendário de obrigações deste mês para um cliente do Lucro Presumido."*<br>
> *"Explique essa recomendação de adubação para o produtor em linguagem simples."*

## 📚 Catálogo


### 💼 Gestão, finanças e contabilidade

| Skill | O que faz | |
|---|---|---|
| [**Organizar documentos digitais**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/organizar-documentos-digitais/SKILL.md) | Estrutura de pastas e padrão de nomes de arquivos para achar tudo rápido. | [site ↗](https://iacomousar.com.br/skills/organizar-documentos-digitais) |
| [**Comparar propostas de fornecedores**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/comparar-propostas-fornecedores/SKILL.md) | Quadro de decisão objetivo entre propostas, com critérios e pesos. | [site ↗](https://iacomousar.com.br/skills/comparar-propostas-fornecedores) |
| [**Organizar finanças do negócio**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/organizar-financas-negocio/SKILL.md) | Separa pessoal de empresarial e prepara o fechamento do mês para o contador. | [site ↗](https://iacomousar.com.br/skills/organizar-financas-negocio) |
| [**Analisar custos e despesas**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/analisar-custos-e-despesas/SKILL.md) | Encontra onde cortar e otimizar gastos da empresa. | [site ↗](https://iacomousar.com.br/skills/analisar-custos-e-despesas) |
| [**Elaborar roteiro de cobrança**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/elaborar-roteiro-cobranca/SKILL.md) | Mensagens por faixa de atraso e estrutura de negociação de dívidas. | [site ↗](https://iacomousar.com.br/skills/elaborar-roteiro-cobranca) |
| [**Calendário de obrigações contábeis**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/organizar-calendario-obrigacoes/SKILL.md) | Obrigações fiscais e contábeis com prazos e documentos por cliente. | [site ↗](https://iacomousar.com.br/skills/organizar-calendario-obrigacoes) |
| [**Análise de enquadramento tributário**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/analisar-enquadramento-tributario/SKILL.md) | Simples Nacional × Lucro Presumido × Lucro Real, lado a lado. | [site ↗](https://iacomousar.com.br/skills/analisar-enquadramento-tributario) |

### ⚖️ Jurídico

| Skill | O que faz | |
|---|---|---|
| [**Analisar processo judicial**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/analisar-processo-judicial/SKILL.md) | Extrai partes, objeto, andamentos e prazos em uma visão estruturada. | [site ↗](https://iacomousar.com.br/skills/analisar-processo-judicial) |
| [**Rascunhar notificação extrajudicial**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/rascunhar-notificacao-extrajudicial/SKILL.md) | Notificações, cartas de cobrança e comunicados formais. | [site ↗](https://iacomousar.com.br/skills/rascunhar-notificacao-extrajudicial) |

### 🌾 Agro

| Skill | O que faz | |
|---|---|---|
| [**Planejar safra agrícola**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-safra-agricola/SKILL.md) | Plano preliminar de safra considerando cultura, clima e custos. | [site ↗](https://iacomousar.com.br/skills/planejar-safra-agricola) |
| [**Planejamento financeiro da safra**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-safra-custos/SKILL.md) | Custos e resultado da safra em diferentes cenários. | [site ↗](https://iacomousar.com.br/skills/planejar-safra-custos) |
| [**Comunicar recomendação rural**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/comunicar-recomendacao-rural/SKILL.md) | Traduz a recomendação técnica para a linguagem do produtor e da equipe. | [site ↗](https://iacomousar.com.br/skills/comunicar-recomendacao-rural) |
| [**Organizar equipe rural**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/organizar-equipe-rural/SKILL.md) | Escala de trabalho, distribuição de tarefas e comunicados da propriedade. | [site ↗](https://iacomousar.com.br/skills/organizar-equipe-rural) |

### 📣 Marketing e vendas

| Skill | O que faz | |
|---|---|---|
| [**Planejar calendário de conteúdo**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-calendario-conteudo/SKILL.md) | Calendário semanal ou mensal para redes sociais e blog. | [site ↗](https://iacomousar.com.br/skills/planejar-calendario-conteudo) |
| [**Adaptar mensagem por canal**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/adaptar-mensagem-canal/SKILL.md) | Um conteúdo, versões para e-mail, redes sociais e blog. | [site ↗](https://iacomousar.com.br/skills/adaptar-mensagem-canal) |
| [**Planejar promoção de vendas**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-promocao-vendas/SKILL.md) | Promoções para girar estoque, gerar caixa ou atrair clientes. | [site ↗](https://iacomousar.com.br/skills/planejar-promocao-vendas) |
| [**Planejar estratégia de negociação**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-estrategia-negociacao/SKILL.md) | Objetivos, limites, argumentos e concessões antes da reunião. | [site ↗](https://iacomousar.com.br/skills/planejar-estrategia-negociacao) |
| [**Analisar dados de vendas**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/analisar-dados-vendas/SKILL.md) | Padrões, tendências e oportunidades nos números de vendas. | [site ↗](https://iacomousar.com.br/skills/analisar-dados-vendas) |

### 🏠 Imobiliário

| Skill | O que faz | |
|---|---|---|
| [**Roteiro de captação de imóveis**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/elaborar-roteiro-captacao/SKILL.md) | Abordagem e reunião com proprietários para conseguir exclusividade. | [site ↗](https://iacomousar.com.br/skills/elaborar-roteiro-captacao) |
| [**Comparativo de mercado imobiliário**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/analisar-comparativo-mercado/SKILL.md) | Estudo de comparáveis para definir preço de venda ou locação. | [site ↗](https://iacomousar.com.br/skills/analisar-comparativo-mercado) |

### 💻 TI e desenvolvimento

| Skill | O que faz | |
|---|---|---|
| [**Analisar logs de erros**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/analisar-logs-erros/SKILL.md) | Padrões, causa provável e ações corretivas a partir de logs. | [site ↗](https://iacomousar.com.br/skills/analisar-logs-erros) |
| [**Planejar janela de mudança de TI**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-janela-mudanca/SKILL.md) | Passos, testes, rollback e comunicação da mudança. | [site ↗](https://iacomousar.com.br/skills/planejar-janela-mudanca) |
| [**Planejar migração técnica**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-migracao-tecnica/SKILL.md) | Fases, tarefas, riscos e requisitos da migração de sistemas. | [site ↗](https://iacomousar.com.br/skills/planejar-migracao-tecnica) |
| [**Revisar código para segurança**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/revisar-codigo-seguranca/SKILL.md) | Caça SQL Injection, XSS e outras falhas comuns. | [site ↗](https://iacomousar.com.br/skills/revisar-codigo-seguranca) |

### 👥 RH e Departamento Pessoal

| Skill | O que faz | |
|---|---|---|
| [**Analisar dados de desligamento**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/analisar-dados-desligamento/SKILL.md) | Padrões e causas de saídas, com ações de retenção. | [site ↗](https://iacomousar.com.br/skills/analisar-dados-desligamento) |
| [**Rascunhar políticas de RH**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/rascunhar-politica-rh/SKILL.md) | Texto base para férias, uso de equipamentos e outras políticas. | [site ↗](https://iacomousar.com.br/skills/rascunhar-politica-rh) |

### 🎓 Educação

| Skill | O que faz | |
|---|---|---|
| [**Planejar aula completa**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-aula-completa/SKILL.md) | Objetivos, conteúdo, atividades, recursos e avaliação. | [site ↗](https://iacomousar.com.br/skills/planejar-aula-completa) |
| [**Rascunhar feedback para aluno**](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/rascunhar-feedback-aluno/SKILL.md) | Feedback construtivo e encorajador sobre trabalhos. | [site ↗](https://iacomousar.com.br/skills/rascunhar-feedback-aluno) |

## 🧭 Encontre pela sua profissão

| Profissão | Skills recomendadas |
|---|---|
| ⚖️ Advogado | [Analisar processo judicial](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/analisar-processo-judicial/SKILL.md) · [Rascunhar notificação extrajudicial](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/rascunhar-notificacao-extrajudicial/SKILL.md) |
| 📊 Contador | [Calendário de obrigações contábeis](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/organizar-calendario-obrigacoes/SKILL.md) · [Análise de enquadramento tributário](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/analisar-enquadramento-tributario/SKILL.md) · [Organizar finanças do negócio](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/organizar-financas-negocio/SKILL.md) · [Analisar custos e despesas](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/analisar-custos-e-despesas/SKILL.md) |
| 🗂️ Administrativo | [Organizar documentos digitais](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/organizar-documentos-digitais/SKILL.md) · [Comparar propostas de fornecedores](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/comparar-propostas-fornecedores/SKILL.md) · [Organizar finanças do negócio](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/organizar-financas-negocio/SKILL.md) · [Analisar custos e despesas](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/analisar-custos-e-despesas/SKILL.md) · [Elaborar roteiro de cobrança](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/elaborar-roteiro-cobranca/SKILL.md) |
| 💰 Financeiro | [Analisar custos e despesas](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/analisar-custos-e-despesas/SKILL.md) · [Elaborar roteiro de cobrança](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/elaborar-roteiro-cobranca/SKILL.md) |
| 🏪 Pequeno empreendedor | [Organizar finanças do negócio](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/organizar-financas-negocio/SKILL.md) · [Analisar custos e despesas](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/analisar-custos-e-despesas/SKILL.md) · [Comparar propostas de fornecedores](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/comparar-propostas-fornecedores/SKILL.md) · [Planejar promoção de vendas](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-promocao-vendas/SKILL.md) · [Analisar dados de vendas](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/analisar-dados-vendas/SKILL.md) · [Planejar calendário de conteúdo](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-calendario-conteudo/SKILL.md) · [Adaptar mensagem por canal](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/adaptar-mensagem-canal/SKILL.md) · [Planejar estratégia de negociação](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-estrategia-negociacao/SKILL.md) · [Elaborar roteiro de cobrança](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/elaborar-roteiro-cobranca/SKILL.md) · [Calendário de obrigações contábeis](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/organizar-calendario-obrigacoes/SKILL.md) · [Análise de enquadramento tributário](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/analisar-enquadramento-tributario/SKILL.md) · [Organizar documentos digitais](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/organizar-documentos-digitais/SKILL.md) · [Rascunhar notificação extrajudicial](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/rascunhar-notificacao-extrajudicial/SKILL.md) |
| 🌱 Agrônomo / consultor rural | [Planejar safra agrícola](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-safra-agricola/SKILL.md) · [Planejamento financeiro da safra](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-safra-custos/SKILL.md) · [Comunicar recomendação rural](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/comunicar-recomendacao-rural/SKILL.md) |
| 🚜 Produtor rural | [Planejar safra agrícola](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-safra-agricola/SKILL.md) · [Planejamento financeiro da safra](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-safra-custos/SKILL.md) · [Comunicar recomendação rural](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/comunicar-recomendacao-rural/SKILL.md) · [Organizar equipe rural](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/organizar-equipe-rural/SKILL.md) |
| 🏠 Corretor de imóveis | [Roteiro de captação de imóveis](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/elaborar-roteiro-captacao/SKILL.md) · [Comparativo de mercado imobiliário](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/analisar-comparativo-mercado/SKILL.md) |
| 📣 Marketing | [Planejar calendário de conteúdo](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-calendario-conteudo/SKILL.md) · [Adaptar mensagem por canal](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/adaptar-mensagem-canal/SKILL.md) · [Planejar promoção de vendas](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-promocao-vendas/SKILL.md) |
| 🤝 Vendas | [Planejar estratégia de negociação](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-estrategia-negociacao/SKILL.md) · [Analisar dados de vendas](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/analisar-dados-vendas/SKILL.md) · [Planejar promoção de vendas](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-promocao-vendas/SKILL.md) · [Elaborar roteiro de cobrança](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/elaborar-roteiro-cobranca/SKILL.md) |
| 💻 Desenvolvedor | [Revisar código para segurança](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/revisar-codigo-seguranca/SKILL.md) · [Analisar logs de erros](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/analisar-logs-erros/SKILL.md) · [Planejar migração técnica](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-migracao-tecnica/SKILL.md) |
| 🖥️ TI e infraestrutura | [Planejar janela de mudança de TI](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-janela-mudanca/SKILL.md) · [Analisar logs de erros](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/analisar-logs-erros/SKILL.md) |
| 👥 RH e DP | [Analisar dados de desligamento](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/analisar-dados-desligamento/SKILL.md) · [Rascunhar políticas de RH](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/rascunhar-politica-rh/SKILL.md) |
| 🎓 Professor | [Planejar aula completa](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/planejar-aula-completa/SKILL.md) · [Rascunhar feedback para aluno](https://github.com/diegojgodoi-br/skills-ia-pt-br/blob/main/skills/rascunhar-feedback-aluno/SKILL.md) |

## ⚠️ Cuidados

As skills orientam o Claude, mas **não substituem a revisão de um profissional**. Revise sempre o resultado antes de enviar a um cliente e evite colar dados pessoais ou sigilosos sem necessidade.

## 🤝 Contribua

- 💡 **Tem uma tarefa repetitiva na sua profissão?** [Sugira uma skill](https://github.com/diegojgodoi-br/skills-ia-pt-br/issues/new?template=sugerir-skill.yml).
- 🐞 Achou algo errado numa skill? [Abra uma issue](https://github.com/diegojgodoi-br/skills-ia-pt-br/issues).
- 🔧 Melhorou uma skill? Pull requests são bem-vindos.

## 🌐 Mais skills

Em [iacomousar.com.br/skills](https://iacomousar.com.br/skills) reunimos também, com explicação em português, skills de outros autores publicadas no GitHub (com link e licença de cada repositório).

---

<div align="center">

**Se alguma skill te economizou tempo, deixe uma ⭐ — ajuda outros profissionais a encontrarem o projeto.**

Feito por [Diego Godoi](https://github.com/diegojgodoi-br) · [iacomousar.com.br](https://iacomousar.com.br) · Licença [MIT](LICENSE)

</div>
