-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           5.7.19 - MySQL Community Server (GPL)
-- OS do Servidor:               Win64
-- HeidiSQL Versão:              9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Copiando estrutura do banco de dados para inclass
CREATE DATABASE IF NOT EXISTS `inclass` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `inclass`;

-- Copiando estrutura para tabela inclass.absence
CREATE TABLE IF NOT EXISTS `absence` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `absence_number` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `lecture_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `absence_lecture_id_student_id_cc6bb99d_uniq` (`lecture_id`,`student_id`),
  KEY `absence_student_id_ee9ee8fd_fk_person_id` (`student_id`),
  CONSTRAINT `absence_lecture_id_786c105f_fk_lecture_id` FOREIGN KEY (`lecture_id`) REFERENCES `lecture` (`id`),
  CONSTRAINT `absence_student_id_ee9ee8fd_fk_person_id` FOREIGN KEY (`student_id`) REFERENCES `person` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.absence: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `absence` DISABLE KEYS */;
INSERT INTO `absence` (`id`, `absence_number`, `is_deleted`, `lecture_id`, `student_id`) VALUES
	(1, 3, 0, 1, 8),
	(2, 3, 0, 1, 4),
	(3, 2, 0, 1, 5),
	(4, 3, 0, 1, 6),
	(5, 4, 0, 1, 7),
	(6, 4, 0, 2, 8),
	(7, 4, 0, 2, 4),
	(8, 4, 0, 2, 5),
	(9, 4, 0, 2, 6),
	(10, 4, 0, 2, 7),
	(11, 4, 0, 3, 8),
	(12, 4, 0, 3, 4),
	(13, 4, 0, 3, 5),
	(14, 4, 0, 3, 6),
	(15, 4, 0, 3, 7),
	(16, 4, 0, 4, 8),
	(17, 2, 0, 4, 4),
	(18, 3, 0, 4, 5),
	(19, 3, 0, 4, 6),
	(20, 2, 0, 4, 7),
	(21, 4, 0, 5, 8),
	(22, 3, 0, 5, 4),
	(23, 2, 0, 5, 5),
	(24, 1, 0, 5, 6),
	(25, 2, 0, 5, 7);
/*!40000 ALTER TABLE `absence` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.address
CREATE TABLE IF NOT EXISTS `address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `street` varchar(200) NOT NULL,
  `number` int(11) NOT NULL,
  `district` varchar(200) NOT NULL,
  `city` varchar(200) NOT NULL,
  `state` varchar(200) NOT NULL,
  `postal_code` varchar(200) NOT NULL,
  `complement` varchar(200) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `institution_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `address_institution_id_42361745_fk_institution_id` (`institution_id`),
  CONSTRAINT `address_institution_id_42361745_fk_institution_id` FOREIGN KEY (`institution_id`) REFERENCES `institution` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.address: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address` (`id`, `street`, `number`, `district`, `city`, `state`, `postal_code`, `complement`, `is_deleted`, `institution_id`) VALUES
	(1, 'Avenida Mauro Ramos', 200, '', 'Florianopolis', 'SC', '88008008', 'Ao lado do SESC', 0, 1);
