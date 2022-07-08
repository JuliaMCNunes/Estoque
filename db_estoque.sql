create database estoque;
use estoque;

create table Fabricantes (
codigo int auto_increment,
nome varchar(60),
cnpj varchar(60),
razao_social varchar(60),
primary key (codigo));

create table Produtos (
cod int auto_increment,
descricao varchar(100),
valor float,
quantidade int, 
codigo_fabricante int not null, 
primary key (cod, codigo_fabricante));

alter table Produtos add foreign key (codigo_fabricante) references Fabricantes(codigo);

create table Entrada (
cod int auto_increment,
primary key (cod));

create table Saida (
cod int auto_increment,
primary key (cod));

select * from Produtos;
select * from Fabricantes;
