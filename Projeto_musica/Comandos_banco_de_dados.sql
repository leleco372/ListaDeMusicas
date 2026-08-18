create database playMusica;

use playMusica;

create table Musica(
	id int primary key auto_increment not null,
    nome varchar(50) not null,
    cantor_banda varchar(50) not null,
    genero varchar(50) not null);
    
insert into Musica(nome, cantor_banda, genero)
VALUES
('Blinding Lights', 'The Weeknd', 'Pop'),
('Shape of You', 'Ed Sheeran', 'Pop'),
('Smells Like Teen Spirit', 'Nirvana', 'Rock'),
('Despacito', 'Luis Fonsi', 'Reggaeton');
    
select * from Musica;
select * from usuario;

update Musica set genero = 'pop country' where id = 2;

delete from Musica where id=5;

create table usuario( 
id_usuario int primary key auto_increment not null,
nome_usuario varchar(50) not null,
senha_usuario varchar(15) not null,
login_usuario varchar(50) not null);

insert into usuario(nome_usuario, senha_usuario, login_usuario)
values
('leandro', 'popa123456', 'lelleco'),
('joao', 'joao123456', 'joaosilva'),
('maria', 'maria123456', 'mariinha'),
('carlos', 'carlos123456', 'carlosdev'),
('ana', 'ana123456', 'aninha'),
('pedro', 'pedro123456', 'pedrinho');

truncate table usuario;

alter table usuario
add unique(login_usuario);

insert into usuario(nome_usuario, senha_usuario, login_usuario)
values
('leandro', 'popa123456', 'lelleco'),
('joao', 'joao123456', 'joaosilva'),
('maria', 'maria123456', 'mariinha'),
('carlos', 'carlos123456', 'carlosdev'),
('ana', 'ana123456', 'aninha'),
('pedro', 'pedro123456', 'pedrinho');









