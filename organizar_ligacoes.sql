select * from atividades;

select * from evento;

insert into evento(id_evento, data_inicio, data_fim,nome,horas_dia,fornecido)
values
(0,'25/11/2018','31/12/2050','Evento de publicação',0,true);


select * from curso order by id_curso;


update curso set id_coordenador=16058 where id_curso=any ('{113641,92}');
update curso set id_coordenador=7366 where  id_curso=ANY ('{20,21,34}'::int[]);
update curso set id_coordenador=15956 where  id_curso=ANY ('{22,23}'::int[]);
update curso set id_coordenador=16053 where  id_curso=ANY ('{33}'::int[]);
update curso set id_coordenador=18985 where  id_curso=ANY ('{119693}'::int[]);
update curso set id_coordenador=17788 where  id_curso=ANY ('{67436,67434}'::int[]);
update curso set id_coordenador=13765 where  id_curso=ANY ('{60291}'::int[]);
update curso set id_coordenador=16009 where  id_curso=ANY ('{37,38,65}'::int[]);
update curso set id_coordenador=16036 where  id_curso=ANY ('{42}'::int[]);
update curso set id_coordenador=18858 where  id_curso=ANY ('{104846}'::int[]);
update curso set id_coordenador=16061 where  id_curso=ANY ('{36}'::int[]);
