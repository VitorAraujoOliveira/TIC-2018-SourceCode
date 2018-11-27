insert into atividade (id_atividade, data_inicio, data_fim, nome, horas_dia, numero_eventos)
	values
	(10000,'24/12/2018','25/12/2018','Natal',12,1),
	(10001,'31/12/2018','01/01/2019','Ano Novo',12,1),
	(10002,'21/11/2018','21/11/2018','Evento do dia',6,1),
	(10003,'11/10/2018','17/10/2018','Evento da semana',9.6,8);

insert into eventos (id_evento, id_atividade, nome_evento, data_evento, ds_evento, horas, tipo_evento)
	values
	('10000A',10000,'NATAL','25/12/2018','Festinha',12,'Outras horas'),
	('10001A',10001,'ANO NOVO','31/12/2018','Festinha',12,'Outras horas'),
	('10002A',10002,'EVENTO DO DIA','21/11/2018','Evento dia',6,'Horas palestra'),
	('10003A',10003,'EVENTO DA SEMANA','11/10/2018','Evento semana',3,'Horas palestras'),
	('10003B',10003,'EVENTO DA SEMANA','12/10/2018','Evento semana',3,'Horas cursos'),
	('10003C',10003,'EVENTO DA SEMANA','13/10/2018','Evento semana',3,'Horas cursos'),
	('10003D',10003,'EVENTO DA SEMANA','14/10/2018','Evento semana',3,'Horas voluntariado'),
	('10003E',10003,'EVENTO DA SEMANA','15/10/2018','Evento semana',3,'Horas palestras'),
	('10003F',10003,'EVENTO DA SEMANA','16/10/2018','Evento semana',3,'Horas empresa junior'),
	('100030',10003,'EVENTO DA SEMANA','16/10/2018','Evento semana',12,'Horas visita tecnica'),
	('100031',10003,'EVENTO DA SEMANA','17/10/2018','Evento semana',10,'Horas visita tecnica');

	select * from eventos;