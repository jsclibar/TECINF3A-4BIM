/* Comandos DDL (Data Definition Language) */

create database escola_abc;
use escola_abc;

/* cria a tabela aluno dentro do banco de dados */

/* brModelo: */


CREATE TABLE ALUNO (
    idade int,
    endereco text,
    sexo char(1),
    telefone varchar(25),
    nome varchar(50),
    data_inscricao_curso date,
    valor_pago_curso float(10,2),
    ativo_sn int,
    id_aluno int autoincrement PRIMARY KEY
);

show tables; /* exibe as tabelas existentes no banco de dados */
drop table aluno; /* remove a tabela aluno */

/* Modificar a estrura de uma tabela */

desc aluno;
alter table aluno add cpf varchar(11);
alter table aluno add email varchar(150) after idade;
alter table aluno modify column cpf varchar(14);
alter table aluno drop column cpf;
alter table aluno add cpf varchar(14) after email;

/* Comandos DML (Data Manipulation Language) */
/* Inserindo registros no banco de dados */

insert into aluno(
	sexo, idade, data_inscricao_curso, telefone, valor_pago_curso,
    ativo_sn, endereco, nome
)values(
	'M', 55, '2018-12-01', '11 5555-2222', 645.22,
	1, 'Avenida Paulista, 1500, ap315 - São Paulo - SP', 'João'
);

insert into aluno(
	sexo, idade, data_inscricao_curso, telefone, valor_pago_curso,
    ativo_sn, endereco, nome
)values(
	'F', 30, '2018-11-01', '11 3333-2222', 589.12,
	1, 'Rua Francisco Sá, 10 - Belo Horizonte - MG', 'Fernanda'
);

insert into aluno(
	sexo, idade, data_inscricao_curso, telefone, valor_pago_curso,
    ativo_sn, endereco, nome
)values(
	'M', 29, '2018-12-02', '11 3333-7777', 600.55,
	0, 'Avenida Dom Manuel, 300 - Fortaleza - CE', 'José'
);

insert into aluno(
	sexo, idade, data_inscricao_curso, telefone, valor_pago_curso,
    ativo_sn, endereco, nome
)values(
	'M', 37, '2018-11-15', '11 1111-7777', 612.99,
	1, 'Rua João de Abreu, 650 - Goiania - GO', 'Marcelo'
);

insert into aluno(
	sexo, idade, data_inscricao_curso, telefone, valor_pago_curso,
    ativo_sn, endereco, nome
)values(
	'F', 42, '2018-12-02', '11 7777-7777', 612.99,
	1, 'Rua Miramar, 1200, ap112 - Natal - RN', 'Maria'
);

/* atualizando registros */

update aluno set ativo_sn = 0 where nome = 'João';
update aluno set ativo_sn = 1, valor_pago_curso = 750 where nome = 'José';
update aluno set telefone =  '11 8888-4444' where telefone = '11 7777-7777';

/* deletando registros */

delete from aluno where ativo_sn = 0;
delete from aluno where ativo_sn = 0;
delete from aluno where idade in (30, 29);
delete from aluno where idade in (30, 29) or sexo = 'F';

/* Comandos DQL (Data Query Language) */

Select * from aluno
select nome, telefone from aluno;