/*!40000 ALTER TABLE `address` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.authtoken_token
CREATE TABLE IF NOT EXISTS `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.authtoken_token: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
INSERT INTO `authtoken_token` (`key`, `created`, `user_id`) VALUES
	('0d3cdcc246e2b3835c9fb53b5bc6bd66529633f9', '2018-07-03 22:44:46.845000', 4),
	('380566518cfc1e3b4d6736339abd9a93a603f36c', '2018-07-03 22:44:47.542000', 7),
	('5094a7f0b6912588263674810b2ef7c6221b59ef', '2018-07-03 22:44:47.066000', 5),
	('51b1bce85d404447bb8bf83bf725709819b581e9', '2018-07-03 22:39:53.248000', 1),
	('548e3deece6ec5ac952155dc039531a22c0f5ff7', '2018-07-03 22:44:46.425000', 3),
	('5dc4854ad6eb9cf3bc00dc00cfa6206a0ad45559', '2018-07-03 22:44:47.310000', 6),
	('8bbf233d552cb60234d76edb0983b1cd3d89daa2', '2018-07-03 22:44:47.752000', 8),
	('b4087ab1f5dd3cb6e87d4f8e8314d91995ef362b', '2018-07-03 22:44:45.727000', 2);
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.auth_group
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.auth_group: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.auth_group_permissions
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.auth_group_permissions: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.auth_permission
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.auth_permission: ~54 rows (aproximadamente)
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can add group', 2, 'add_group'),
	(5, 'Can change group', 2, 'change_group'),
	(6, 'Can delete group', 2, 'delete_group'),
	(7, 'Can add permission', 3, 'add_permission'),
	(8, 'Can change permission', 3, 'change_permission'),
	(9, 'Can delete permission', 3, 'delete_permission'),
	(10, 'Can add user', 4, 'add_user'),
	(11, 'Can change user', 4, 'change_user'),
	(12, 'Can delete user', 4, 'delete_user'),
	(13, 'Can add content type', 5, 'add_contenttype'),
	(14, 'Can change content type', 5, 'change_contenttype'),
	(15, 'Can delete content type', 5, 'delete_contenttype'),
	(16, 'Can add session', 6, 'add_session'),
	(17, 'Can change session', 6, 'change_session'),
	(18, 'Can delete session', 6, 'delete_session'),
	(19, 'Can add falta', 7, 'add_absence'),
	(20, 'Can change falta', 7, 'change_absence'),
	(21, 'Can delete falta', 7, 'delete_absence'),
	(22, 'Can add instituição', 8, 'add_institution'),
	(23, 'Can change instituição', 8, 'change_institution'),
	(24, 'Can delete instituição', 8, 'delete_institution'),
	(25, 'Can add endereço', 9, 'add_address'),
	(26, 'Can change endereço', 9, 'change_address'),
	(27, 'Can delete endereço', 9, 'delete_address'),
	(28, 'Can add disciplina', 10, 'add_subject'),
	(29, 'Can change disciplina', 10, 'change_subject'),
	(30, 'Can delete disciplina', 10, 'delete_subject'),
	(31, 'Can add pessoa', 11, 'add_person'),
	(32, 'Can change pessoa', 11, 'change_person'),
	(33, 'Can delete pessoa', 11, 'delete_person'),
	(34, 'Has professor permissions', 11, 'is_professor'),
	(35, 'Has student permissions', 11, 'is_student'),
	(36, 'Has administrator permissions', 11, 'is_admin'),
	(37, 'Can add aula', 12, 'add_lecture'),
	(38, 'Can change aula', 12, 'change_lecture'),
	(39, 'Can delete aula', 12, 'delete_lecture'),
	(40, 'Can add configuração do sistemas', 13, 'add_systemconfig'),
	(41, 'Can change configuração do sistemas', 13, 'change_systemconfig'),
	(42, 'Can delete configuração do sistemas', 13, 'delete_systemconfig'),
	(43, 'Can add contestação', 14, 'add_dispute'),
	(44, 'Can change contestação', 14, 'change_dispute'),
	(45, 'Can delete contestação', 14, 'delete_dispute'),
	(46, 'Can add curso', 15, 'add_course'),
	(47, 'Can change curso', 15, 'change_course'),
	(48, 'Can delete curso', 15, 'delete_course'),
	(49, 'Can add turma', 16, 'add_group'),
	(50, 'Can change turma', 16, 'change_group'),
	(51, 'Can delete turma', 16, 'delete_group'),
	(52, 'Can add Token', 17, 'add_token'),
	(53, 'Can change Token', 17, 'change_token'),
	(54, 'Can delete Token', 17, 'delete_token');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.auth_user
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.auth_user: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$36000$QLGkKFNmmiDb$T+pWyfEAde9uu7d3FDfrEveUL8DKbncXQvw01WjRqfc=', NULL, 1, 'admin', 'Felipe', 'Admin', 'lipe.menezes@live.com', 1, 1, '2018-07-03 22:39:53.048000'),
	(2, 'pbkdf2_sha256$36000$FYNLbc6QJWKx$XgdVyjZp1zrcLoNAD1RYKkgkEfqUZrxf2vqMbvTnyDE=', NULL, 0, '123', 'Vilmar', 'Pereira', 'vilmar.junior@edu.sc.senac.br', 0, 1, '2018-07-03 22:44:45.629000'),
	(3, 'pbkdf2_sha256$36000$qKz4nJTC8qXq$1vSFA01/TrmEdPgIIgoZve33ExgvLdwe0kFytnlFryc=', NULL, 0, '456', 'Luciano', 'Kogut', 'luciano.kogut@sc.senac.br', 0, 1, '2018-07-03 22:44:46.317000'),
	(4, 'pbkdf2_sha256$36000$G8TPCjuaQLhR$BN3elsMKW/zc2tFDiNd7o4MNK6miSzEYVtXOWXukTB8=', NULL, 0, '100', 'Felipe', 'Menezes', 'lipe.menezes@live.com', 0, 1, '2018-07-03 22:44:46.770000'),
	(5, 'pbkdf2_sha256$36000$A2pPpnrYBYYh$p9L8tiQshrYaaJqt1MMR/rLTOWfLXBX/F/GpbWxAz2U=', NULL, 0, '101', 'Maicon', 'Queiroz', 'maiconqdev@gmail.com', 0, 1, '2018-07-03 22:44:47.001000'),
	(6, 'pbkdf2_sha256$36000$dHd1YHHHnUpX$ixYAl/7h8YQ2i80JMcKy/Ly/hzWpO79+cHUYoqLa5TI=', NULL, 0, '102', 'Bruno', 'Gehrke', 'brunovitorr@gmail.com', 0, 1, '2018-07-03 22:44:47.226000'),
	(7, 'pbkdf2_sha256$36000$AVnUaTYN0zCq$liTYBD2nS3IpsgNtakWIza7XbZLPMANcQ808xf1BwZk=', NULL, 0, '103', 'Guilherme', 'Rodrigues', 'guilherme121225@gmail.com', 0, 1, '2018-07-03 22:44:47.478000'),
	(8, 'pbkdf2_sha256$36000$EVHrmfz4jtym$vmHNHPoOfvkFWf11fsK27DfLs2IJeyRn8GbDI6L0O6I=', NULL, 0, '104', 'Ana', 'Luiza Negri', 'analuizanegri@gmail.com', 0, 1, '2018-07-03 22:44:47.677000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.auth_user_groups
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.auth_user_groups: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.auth_user_user_permissions
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.auth_user_user_permissions: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
INSERT INTO `auth_user_user_permissions` (`id`, `user_id`, `permission_id`) VALUES
	(1, 2, 34),
	(3, 3, 34),
	(2, 3, 35),
	(4, 3, 36),
	(5, 4, 35),
	(6, 5, 35),
	(7, 6, 35),
	(8, 7, 35),
	(9, 8, 35);
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.course
CREATE TABLE IF NOT EXISTS `course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `initials` varchar(14) NOT NULL,
  `external_code` varchar(200) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `institution_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `course_institution_id_f8408a49_fk_institution_id` (`institution_id`),
  CONSTRAINT `course_institution_id_f8408a49_fk_institution_id` FOREIGN KEY (`institution_id`) REFERENCES `institution` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.course: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` (`id`, `name`, `initials`, `external_code`, `is_deleted`, `institution_id`) VALUES
	(1, 'Análise e Desenvolvimento de Sistemas', 'ADS', 'ADS', 0, 1),
	(2, 'Gestão em TI', 'TGTI', 'TGTI', 0, 1),
	(3, 'Processos Gerenciais', 'PG', 'PG', 0, 1);
/*!40000 ALTER TABLE `course` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.dispute
CREATE TABLE IF NOT EXISTS `dispute` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` varchar(200) NOT NULL,
  `status` int(11) NOT NULL,
  `initial_absence_number` int(11) NOT NULL,
  `final_absence_number` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `absence_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dispute_absence_id_e394fe69_fk_absence_id` (`absence_id`),
  CONSTRAINT `dispute_absence_id_e394fe69_fk_absence_id` FOREIGN KEY (`absence_id`) REFERENCES `absence` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.dispute: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `dispute` DISABLE KEYS */;
