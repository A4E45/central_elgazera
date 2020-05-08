CREATE DATABASE  IF NOT EXISTS `central_elgazera` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `central_elgazera`;
-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: central_elgazera
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accessories`
--

DROP TABLE IF EXISTS `accessories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accessories` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `value` int NOT NULL,
  `quantity` int NOT NULL,
  `_date` date NOT NULL,
  `_time` time NOT NULL,
  `EmployeeID` int NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `EmployeeID` (`EmployeeID`),
  KEY `order_id` (`order_id`),
  CONSTRAINT `accessories_ibfk_1` FOREIGN KEY (`EmployeeID`) REFERENCES `employee` (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accessories`
--

LOCK TABLES `accessories` WRITE;
/*!40000 ALTER TABLE `accessories` DISABLE KEYS */;
/*!40000 ALTER TABLE `accessories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accessories_stored`
--

DROP TABLE IF EXISTS `accessories_stored`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accessories_stored` (
  `accessoriesID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `price` int NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`accessoriesID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accessories_stored`
--

LOCK TABLES `accessories_stored` WRITE;
/*!40000 ALTER TABLE `accessories_stored` DISABLE KEYS */;
/*!40000 ALTER TABLE `accessories_stored` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `charge`
--

DROP TABLE IF EXISTS `charge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `charge` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `phone_number` varchar(255) NOT NULL,
  `value` float NOT NULL,
  `_date` date NOT NULL,
  `_time` time NOT NULL,
  `serviceID` int NOT NULL,
  `EmployeeID` int NOT NULL,
  `MachineID` int NOT NULL,
  KEY `EmployeeID` (`EmployeeID`),
  KEY `MachineID` (`MachineID`),
  KEY `serviceID` (`serviceID`),
  KEY `order_id` (`order_id`),
  CONSTRAINT `charge_ibfk_1` FOREIGN KEY (`EmployeeID`) REFERENCES `employee` (`EmployeeID`),
  CONSTRAINT `charge_ibfk_2` FOREIGN KEY (`MachineID`) REFERENCES `machines` (`MachineID`),
  CONSTRAINT `charge_ibfk_3` FOREIGN KEY (`serviceID`) REFERENCES `services` (`serviceID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `charge`
--

LOCK TABLES `charge` WRITE;
/*!40000 ALTER TABLE `charge` DISABLE KEYS */;
/*!40000 ALTER TABLE `charge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_names`
--

DROP TABLE IF EXISTS `company_names`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company_names` (
  `companyID` int NOT NULL AUTO_INCREMENT,
  `company_name` varchar(255) NOT NULL,
  PRIMARY KEY (`companyID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_names`
--

LOCK TABLES `company_names` WRITE;
/*!40000 ALTER TABLE `company_names` DISABLE KEYS */;
INSERT INTO `company_names` VALUES (1,'فودافون'),(2,'اورنج'),(3,'اتصالات'),(4,'WE');
/*!40000 ALTER TABLE `company_names` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dailymoment`
--

DROP TABLE IF EXISTS `dailymoment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dailymoment` (
  `moveID` int NOT NULL AUTO_INCREMENT,
  `EmployeeID` int NOT NULL,
  `_move` varchar(255) NOT NULL,
  `_date` date NOT NULL,
  `_time` time NOT NULL,
  PRIMARY KEY (`moveID`),
  KEY `EmployeeID` (`EmployeeID`),
  CONSTRAINT `dailymoment_ibfk_1` FOREIGN KEY (`EmployeeID`) REFERENCES `employee` (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dailymoment`
--

LOCK TABLES `dailymoment` WRITE;
/*!40000 ALTER TABLE `dailymoment` DISABLE KEYS */;
/*!40000 ALTER TABLE `dailymoment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elec_cards`
--

DROP TABLE IF EXISTS `elec_cards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `elec_cards` (
  `client_number` varchar(255) NOT NULL,
  `value` float NOT NULL,
  `type` varchar(255) NOT NULL,
  `_date` date NOT NULL,
  `_time` time NOT NULL,
  `EmployeeID` int NOT NULL,
  `MachineID` int NOT NULL,
  KEY `EmployeeID` (`EmployeeID`),
  KEY `MachineID` (`MachineID`),
  CONSTRAINT `elec_cards_ibfk_1` FOREIGN KEY (`EmployeeID`) REFERENCES `employee` (`EmployeeID`),
  CONSTRAINT `elec_cards_ibfk_2` FOREIGN KEY (`MachineID`) REFERENCES `machines` (`MachineID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elec_cards`
--

LOCK TABLES `elec_cards` WRITE;
/*!40000 ALTER TABLE `elec_cards` DISABLE KEYS */;
/*!40000 ALTER TABLE `elec_cards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `EmployeeID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `mail` varchar(255) DEFAULT NULL,
  `national_id` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`EmployeeID`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'على','alialaa','alialaa','213','3213','asdf','e10adc3949ba59abbe56e057f20f883e');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `etisalat_cards_values`
--

DROP TABLE IF EXISTS `etisalat_cards_values`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `etisalat_cards_values` (
  `cardID` int NOT NULL AUTO_INCREMENT,
  `card_value` float NOT NULL,
  PRIMARY KEY (`cardID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `etisalat_cards_values`
--

LOCK TABLES `etisalat_cards_values` WRITE;
/*!40000 ALTER TABLE `etisalat_cards_values` DISABLE KEYS */;
/*!40000 ALTER TABLE `etisalat_cards_values` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `machines`
--

DROP TABLE IF EXISTS `machines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `machines` (
  `MachineID` int NOT NULL AUTO_INCREMENT,
  `machine_name` varchar(255) NOT NULL,
  PRIMARY KEY (`MachineID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `machines`
--

LOCK TABLES `machines` WRITE;
/*!40000 ALTER TABLE `machines` DISABLE KEYS */;
INSERT INTO `machines` VALUES (1,'فوري'),(2,'مصاري'),(3,'سداد'),(4,'ضامن');
/*!40000 ALTER TABLE `machines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orange_cards_values`
--

DROP TABLE IF EXISTS `orange_cards_values`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orange_cards_values` (
  `cardID` int NOT NULL AUTO_INCREMENT,
  `card_value` float NOT NULL,
  PRIMARY KEY (`cardID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orange_cards_values`
--

LOCK TABLES `orange_cards_values` WRITE;
/*!40000 ALTER TABLE `orange_cards_values` DISABLE KEYS */;
/*!40000 ALTER TABLE `orange_cards_values` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `other`
--

DROP TABLE IF EXISTS `other`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `other` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `num` int NOT NULL,
  `value` float NOT NULL,
  `_date` date NOT NULL,
  `_time` time NOT NULL,
  `EmployeeID` int NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `EmployeeID` (`EmployeeID`),
  KEY `order_id` (`order_id`),
  CONSTRAINT `other_ibfk_1` FOREIGN KEY (`EmployeeID`) REFERENCES `employee` (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `other`
--

LOCK TABLES `other` WRITE;
/*!40000 ALTER TABLE `other` DISABLE KEYS */;
/*!40000 ALTER TABLE `other` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `other_stored`
--

DROP TABLE IF EXISTS `other_stored`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `other_stored` (
  `otherID` int NOT NULL AUTO_INCREMENT,
  `other_name` varchar(255) NOT NULL,
  `price` float NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`otherID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `other_stored`
--

LOCK TABLES `other_stored` WRITE;
/*!40000 ALTER TABLE `other_stored` DISABLE KEYS */;
/*!40000 ALTER TABLE `other_stored` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permissions`
--

DROP TABLE IF EXISTS `permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `permissions` (
  `permissionID` int NOT NULL AUTO_INCREMENT,
  `EmployeeID` int NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `charge_tab` tinyint(1) NOT NULL,
  `charge_add` tinyint(1) NOT NULL,
  `charge_del` tinyint(1) NOT NULL,
  `charge_info` tinyint(1) NOT NULL,
  `accessories_tab` tinyint(1) NOT NULL,
  `accessories_add` tinyint(1) NOT NULL,
  `accessories_del` tinyint(1) NOT NULL,
  `accessories_info` tinyint(1) NOT NULL,
  `tobacco_tab` tinyint(1) NOT NULL,
  `tobacco_add` tinyint(1) NOT NULL,
  `tobacco_del` tinyint(1) NOT NULL,
  `tobacco_info` tinyint(1) NOT NULL,
  `other_tab` tinyint(1) NOT NULL,
  `other_add` tinyint(1) NOT NULL,
  `other_del` tinyint(1) NOT NULL,
  `other_info` tinyint(1) NOT NULL,
  `wanted_tab` tinyint(1) NOT NULL,
  `wanted_add` tinyint(1) NOT NULL,
  `wanted_del` tinyint(1) NOT NULL,
  `search_op` tinyint(1) NOT NULL,
  `settings_tab` tinyint(1) NOT NULL,
  `setting_add_brand` tinyint(1) NOT NULL,
  `setting_add_new_brand` tinyint(1) NOT NULL,
  `setting_edit_brand` tinyint(1) NOT NULL,
  `add_employee` tinyint(1) NOT NULL,
  `edit_employee` tinyint(1) NOT NULL,
  `reports` tinyint(1) NOT NULL,
  `dailymoment` tinyint(1) NOT NULL,
  `add_permissions` tinyint(1) NOT NULL,
  PRIMARY KEY (`permissionID`),
  KEY `EmployeeID` (`EmployeeID`),
  CONSTRAINT `permissions_ibfk_1` FOREIGN KEY (`EmployeeID`) REFERENCES `employee` (`EmployeeID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permissions`
--

LOCK TABLES `permissions` WRITE;
/*!40000 ALTER TABLE `permissions` DISABLE KEYS */;
INSERT INTO `permissions` VALUES (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phone_cards`
--

DROP TABLE IF EXISTS `phone_cards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phone_cards` (
  `company_name` varchar(255) NOT NULL,
  `value` float NOT NULL,
  `quantity` int NOT NULL,
  `_date` date NOT NULL,
  `_time` time NOT NULL,
  `EmployeeID` int NOT NULL,
  KEY `EmployeeID` (`EmployeeID`),
  CONSTRAINT `phone_cards_ibfk_1` FOREIGN KEY (`EmployeeID`) REFERENCES `employee` (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phone_cards`
--

LOCK TABLES `phone_cards` WRITE;
/*!40000 ALTER TABLE `phone_cards` DISABLE KEYS */;
/*!40000 ALTER TABLE `phone_cards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `services`
--

DROP TABLE IF EXISTS `services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `services` (
  `serviceID` int NOT NULL AUTO_INCREMENT,
  `service_name` varchar(255) NOT NULL,
  PRIMARY KEY (`serviceID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `services`
--

LOCK TABLES `services` WRITE;
/*!40000 ALTER TABLE `services` DISABLE KEYS */;
INSERT INTO `services` VALUES (1,'شحن فودافون'),(2,'شحن اتصالات'),(3,'شحن اورنج'),(4,'شحن WE');
/*!40000 ALTER TABLE `services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tobacco`
--

DROP TABLE IF EXISTS `tobacco`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tobacco` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `value` float NOT NULL,
  `num` int NOT NULL,
  `_date` date NOT NULL,
  `_time` time NOT NULL,
  `EmployeeID` int NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `EmployeeID` (`EmployeeID`),
  KEY `order_id` (`order_id`),
  CONSTRAINT `tobacco_ibfk_1` FOREIGN KEY (`EmployeeID`) REFERENCES `employee` (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tobacco`
--

LOCK TABLES `tobacco` WRITE;
/*!40000 ALTER TABLE `tobacco` DISABLE KEYS */;
/*!40000 ALTER TABLE `tobacco` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tobacco_stored`
--

DROP TABLE IF EXISTS `tobacco_stored`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tobacco_stored` (
  `tobaccoID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `quantity` int NOT NULL,
  `price` float NOT NULL,
  PRIMARY KEY (`tobaccoID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tobacco_stored`
--

LOCK TABLES `tobacco_stored` WRITE;
/*!40000 ALTER TABLE `tobacco_stored` DISABLE KEYS */;
/*!40000 ALTER TABLE `tobacco_stored` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vodafone_cards_values`
--

DROP TABLE IF EXISTS `vodafone_cards_values`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vodafone_cards_values` (
  `cardID` int NOT NULL AUTO_INCREMENT,
  `card_value` float NOT NULL,
  PRIMARY KEY (`cardID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vodafone_cards_values`
--

LOCK TABLES `vodafone_cards_values` WRITE;
/*!40000 ALTER TABLE `vodafone_cards_values` DISABLE KEYS */;
/*!40000 ALTER TABLE `vodafone_cards_values` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wanted`
--

DROP TABLE IF EXISTS `wanted`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wanted` (
  `client_name` varchar(255) NOT NULL,
  `value` float NOT NULL,
  `order_id` int NOT NULL AUTO_INCREMENT,
  `_date` date NOT NULL,
  `_time` time NOT NULL,
  `EmployeeID` int NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `order_id` (`order_id`),
  KEY `EmployeeID` (`EmployeeID`),
  CONSTRAINT `wanted_ibfk_1` FOREIGN KEY (`EmployeeID`) REFERENCES `employee` (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wanted`
--

LOCK TABLES `wanted` WRITE;
/*!40000 ALTER TABLE `wanted` DISABLE KEYS */;
/*!40000 ALTER TABLE `wanted` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `we_cards_values`
--

DROP TABLE IF EXISTS `we_cards_values`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `we_cards_values` (
  `cardID` int NOT NULL AUTO_INCREMENT,
  `card_value` float NOT NULL,
  PRIMARY KEY (`cardID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `we_cards_values`
--

LOCK TABLES `we_cards_values` WRITE;
/*!40000 ALTER TABLE `we_cards_values` DISABLE KEYS */;
/*!40000 ALTER TABLE `we_cards_values` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-08  2:30:59
