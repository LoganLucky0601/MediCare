# MediCare — Protótipo navegável v2.0

Projeto acadêmico de Engenharia de Software: sistema demonstrativo de agendamento de consultas com **três dashboards individualizados**.

## Como abrir

1. Extraia o arquivo ZIP preservando a estrutura de pastas.
2. Abra `MediCare_v2` no Visual Studio Code.
3. Execute `index.html` diretamente no navegador ou pelo **Live Server** (opção recomendada).
4. No menu lateral, selecione uma **identidade demonstrativa**: Ana, Bruno, Clara, Patrícia ou um dos três médicos.
5. Navegue pelas funcionalidades habilitadas para o perfil escolhido. Use **Reiniciar dados** para retornar à base fictícia original.

Não é necessário instalar bibliotecas ou iniciar banco de dados. Os arquivos `index.html`, `styles.css` e `app.js` devem permanecer na mesma pasta.

## O que foi implementado

- **Paciente:** painel personalizado, indicadores, agendamento por especialidade/médico/data/horário, listagem das próprias consultas e cancelamento com antecedência mínima de 24 horas.
- **Recepcionista:** painel operacional, agenda geral com filtros por data e médico, agendamento por telefone para paciente cadastrado e log de solicitações fictícias de e-mail.
- **Médico:** painel individual, agenda apenas das próprias consultas e registro demonstrativo de atendimento após o horário da consulta.
- **Validações:** horário não disponível, dupla reserva do mesmo médico, acesso fora do perfil, titularidade do cancelamento, antecedência mínima e tentativa de atendimento não autorizado.

O código lê e salva dados fictícios em `localStorage` quando permitido pelo navegador.

## Documentos e diagramas

- `MediCare_Documentacao_Tecnica_v2.docx`: UC01 e regras originais preservadas; complementos, permissões e fluxos da v2, diagramas e cenários de teste.
- `diagrams/diagrama_casos_uso_original.png`: diagrama original inalterado.
- `diagrams/diagrama_dashboard_v2.png`: novos casos de uso relacionados aos dashboards.
- `diagrams/diagrama_classes_v2.png`: diagrama de classes proposto da versão 2.0.
- `diagrams/*.dot`: fonte editável de diagramas complementares (a imagem do modelo de classes foi refinada em Python).

## Limitações importantes

**Protótipo, não sistema clínico em produção.** A seleção de identidades é fictícia e aberta para demonstração: **não há autenticação real, controle de acesso em backend, sigilo entre usuários nem armazenamento seguro de prontuários**. Não introduza dados reais de pacientes. As notas de atendimento são meramente fictícias. O envio de e-mail é **simulado**; nenhuma mensagem é enviada. Uma solução real precisará de autenticação de contas, autorização no servidor, banco de dados transacional, trilha de auditoria e medidas de proteção de dados pessoais.

As regras originais RN01 a RN04 e a antecipação de 24h foram mantidas. As novas RN05 a RN10 são propostas de ampliação, não exigências explícitas do enunciado original.

## Verificação

- `node --check app.js` — sintaxe JavaScript verificada.
- `test_ui.py` — 18 verificações automatizadas de navegação/interação em navegador embutindo os arquivos; passaram sem erros JavaScript.
- `test_rules.py` — horário ocupado excluído e tentativa forçada de agendamento duplicado rejeitada.
- Documento Word renderizado em 10 páginas e inspecionado visualmente.

A abertura direta por URL `file://`/`localhost` foi bloqueada no ambiente de teste do assistente. Portanto, o teste automatizado utilizou conteúdo HTML/CSS/JS embutido no navegador; recomenda-se conferir a abertura e a persistência no seu navegador local antes da entrega.
