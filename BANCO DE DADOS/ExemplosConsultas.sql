-- 1) Tudo de todo mundo
SELECT * FROM aluno;

-- 2) Só alguns campos
SELECT nome, idade, sexo FROM aluno;

-- 3) Eliminar duplicados (ex.: endereços repetidos)
SELECT DISTINCT endereco FROM aluno;

-- 4) Ordenação simples (A→Z)
SELECT nome, idade FROM aluno ORDER BY nome ASC;

-- 5) Ordenação múltipla (por sexo e, dentro, por idade decrescente)
SELECT nome, sexo, idade FROM aluno ORDER BY sexo, idade DESC;

-- 6) Limitar resultados (os 10 primeiros)
SELECT nome, idade FROM aluno ORDER BY idade DESC LIMIT 10;

-- 7) Paginação (pule 20, traga 10)
SELECT nome, idade FROM aluno ORDER BY nome LIMIT 10 OFFSET 20;

-- 8) Alunos maiores de 30 anos
SELECT nome, idade FROM aluno WHERE idade > 30;

-- 9) Idade entre 20 e 25 (inclusive)
SELECT nome, idade FROM aluno WHERE idade BETWEEN 20 AND 25;

-- 10) Sexo feminino OU idade 18 ou 19
SELECT nome, sexo, idade FROM aluno
WHERE sexo = 'F' OR idade IN (18, 19);

-- 11) Somente ativos (ativo_sn = 1)
SELECT nome, ativo_sn FROM aluno WHERE ativo_sn = 1;

-- 12) Nomes que começam com 'Ca'
SELECT nome FROM aluno WHERE nome LIKE 'Ca%';

-- 13) Nomes que terminam com 'a'
SELECT nome FROM aluno WHERE nome LIKE '%a';

-- 14) Endereços contendo 'Av.'
SELECT nome, endereco FROM aluno WHERE endereco LIKE '%Av.%';

-- 15) Telefones do DDD 11 (começam com '11')
SELECT nome, telefone FROM aluno WHERE telefone LIKE '11%';

-- 16) Registros sem telefone (pouco provável aqui, mas didático)
SELECT nome FROM aluno WHERE telefone IS NULL;

-- 17) Inscritos em 2025
SELECT nome, data_inscricao_curso
FROM aluno
WHERE YEAR(data_inscricao_curso) = 2025;

-- 18) Inscritos no 1º trimestre de 2025
SELECT nome, data_inscricao_curso
FROM aluno
WHERE data_inscricao_curso >= '2025-01-01'
  AND data_inscricao_curso <  '2025-04-01';

-- 19) Inscritos em fevereiro (de qualquer ano)
SELECT nome, data_inscricao_curso
FROM aluno
WHERE MONTH(data_inscricao_curso) = 2;

-- 20) Dia da semana da inscrição (MySQL: 1=domingo … 7=sábado com DAYOFWEEK)
SELECT nome, data_inscricao_curso, DAYOFWEEK(data_inscricao_curso) AS dia_semana
FROM aluno;

-- 22) Média, mínimo e máximo do valor pago
SELECT
  ROUND(AVG(valor_pago_curso), 2) AS media,
  MIN(valor_pago_curso) AS menor,
  MAX(valor_pago_curso) AS maior
FROM aluno;

-- 23) Total arrecadado
SELECT ROUND(SUM(valor_pago_curso), 2) AS total
FROM aluno;

-- 24) Distribuição por faixas de preço (com CASE)
SELECT
  CASE
    WHEN valor_pago_curso < 500 THEN 'Abaixo de 500'
    WHEN valor_pago_curso < 800 THEN '500 a 799,99'
    WHEN valor_pago_curso < 1000 THEN '800 a 999,99'
    ELSE '1000 ou mais'
  END AS faixa_preco,
  COUNT(*) AS qtd
FROM aluno
GROUP BY faixa_preco
ORDER BY qtd DESC;

-- 25) Quantos alunos por sexo
SELECT sexo, COUNT(*) AS qtd
FROM aluno
GROUP BY sexo;

-- 26) Ticket médio por sexo
SELECT sexo, ROUND(AVG(valor_pago_curso), 2) AS media_valor
FROM aluno
GROUP BY sexo;

-- 27) Idade média por status (ativo x inativo)
SELECT ativo_sn, ROUND(AVG(idade), 1) AS idade_media
FROM aluno
GROUP BY ativo_sn;

-- 28) Somente grupos com média acima de R$ 800
SELECT sexo, ROUND(AVG(valor_pago_curso), 2) AS media_valor
FROM aluno
GROUP BY sexo
HAVING AVG(valor_pago_curso) > 800;

-- 29) Extrair primeiro nome (até o primeiro espaço)
SELECT
  nome,
  SUBSTRING_INDEX(nome, ' ', 1) AS primeiro_nome
FROM aluno;

-- 30) Contar quantos têm sobrenome 'Silva'
SELECT COUNT(*) AS qtd_silva
FROM aluno
WHERE nome LIKE '% Silva';

-- 31) Normalizar para MAIÚSCULAS (demonstração)
SELECT UPPER(nome) AS nome_maiusculo
FROM aluno
LIMIT 10;

-- 32) Quem paga acima da média geral
SELECT nome, valor_pago_curso
FROM aluno
WHERE valor_pago_curso > (
  SELECT AVG(valor_pago_curso) FROM aluno
)
ORDER BY valor_pago_curso DESC;

-- 33) Alunos com idade máxima (pega a maior e retorna todos que a possuem)
SELECT nome, idade
FROM aluno
WHERE idade = (SELECT MAX(idade) FROM aluno);

-- 34) Conferir quantos seriam removidos por um filtro (ANTES de um DELETE real)
SELECT COUNT(*) AS candidatos
FROM aluno
WHERE sexo = 'F' OR idade IN (29, 30);