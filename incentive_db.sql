-- MySQL dump 10.13  Distrib 5.5.58, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: incentive_db
-- ------------------------------------------------------
-- Server version	5.5.58-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('6ecdff2e21f1');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attendances`
--

DROP TABLE IF EXISTS `attendances`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attendances` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `att_employee_id` int(11) DEFAULT NULL,
  `leave_days` int(11) DEFAULT NULL,
  `days_present` int(11) DEFAULT NULL,
  `percentage_attendance` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `att_employee_id` (`att_employee_id`),
  CONSTRAINT `attendances_ibfk_1` FOREIGN KEY (`att_employee_id`) REFERENCES `employees` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendances`
--

LOCK TABLES `attendances` WRITE;
/*!40000 ALTER TABLE `attendances` DISABLE KEYS */;
/*!40000 ALTER TABLE `attendances` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employees` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_number` varchar(10) DEFAULT NULL,
  `username` varchar(60) DEFAULT NULL,
  `emp_name` varchar(100) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `emp_project_id` int(11) DEFAULT NULL,
  `emp_subproject_id` int(11) DEFAULT NULL,
  `emp_role_id` int(11) DEFAULT NULL,
  `is_admin` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_employees_emp_number` (`emp_number`),
  UNIQUE KEY `ix_employees_username` (`username`),
  KEY `emp_project_id` (`emp_project_id`),
  KEY `emp_role_id` (`emp_role_id`),
  KEY `emp_subproject_id` (`emp_subproject_id`),
  KEY `ix_employees_emp_name` (`emp_name`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`emp_project_id`) REFERENCES `projects` (`id`),
  CONSTRAINT `employees_ibfk_2` FOREIGN KEY (`emp_role_id`) REFERENCES `roles` (`id`),
  CONSTRAINT `employees_ibfk_3` FOREIGN KEY (`emp_subproject_id`) REFERENCES `subprojects` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `incentives`
--

DROP TABLE IF EXISTS `incentives`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `incentives` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `inc_employee_id` int(11) DEFAULT NULL,
  `inc_subproject_id` int(11) DEFAULT NULL,
  `inc_attendances_id` int(11) DEFAULT NULL,
  `production` int(11) DEFAULT NULL,
  `av_qa_score` int(11) DEFAULT NULL,
  `total_points` int(11) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `inc_attendances_id` (`inc_attendances_id`),
  KEY `inc_employee_id` (`inc_employee_id`),
  KEY `inc_subproject_id` (`inc_subproject_id`),
  CONSTRAINT `incentives_ibfk_1` FOREIGN KEY (`inc_attendances_id`) REFERENCES `attendances` (`id`),
  CONSTRAINT `incentives_ibfk_2` FOREIGN KEY (`inc_employee_id`) REFERENCES `employees` (`id`),
  CONSTRAINT `incentives_ibfk_3` FOREIGN KEY (`inc_subproject_id`) REFERENCES `subprojects` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `incentives`
--

LOCK TABLES `incentives` WRITE;
/*!40000 ALTER TABLE `incentives` DISABLE KEYS */;
/*!40000 ALTER TABLE `incentives` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `pro_employee_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `pro_employee_id` (`pro_employee_id`),
  CONSTRAINT `projects_ibfk_1` FOREIGN KEY (`pro_employee_id`) REFERENCES `employees` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects`
--

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subprojects`
--

DROP TABLE IF EXISTS `subprojects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subprojects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `sp_project_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `sp_project_id` (`sp_project_id`),
  CONSTRAINT `subprojects_ibfk_1` FOREIGN KEY (`sp_project_id`) REFERENCES `projects` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subprojects`
--

LOCK TABLES `subprojects` WRITE;
/*!40000 ALTER TABLE `subprojects` DISABLE KEYS */;
/*!40000 ALTER TABLE `subprojects` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-13  6:06:06
