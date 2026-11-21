# MediCare 2.0 — registro de verificação

Data: 19/11/2026. A execução foi realizada com navegador Chromium em ambiente isolado, por meio de HTML/CSS/JavaScript embutidos na página de teste.

## Testes automatizados concluídos

- 18 verificações de interface e fluxos: página inicial do paciente, troca de identidade, tela de agendamento, filtro de médicos por especialidade, disponibilidade, confirmação, isolamento entre pacientes, acesso da recepção à agenda geral e a agendamentos, escopo de acesso do médico, registro de atendimento, navegação mobile e ausência de exceções JS.
- Verificação adicional: horário já confirmado não aparece como livre, e tentativa forçada de confirmar o mesmo horário é rejeitada.
- Verificação adicional: cancelamento de consulta futura própria altera a situação e libera o horário anteriormente ocupado.
- Sintaxe JavaScript verificada por Node.js.
- Documento Word renderizado em 10 páginas para revisão de layout.

## Limitação do teste

A política do ambiente impediu a navegação para endereços `file://` e `localhost`. O teste foi feito com os arquivos embutidos no navegador. O comportamento de persistência via `localStorage` não pôde ser verificado nesse ambiente; o código de persistência foi implementado, mas deve ser testado pelo usuário no navegador real. Assim, a entrega não equivale à validação de um sistema em produção.