INSERT INTO `dispute` (`id`, `message`, `status`, `initial_absence_number`, `final_absence_number`, `is_deleted`, `absence_id`) VALUES
	(1, 'Professor, nesse dia tive apenas uma falta, pois cheguei as 08:20! Pode arrumar, por favor?', 0, 3, 0, 0, 2),
	(2, 'Professor, ja que deu essa falta por engano, ajuda na banca ai rsrs', 1, 4, 2, 0, 17),
	(3, 'Professor, eu so tive duas faltas!', 2, 4, 4, 0, 12),
	(4, ':(', 0, 4, 4, 0, 7);
/*!40000 ALTER TABLE `dispute` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.django_admin_log: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.django_content_type
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.django_content_type: ~17 rows (aproximadamente)
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(2, 'auth', 'group'),
	(3, 'auth', 'permission'),
	(4, 'auth', 'user'),
	(17, 'authtoken', 'token'),
	(5, 'contenttypes', 'contenttype'),
	(7, 'inclass_server', 'absence'),
	(9, 'inclass_server', 'address'),
	(15, 'inclass_server', 'course'),
	(14, 'inclass_server', 'dispute'),
	(16, 'inclass_server', 'group'),
	(8, 'inclass_server', 'institution'),
	(12, 'inclass_server', 'lecture'),
	(11, 'inclass_server', 'person'),
	(10, 'inclass_server', 'subject'),
	(13, 'inclass_server', 'systemconfig'),
	(6, 'sessions', 'session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.django_migrations
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.django_migrations: ~21 rows (aproximadamente)
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2018-07-03 22:32:33.582000'),
	(2, 'auth', '0001_initial', '2018-07-03 22:32:42.913000'),
	(3, 'admin', '0001_initial', '2018-07-03 22:32:44.748000'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2018-07-03 22:32:44.802000'),
	(5, 'contenttypes', '0002_remove_content_type_name', '2018-07-03 22:32:46.290000'),
	(6, 'auth', '0002_alter_permission_name_max_length', '2018-07-03 22:32:46.433000'),
	(7, 'auth', '0003_alter_user_email_max_length', '2018-07-03 22:32:46.589000'),
	(8, 'auth', '0004_alter_user_username_opts', '2018-07-03 22:32:46.638000'),
	(9, 'auth', '0005_alter_user_last_login_null', '2018-07-03 22:32:47.555000'),
	(10, 'auth', '0006_require_contenttypes_0002', '2018-07-03 22:32:47.624000'),
	(11, 'auth', '0007_alter_validators_add_error_messages', '2018-07-03 22:32:47.723000'),
	(12, 'auth', '0008_alter_user_username_max_length', '2018-07-03 22:32:48.037000'),
	(13, 'authtoken', '0001_initial', '2018-07-03 22:32:49.582000'),
	(14, 'authtoken', '0002_auto_20160226_1747', '2018-07-03 22:32:50.489000'),
	(15, 'inclass_server', '0001_initial', '2018-07-03 22:33:16.952000'),
	(16, 'inclass_server', '0002_auto_20180626_2037', '2018-07-03 22:33:20.135000'),
	(17, 'inclass_server', '0003_auto_20180626_2343', '2018-07-03 22:33:24.576000'),
	(18, 'inclass_server', '0004_group_sunday', '2018-07-03 22:33:25.060000'),
	(19, 'inclass_server', '0005_group_course', '2018-07-03 22:33:27.675000'),
	(20, 'inclass_server', '0006_systemconfig', '2018-07-03 22:33:28.846000'),
	(21, 'sessions', '0001_initial', '2018-07-03 22:33:31.435000');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.django_session: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.group
CREATE TABLE IF NOT EXISTS `group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) NOT NULL,
  `day_period` int(11) NOT NULL,
  `semester` int(11) NOT NULL,
  `start_at` date NOT NULL,
  `end_at` date NOT NULL,
  `external_code` varchar(200) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `subject_id` int(11) NOT NULL,
  `friday` tinyint(1) NOT NULL,
  `monday` tinyint(1) NOT NULL,
  `saturday` tinyint(1) NOT NULL,
  `thursday` tinyint(1) NOT NULL,
  `tuesday` tinyint(1) NOT NULL,
  `wednesday` tinyint(1) NOT NULL,
  `sunday` tinyint(1) NOT NULL,
  `course_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `group_subject_id_004bbf23_fk_subject_id` (`subject_id`),
  KEY `group_course_id_fae05f05_fk_course_id` (`course_id`),
  CONSTRAINT `group_course_id_fae05f05_fk_course_id` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`),
  CONSTRAINT `group_subject_id_004bbf23_fk_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.group: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `group` DISABLE KEYS */;
