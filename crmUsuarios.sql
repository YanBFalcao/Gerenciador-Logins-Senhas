CREATE DATABASE crmUsuarios

USE crmUsuarios


CREATE TABLE usuariosSistema
	(
		id_usuario INT,

		usuario VARCHAR (50),
		senha VARCHAR (15),


	)

CREATE TABLE bancos
	(
		id_banco INT,

		nome_banco VARCHAR (50) NOT NULL,
		codigo_banco INT NOT NULL,
		


	)

CREATE TABLE usuariosBancos
	(
		id_usuario_banco INT,

		login_usuario_banco VARCHAR (50) NOT NULL,
		senha_usuario_banco VARCHAR (50) NOT NULL,
		data_atualizacao_usuario_banco DATE NOT NULL,

		observacao1_usuario_banco VARCHAR (50) NOT NULL,
		observacao2_usuario_banco VARCHAR (50) NOT NULL,

		visao_loja_usuario_banco VARCHAR (4) NOT NULL,
		robo_usuario_banco VARCHAR (4) NOT NULL,
		aprovador_usuario_banco VARCHAR (4) NOT NULL,


)

CREATE TABLE usuariosCertificados
	(
		id_usuariosCertificados INT,

		nome_usuario_certificado VARCHAR (50) NOT NULL,
		cpf_usuario_certificado VARCHAR (11) NOT NULL,
		numero_certificado_usuario_certificado VARCHAR (50),
		lgpd_usuario_certificado VARCHAR (4),
		pldft_usuario_certificado VARCHAR (4),
		data_validade_usuario_certificado DATE,
		
		rg_usuario_certificado VARCHAR (15) NOT NULL,
		telefone_usuario_certificado INT NOT NULL,
		nome_mae_usuario_certificado VARCHAR (15) NOT NULL,
		nome_pai_usuario_certificado VARCHAR (15) NOT NULL,





	)

CREATE TABLE promotoras
	(
		id_promotora INT,

		nome_promotora VARCHAR (50) NOT NULL,
		codigo_parceiro_promotora INT NOT NULL,

		CONSTRAINT fk1_promotoras FOREIGN KEY () REFERENCES (),
		CONSTRAINT fk2_promotoras FOREIGN KEY () REFERENCES (),
		CONSTRAINT fk3_promotoras FOREIGN KEY () REFERENCES (),
		CONSTRAINT fk4_promotoras FOREIGN KEY () REFERENCES (),

	)
