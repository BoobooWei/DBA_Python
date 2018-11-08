

DROP TABLE IF EXISTS `event_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `event_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(64) DEFAULT NULL,
  `category_id` varchar(32) DEFAULT NULL,
  `tec_id` varchar(32) DEFAULT NULL,
  `create_time` bigint(20) DEFAULT NULL,
  `update_time` bigint(20) DEFAULT NULL,
  `is_deleted` smallint(6) DEFAULT NULL,
  `delete_time` bigint(20) DEFAULT NULL,
  `uuid` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `events` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event` varchar(255) DEFAULT NULL,
  `state` varchar(32) DEFAULT NULL,
  `event_type_id` varchar(32) DEFAULT NULL,
  `product_type_id` varchar(32) DEFAULT NULL,
  `kitchen_url` varchar(255) DEFAULT NULL,
  `uuid` varchar(32) DEFAULT NULL,
  `create_time` bigint(20) DEFAULT NULL,
  `update_time` bigint(20) DEFAULT NULL,
  `is_deleted` smallint(6) DEFAULT NULL,
  `delete_time` bigint(20) DEFAULT NULL,
  `project_id` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `project_id` (`project_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;



DROP TABLE IF EXISTS `product_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(255) DEFAULT NULL,
  `category_id` varchar(32) DEFAULT NULL,
  `platform_id` varchar(32) DEFAULT NULL,
  `uuid` varchar(32) DEFAULT NULL,
  `create_time` bigint(20) DEFAULT NULL,
  `update_time` bigint(20) DEFAULT NULL,
  `is_deleted` smallint(6) DEFAULT NULL,
  `delete_time` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `customer_id` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `manager_id` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `architect_id` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `operator_id` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `consumer_id` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `sales_id` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `status` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `begin_time` int(11) DEFAULT NULL,
  `end_time` int(11) DEFAULT NULL,
  `creator_id` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `modifier_id` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `uuid` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `remarks` text COLLATE utf8_bin,
  `create_time` bigint(20) DEFAULT NULL,
  `update_time` bigint(20) DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  `sensitivity_level` int(11) DEFAULT NULL,
  `delete_time` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_projects_uuid` (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=907 DEFAULT CHARSET=utf8 COLLATE=utf8_bin ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `user_processlist`
--

DROP TABLE IF EXISTS `user_processlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_processlist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(32) DEFAULT NULL,
  `event_id` varchar(32) DEFAULT NULL,
  `info` text,
  `create_time` bigint(20) DEFAULT NULL,
  `update_time` bigint(20) DEFAULT NULL,
  `is_deleted` smallint(6) DEFAULT NULL,
  `delete_time` bigint(20) DEFAULT NULL,
  `uuid` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `username` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `name` varchar(64) COLLATE utf8_bin NOT NULL DEFAULT '',
  `location` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `mobile` varchar(11) COLLATE utf8_bin DEFAULT NULL,
  `is_admin` tinyint(1) DEFAULT NULL,
  `is_locked` tinyint(1) DEFAULT NULL,
  `creator_id` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `ding_talk` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `is_deleted` tinyint(1) DEFAULT NULL,
  `last_login_ip` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `login_count` int(11) DEFAULT NULL,
  `modifier_id` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `nickname` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `position` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `remarks` text COLLATE utf8_bin,
  `source` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `uuid` varchar(32) COLLATE utf8_bin DEFAULT NULL,
  `last_seen` bigint(20) DEFAULT NULL,
  `create_time` bigint(20) DEFAULT NULL,
  `update_time` bigint(20) DEFAULT NULL,
  `unique_id` varchar(64) COLLATE utf8_bin DEFAULT NULL,
  `delete_time` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_users_uuid` (`uuid`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `unique_id` (`unique_id`)
) ENGINE=InnoDB AUTO_INCREMENT=981 DEFAULT CHARSET=utf8 COLLATE=utf8_bin ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;


CREATE TABLE `shadow` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(80) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL,
  `create_time` bigint(20) DEFAULT NULL,
  `update_time` bigint(20) DEFAULT NULL,
  `is_deleted` int(11) DEFAULT NULL,
  `delete_time` bigint(20) DEFAULT NULL,
  `uuid` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