INSERT INTO `group` (`id`, `year`, `day_period`, `semester`, `start_at`, `end_at`, `external_code`, `is_deleted`, `subject_id`, `friday`, `monday`, `saturday`, `thursday`, `tuesday`, `wednesday`, `sunday`, `course_id`) VALUES
	(1, 2018, 0, 1, '2018-02-10', '2018-07-10', '0_ADS_20181_WEB', 0, 2, 1, 1, 0, 0, 0, 1, 0, 1),
	(2, 2018, 0, 1, '2018-02-09', '2018-07-15', '0_ADS_20181_ARC', 0, 3, 0, 1, 0, 0, 1, 0, 0, 1);
/*!40000 ALTER TABLE `group` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.group_instructors
CREATE TABLE IF NOT EXISTS `group_instructors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_instructors_group_id_person_id_7ce86f1e_uniq` (`group_id`,`person_id`),
  KEY `group_instructors_person_id_7d5892f4_fk_person_id` (`person_id`),
  CONSTRAINT `group_instructors_group_id_24304bf9_fk_group_id` FOREIGN KEY (`group_id`) REFERENCES `group` (`id`),
  CONSTRAINT `group_instructors_person_id_7d5892f4_fk_person_id` FOREIGN KEY (`person_id`) REFERENCES `person` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.group_instructors: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `group_instructors` DISABLE KEYS */;
