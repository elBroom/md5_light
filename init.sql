CREATE TABLE IF NOT EXISTS `task` (
  `id` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `started_at` datetime DEFAULT NULL,
  `finished_at` datetime DEFAULT NULL,
  `url` varchar(32768) NOT NULL,
  `email` varchar(120) DEFAULT NULL,
  `status` enum('CREATED','RUNNING','DONE','FAIL') NOT NULL,
  `md5` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
