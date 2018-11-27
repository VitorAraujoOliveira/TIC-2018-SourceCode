--primeiro se cria a tabela de curso
create table curso(
	id_curso integer,
	nome_curso varchar(120),
	id_coordenador integer,
	carga_horaria integer,
	data_criacao date,
	qtd_horas_extras integer,
	descricao text,
	constraint pk_curso primary key(id_curso)
	);



--em seguida a tabela de aluno
create table aluno(
	id_aluno integer,
	id_curso integer,
	nome_aluno varchar(120),
	login_ varchar(90),
	senha varchar(90),
	horas integer,
	quant_eventos integer,
	constraint pk_aluno primary key(id_aluno),
	constraint fk_aluno_curso foreign key(id_curso) references curso(id_curso)
	);


select * from aluno;

--em seguida atividade
create table evento(
	id_evento serial,
	data_inicio date,
	data_fim date,
	nome varchar,
	local_evento varchar,
	horas_dia integer,
	numero_atividades integer,
	fornecido boolean default true,
	constraint pk_evento primary key(id_evento)
	);



create table atividades(
	id_atividade serial,
	id_evento integer,
	nome_atividade varchar,
	tipo_atividade varchar(20),
	horas integer,
	fornecido boolean default true,
	data_atividade date,
	ds_atividade text,
	constraint pk_atividade primary key(id_atividade),
	constraint fk_atividade_evento foreign key(id_evento) references evento(id_evento)
	);



create table imagens(
	id_imagem serial,
	id_atividade integer,
	id_aluno integer,
	nome_imagem varchar,
	tipo_imagem varchar(8),
	imagem_path varchar,
	constraint pk_imagem primary key(id_imagem),
	constraint fk_imagem_aluno foreign key (id_aluno) references aluno(id_aluno),
	constraint fk_imagem_atividade foreign key(id_atividade) references atividades(id_atividade)
	);


create table aluno_frequenta_atividade(
	id_aluno integer,
	id_atividade integer,
	aprovacao boolean default false,
	constraint pk_aluno_atividade primary key(id_aluno,id_atividade),
	constraint fk_aluno_frequenta foreign key (id_aluno) references aluno(id_aluno),
	constraint fk_atividade_frequentada foreign key (id_atividade) references atividades(id_atividade)
	);

create table curso_tem_evento(
	id_curso integer,
	id_evento integer,
	id_coordenador integer,
	constraint pk_curso_tem_evento primary key(id_curso,id_evento),
	constraint fk_curso_tem_evento foreign key (id_curso) references curso(id_curso),
	constraint fk_evento_faz_parte_curso foreign key (id_evento) references evento(id_evento)	
	);