INSERT INTO `group_instructors` (`id`, `group_id`, `person_id`) VALUES
	(1, 1, 2),
	(2, 1, 3),
	(3, 2, 2),
	(4, 2, 3);
/*!40000 ALTER TABLE `group_instructors` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.group_students
CREATE TABLE IF NOT EXISTS `group_students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_students_group_id_person_id_f687e183_uniq` (`group_id`,`person_id`),
  KEY `group_students_person_id_dbf2a2f4_fk_person_id` (`person_id`),
  CONSTRAINT `group_students_group_id_e69a4cbc_fk_group_id` FOREIGN KEY (`group_id`) REFERENCES `group` (`id`),
  CONSTRAINT `group_students_person_id_dbf2a2f4_fk_person_id` FOREIGN KEY (`person_id`) REFERENCES `person` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.group_students: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `group_students` DISABLE KEYS */;
INSERT INTO `group_students` (`id`, `group_id`, `person_id`) VALUES
	(2, 1, 4),
	(3, 1, 5),
	(4, 1, 6),
	(5, 1, 7),
	(1, 1, 8),
	(7, 2, 4),
	(8, 2, 5),
	(9, 2, 6),
	(10, 2, 7),
	(6, 2, 8);
/*!40000 ALTER TABLE `group_students` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.institution
CREATE TABLE IF NOT EXISTS `institution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `register` varchar(14) NOT NULL,
  `external_code` varchar(200) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.institution: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `institution` DISABLE KEYS */;
INSERT INTO `institution` (`id`, `name`, `register`, `external_code`, `is_deleted`) VALUES
	(1, 'SENAC', '24388736000147', '24388736000147', 0);
/*!40000 ALTER TABLE `institution` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.lecture
CREATE TABLE IF NOT EXISTS `lecture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `workload` int(11) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `group_id` int(11) NOT NULL,
  `instructor_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lecture_group_id_cf41a597_fk_group_id` (`group_id`),
  KEY `lecture_instructor_id_2cf63940_fk_person_id` (`instructor_id`),
  CONSTRAINT `lecture_group_id_cf41a597_fk_group_id` FOREIGN KEY (`group_id`) REFERENCES `group` (`id`),
  CONSTRAINT `lecture_instructor_id_2cf63940_fk_person_id` FOREIGN KEY (`instructor_id`) REFERENCES `person` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.lecture: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `lecture` DISABLE KEYS */;
INSERT INTO `lecture` (`id`, `date`, `workload`, `is_deleted`, `group_id`, `instructor_id`) VALUES
	(1, '2018-07-03', 4, 0, 1, 2),
	(2, '2018-07-04', 4, 0, 1, 2),
	(3, '2018-07-03', 4, 0, 2, 2),
	(4, '2018-07-05', 4, 0, 2, 2),
	(5, '2018-07-02', 4, 0, 1, 2);
/*!40000 ALTER TABLE `lecture` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.person
CREATE TABLE IF NOT EXISTS `person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `social_security_number` varchar(200) NOT NULL,
  `register` varchar(200) NOT NULL,
  `external_code` varchar(200) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  `is_new_password` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `person_user_id_1e34abe8_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.person: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` (`id`, `social_security_number`, `register`, `external_code`, `is_deleted`, `user_id`, `is_new_password`) VALUES
	(1, 'admin', 'admin', 'admin', 0, 1, 0),
	(2, '123', '26062018210635', '123', 0, 2, 0),
	(3, '456', '26062018210123', '456', 0, 3, 0),
	(4, '100', '26062018210635', '100', 0, 4, 0),
	(5, '101', '26062018210635', '101', 0, 5, 1),
	(6, '102', '26062018210635', '102', 0, 6, 1),
	(7, '103', '26062018210635', '103', 0, 7, 1),
	(8, '104', '26062018210635', '104', 0, 8, 1);
/*!40000 ALTER TABLE `person` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.subject
CREATE TABLE IF NOT EXISTS `subject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `initials` varchar(14) NOT NULL,
  `workload` int(11) NOT NULL,
  `external_code` varchar(200) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.subject: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `subject` DISABLE KEYS */;
INSERT INTO `subject` (`id`, `name`, `initials`, `workload`, `external_code`, `is_deleted`) VALUES
	(1, 'Desenvolvimento Mobile', 'MOB', 160, 'mob001', 0),
	(2, 'Desenvolvimento Web', 'WEB', 160, 'web001', 0),
	(3, 'Arquitetura de Redes e Computadores', 'ARC', 80, 'arc001', 0);
/*!40000 ALTER TABLE `subject` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.subject_courses
CREATE TABLE IF NOT EXISTS `subject_courses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `subject_courses_subject_id_course_id_88e4944e_uniq` (`subject_id`,`course_id`),
  KEY `subject_courses_course_id_7f5d30b7_fk_course_id` (`course_id`),
  CONSTRAINT `subject_courses_course_id_7f5d30b7_fk_course_id` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`),
  CONSTRAINT `subject_courses_subject_id_3262c08e_fk_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.subject_courses: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `subject_courses` DISABLE KEYS */;
INSERT INTO `subject_courses` (`id`, `subject_id`, `course_id`) VALUES
	(1, 1, 1),
	(2, 1, 2),
	(3, 2, 1),
	(4, 2, 2),
	(5, 3, 1),
	(6, 3, 2);
/*!40000 ALTER TABLE `subject_courses` ENABLE KEYS */;

-- Copiando estrutura para tabela inclass.system_config
CREATE TABLE IF NOT EXISTS `system_config` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `config` varchar(200) NOT NULL,
  `value` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Copiando dados para a tabela inclass.system_config: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `system_config` DISABLE KEYS */;
INSERT INTO `system_config` (`id`, `config`, `value`) VALUES
	(1, 'min_allowed_attendance', '75'),
	(2, 'email', 'naorespondainclass@gmail.com '),
	(3, 'email_pass', '#Abc123456');
/*!40000 ALTER TABLE `system_config` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
