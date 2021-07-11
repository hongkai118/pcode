/*
 Navicat MySQL Data Transfer

 Source Server         : k1
 Source Server Type    : MySQL
 Source Server Version : 80023
 Source Host           : localhost:3306
 Source Schema         : db10

 Target Server Type    : MySQL
 Target Server Version : 80023
 File Encoding         : 65001

 Date: 11/06/2021 23:19:49
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bumen
-- ----------------------------
DROP TABLE IF EXISTS `bumen`;
CREATE TABLE `bumen`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `bm_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 22 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of bumen
-- ----------------------------
INSERT INTO `bumen` VALUES (1, 'head');
INSERT INTO `bumen` VALUES (2, 'pharmcology');
INSERT INTO `bumen` VALUES (3, 'discovery');
INSERT INTO `bumen` VALUES (4, 'pm');
INSERT INTO `bumen` VALUES (5, 'ds');
INSERT INTO `bumen` VALUES (6, 'ad');
INSERT INTO `bumen` VALUES (7, 'dp');
INSERT INTO `bumen` VALUES (8, 'msat');
INSERT INTO `bumen` VALUES (9, 'ra');
INSERT INTO `bumen` VALUES (10, 'quality');
INSERT INTO `bumen` VALUES (11, 'supply_chain');
INSERT INTO `bumen` VALUES (12, 'manufacturing');
INSERT INTO `bumen` VALUES (13, 'engineer');
INSERT INTO `bumen` VALUES (14, 'ehs');
INSERT INTO `bumen` VALUES (15, 'trade');
INSERT INTO `bumen` VALUES (16, 'bd');
INSERT INTO `bumen` VALUES (17, 'hr');
INSERT INTO `bumen` VALUES (18, 'finance');
INSERT INTO `bumen` VALUES (19, 'it');
INSERT INTO `bumen` VALUES (20, 'cmo');
INSERT INTO `bumen` VALUES (21, 'medical');

-- ----------------------------
-- Table structure for class
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `class` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of class
-- ----------------------------
INSERT INTO `class` VALUES (1, '全栈4期');
INSERT INTO `class` VALUES (2, '全栈5期');
INSERT INTO `class` VALUES (3, '全栈6期');
INSERT INTO `class` VALUES (4, '六年级一班');
INSERT INTO `class` VALUES (5, '猎头2期DFDF');
INSERT INTO `class` VALUES (7, '猎头3期dfdfdfdf');
INSERT INTO `class` VALUES (8, '三年');
INSERT INTO `class` VALUES (17, '再来几个');
INSERT INTO `class` VALUES (19, '数据库1期2');
INSERT INTO `class` VALUES (20, '最后一个班');

-- ----------------------------
-- Table structure for cnd
-- ----------------------------
DROP TABLE IF EXISTS `cnd`;
CREATE TABLE `cnd`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `jibie` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `min_salary` int NULL DEFAULT NULL,
  `max_salary` int NULL DEFAULT NULL,
  `hangye_id` int NULL DEFAULT NULL,
  `zhineng_id` int NULL DEFAULT NULL,
  `bumen_id` int NULL DEFAULT NULL,
  `jixing_id` int NULL DEFAULT NULL,
  `company` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `cnd_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `cell_phone` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `email` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `wechart` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `degree` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `link_url` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `location` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `birth_day` date NULL DEFAULT NULL,
  `insert_time` datetime NULL DEFAULT NULL,
  `report` int NULL DEFAULT NULL,
  `motivation` int NULL DEFAULT NULL,
  `todo` int NULL DEFAULT NULL,
  `beizhu` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_cnd_hy`(`hangye_id`) USING BTREE,
  INDEX `fk_cnd_zn`(`zhineng_id`) USING BTREE,
  INDEX `fk_cnd_bm`(`bumen_id`) USING BTREE,
  INDEX `fk_cnd_jx`(`jixing_id`) USING BTREE,
  CONSTRAINT `fk_cnd_bm` FOREIGN KEY (`bumen_id`) REFERENCES `bumen` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_cnd_hy` FOREIGN KEY (`hangye_id`) REFERENCES `hangye` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_cnd_jx` FOREIGN KEY (`jixing_id`) REFERENCES `jixing` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_cnd_zn` FOREIGN KEY (`zhineng_id`) REFERENCES `zhineng` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cnd
-- ----------------------------

-- ----------------------------
-- Table structure for hangye
-- ----------------------------
DROP TABLE IF EXISTS `hangye`;
CREATE TABLE `hangye`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `hy_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of hangye
-- ----------------------------
INSERT INTO `hangye` VALUES (1, 'small');
INSERT INTO `hangye` VALUES (2, 'large');
INSERT INTO `hangye` VALUES (3, 'xna');
INSERT INTO `hangye` VALUES (4, 'peptide');
INSERT INTO `hangye` VALUES (5, 'cart');

-- ----------------------------
-- Table structure for jixing
-- ----------------------------
DROP TABLE IF EXISTS `jixing`;
CREATE TABLE `jixing`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `jx_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 23 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of jixing
-- ----------------------------
INSERT INTO `jixing` VALUES (1, 'head');
INSERT INTO `jixing` VALUES (2, 'invivo');
INSERT INTO `jixing` VALUES (3, 'dmpk');
INSERT INTO `jixing` VALUES (4, 'biomarker');
INSERT INTO `jixing` VALUES (5, 'clinical_pharmacology');
INSERT INTO `jixing` VALUES (6, 'biology');
INSERT INTO `jixing` VALUES (7, 'bioinformatics');
INSERT INTO `jixing` VALUES (8, 'med-chemistry');
INSERT INTO `jixing` VALUES (9, 'protein-engineer');
INSERT INTO `jixing` VALUES (10, 'pm');
INSERT INTO `jixing` VALUES (11, 'ds');
INSERT INTO `jixing` VALUES (12, 'dp');
INSERT INTO `jixing` VALUES (13, 'injectable');
INSERT INTO `jixing` VALUES (14, 'solid');
INSERT INTO `jixing` VALUES (15, 'sustained-release');
INSERT INTO `jixing` VALUES (16, 'nano');
INSERT INTO `jixing` VALUES (17, 'cl');
INSERT INTO `jixing` VALUES (18, 'up');
INSERT INTO `jixing` VALUES (19, 'down');
INSERT INTO `jixing` VALUES (20, 'pre-formulation');
INSERT INTO `jixing` VALUES (21, '505b2');
INSERT INTO `jixing` VALUES (22, 'qa');
INSERT INTO `jixing` VALUES (23, 'qc');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `stu_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `class_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_stu_class`(`class_id`) USING BTREE,
  CONSTRAINT `fk_stu_class` FOREIGN KEY (`class_id`) REFERENCES `class` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES (1, '小王', 2);
INSERT INTO `student` VALUES (2, '豆三', 3);
INSERT INTO `student` VALUES (3, 'K2', 5);

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `t_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES (1, '苍老师');
INSERT INTO `teacher` VALUES (2, '武老师');
INSERT INTO `teacher` VALUES (3, '饭老师');
INSERT INTO `teacher` VALUES (4, '游老师啦啦啦');
INSERT INTO `teacher` VALUES (5, '王老师');
INSERT INTO `teacher` VALUES (10, '李莉莉');

-- ----------------------------
-- Table structure for teacher2class
-- ----------------------------
DROP TABLE IF EXISTS `teacher2class`;
CREATE TABLE `teacher2class`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `t_id` int NOT NULL,
  `class_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_guanxi_teach`(`t_id`) USING BTREE,
  INDEX `fk_guanxi_class`(`class_id`) USING BTREE,
  CONSTRAINT `fk_guanxi_class` FOREIGN KEY (`class_id`) REFERENCES `class` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_guanxi_teach` FOREIGN KEY (`t_id`) REFERENCES `teacher` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacher2class
-- ----------------------------
INSERT INTO `teacher2class` VALUES (1, 1, 2);
INSERT INTO `teacher2class` VALUES (2, 2, 2);
INSERT INTO `teacher2class` VALUES (3, 3, 3);
INSERT INTO `teacher2class` VALUES (4, 1, 3);
INSERT INTO `teacher2class` VALUES (5, 2, 1);

-- ----------------------------
-- Table structure for test01
-- ----------------------------
DROP TABLE IF EXISTS `test01`;
CREATE TABLE `test01`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `c_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `c_title` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `public` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of test01
-- ----------------------------
INSERT INTO `test01` VALUES (1, 'oooo', 'kkkk', NULL);
INSERT INTO `test01` VALUES (2, 'oooo', 'kkkk', '2021-06-04 00:00:00');
INSERT INTO `test01` VALUES (3, 'oooo', 'kkkk', '2021-06-04 00:00:00');
INSERT INTO `test01` VALUES (4, 'oooo', 'kkkk', '2021-06-04 00:00:00');
INSERT INTO `test01` VALUES (5, 'oooo', 'date', '2021-06-04 00:00:00');
INSERT INTO `test01` VALUES (6, 'oooo', 'time', '2021-06-04 00:00:00');
INSERT INTO `test01` VALUES (7, 'oooo', 'now', '2021-06-04 00:00:00');
INSERT INTO `test01` VALUES (8, 'oooo', 'date--', '2021-06-04 00:00:00');
INSERT INTO `test01` VALUES (9, 'oooo', 'date--', '2021-07-04 00:00:00');
INSERT INTO `test01` VALUES (10, 'oooo', 'date--', '2021-07-04 00:00:00');
INSERT INTO `test01` VALUES (11, 'oooo', 'date--', '2021-09-04 00:00:00');
INSERT INTO `test01` VALUES (12, 'oooo', 'date--', '2021-09-04 00:00:00');
INSERT INTO `test01` VALUES (13, '123oo', 'date--', '2021-09-04 00:00:00');

-- ----------------------------
-- Table structure for ygoffer
-- ----------------------------
DROP TABLE IF EXISTS `ygoffer`;
CREATE TABLE `ygoffer`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `yg_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `yg_yeji` int NOT NULL,
  `offer_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_ygoffer_zoffer`(`offer_id`) USING BTREE,
  CONSTRAINT `fk_ygoffer_zoffer` FOREIGN KEY (`offer_id`) REFERENCES `zoffer` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 97 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of ygoffer
-- ----------------------------
INSERT INTO `ygoffer` VALUES (1, 'kyle', 35000, 1);
INSERT INTO `ygoffer` VALUES (2, 'raya', 30000, 1);
INSERT INTO `ygoffer` VALUES (3, 'shelley', 80000, 2);
INSERT INTO `ygoffer` VALUES (4, 'kevin', 40000, 3);
INSERT INTO `ygoffer` VALUES (5, 'amy', 40000, 3);
INSERT INTO `ygoffer` VALUES (6, 'kyle', 50000, 3);
INSERT INTO `ygoffer` VALUES (7, 'kyle', 250000, 4);
INSERT INTO `ygoffer` VALUES (8, 'kerwin', 70000, 4);
INSERT INTO `ygoffer` VALUES (9, 'shelley', 18000, 5);
INSERT INTO `ygoffer` VALUES (10, 'kerwin', 72000, 5);
INSERT INTO `ygoffer` VALUES (11, 'shelley', 14000, 6);
INSERT INTO `ygoffer` VALUES (12, 'shark', 56000, 6);
INSERT INTO `ygoffer` VALUES (13, 'cristina', 50000, 7);
INSERT INTO `ygoffer` VALUES (14, 'kyle', 7499, 7);
INSERT INTO `ygoffer` VALUES (15, 'skye', 60000, 8);
INSERT INTO `ygoffer` VALUES (16, 'kyle', 9000, 8);
INSERT INTO `ygoffer` VALUES (17, 'kyle', 276000, 9);
INSERT INTO `ygoffer` VALUES (18, 'shelley', 92400, 10);
INSERT INTO `ygoffer` VALUES (19, 'vera', 42336, 11);
INSERT INTO `ygoffer` VALUES (20, 'kyle', 10584, 11);
INSERT INTO `ygoffer` VALUES (21, 'kyle', 310000, 12);
INSERT INTO `ygoffer` VALUES (22, 'raya', 136320, 13);
INSERT INTO `ygoffer` VALUES (23, 'skye', 34080, 13);
INSERT INTO `ygoffer` VALUES (24, 'kyle', 56160, 14);
INSERT INTO `ygoffer` VALUES (25, 'shelley', 14040, 14);
INSERT INTO `ygoffer` VALUES (26, 'vera', 44160, 15);
INSERT INTO `ygoffer` VALUES (27, 'kyle', 11040, 15);
INSERT INTO `ygoffer` VALUES (28, 'frank', 63000, 16);
INSERT INTO `ygoffer` VALUES (29, 'raya', 27000, 16);
INSERT INTO `ygoffer` VALUES (30, 'kyle', 15000, 17);
INSERT INTO `ygoffer` VALUES (31, 'anna', 35000, 17);
INSERT INTO `ygoffer` VALUES (32, 'amy', 158333, 18);
INSERT INTO `ygoffer` VALUES (33, 'anna', 39583, 18);
INSERT INTO `ygoffer` VALUES (34, 'cristina', 39424, 19);
INSERT INTO `ygoffer` VALUES (35, 'shark', 9856, 19);
INSERT INTO `ygoffer` VALUES (36, 'kyle', 120000, 20);
INSERT INTO `ygoffer` VALUES (37, 'shelley', 66000, 21);
INSERT INTO `ygoffer` VALUES (38, 'raya', 32000, 22);
INSERT INTO `ygoffer` VALUES (39, 'shelley', 8000, 22);
INSERT INTO `ygoffer` VALUES (40, 'skye', 88000, 23);
INSERT INTO `ygoffer` VALUES (41, 'skye', 69600, 24);
INSERT INTO `ygoffer` VALUES (42, 'skye', 72400, 25);
INSERT INTO `ygoffer` VALUES (43, 'kyle', 111680, 26);
INSERT INTO `ygoffer` VALUES (44, 'della', 27920, 26);
INSERT INTO `ygoffer` VALUES (45, 'cristina', 93990, 27);
INSERT INTO `ygoffer` VALUES (46, 'frank', 23498, 27);
INSERT INTO `ygoffer` VALUES (47, 'vera', 44160, 28);
INSERT INTO `ygoffer` VALUES (48, 'kyle', 11040, 28);
INSERT INTO `ygoffer` VALUES (49, 'vera', 44480, 29);
INSERT INTO `ygoffer` VALUES (50, 'kyle', 11120, 29);
INSERT INTO `ygoffer` VALUES (51, 'raya', 28600, 30);
INSERT INTO `ygoffer` VALUES (52, 'anna', 114400, 30);
INSERT INTO `ygoffer` VALUES (53, 'raya', 39000, 31);
INSERT INTO `ygoffer` VALUES (54, 'permi', 91000, 31);
INSERT INTO `ygoffer` VALUES (55, 'will', 45540, 32);
INSERT INTO `ygoffer` VALUES (56, 'amy', 106260, 32);
INSERT INTO `ygoffer` VALUES (57, 'skye', 328786, 33);
INSERT INTO `ygoffer` VALUES (58, 'kyle', 109595, 33);
INSERT INTO `ygoffer` VALUES (59, 'shelley', 109595, 33);
INSERT INTO `ygoffer` VALUES (60, 'kyle', 114816, 34);
INSERT INTO `ygoffer` VALUES (61, 'kerwin', 28704, 34);
INSERT INTO `ygoffer` VALUES (62, 'vera', 33000, 35);
INSERT INTO `ygoffer` VALUES (63, 'kyle', 22000, 35);
INSERT INTO `ygoffer` VALUES (64, 'amy', 62400, 36);
INSERT INTO `ygoffer` VALUES (65, 'skye', 15600, 36);
INSERT INTO `ygoffer` VALUES (66, 'cristina', 100960, 37);
INSERT INTO `ygoffer` VALUES (67, 'kyle', 25240, 37);
INSERT INTO `ygoffer` VALUES (68, 'shelley', 78000, 38);
INSERT INTO `ygoffer` VALUES (69, 'kyle', 66000, 39);
INSERT INTO `ygoffer` VALUES (70, 'aimee', 113920, 40);
INSERT INTO `ygoffer` VALUES (71, 'kyle', 28480, 40);
INSERT INTO `ygoffer` VALUES (72, 'vera', 83701, 41);
INSERT INTO `ygoffer` VALUES (73, 'frank', 20925, 41);
INSERT INTO `ygoffer` VALUES (74, 'vera', 53312, 42);
INSERT INTO `ygoffer` VALUES (75, 'kyle', 13328, 42);
INSERT INTO `ygoffer` VALUES (76, 'vera', 56480, 43);
INSERT INTO `ygoffer` VALUES (77, 'amy', 14120, 43);
INSERT INTO `ygoffer` VALUES (78, 'raya', 220800, 44);
INSERT INTO `ygoffer` VALUES (79, 'shelley', 55200, 44);
INSERT INTO `ygoffer` VALUES (80, 'shelley', 94080, 45);
INSERT INTO `ygoffer` VALUES (81, 'kyle', 23520, 45);
INSERT INTO `ygoffer` VALUES (82, 'raya', 55200, 46);
INSERT INTO `ygoffer` VALUES (83, 'aimee', 128800, 46);
INSERT INTO `ygoffer` VALUES (84, 'jessie', 158720, 49);
INSERT INTO `ygoffer` VALUES (85, 'kyle', 39680, 49);
INSERT INTO `ygoffer` VALUES (86, 'raya', 96000, 50);
INSERT INTO `ygoffer` VALUES (87, 'kyle', 24000, 50);
INSERT INTO `ygoffer` VALUES (88, 'raya', 315100, 51);
INSERT INTO `ygoffer` VALUES (89, 'kyle', 240000, 52);
INSERT INTO `ygoffer` VALUES (90, 'kyle', 66240, 53);
INSERT INTO `ygoffer` VALUES (91, 'kyle', 12800, 54);
INSERT INTO `ygoffer` VALUES (92, 'leo', 51200, 54);
INSERT INTO `ygoffer` VALUES (93, 'raya', 6048, 55);
INSERT INTO `ygoffer` VALUES (94, 'duke', 24192, 55);
INSERT INTO `ygoffer` VALUES (95, 'vera', 84000, 56);
INSERT INTO `ygoffer` VALUES (96, 'shark', 36000, 56);

-- ----------------------------
-- Table structure for zhineng
-- ----------------------------
DROP TABLE IF EXISTS `zhineng`;
CREATE TABLE `zhineng`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `zn_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of zhineng
-- ----------------------------
INSERT INTO `zhineng` VALUES (1, 'preclinical');
INSERT INTO `zhineng` VALUES (2, 'cmc');
INSERT INTO `zhineng` VALUES (3, 'plant');
INSERT INTO `zhineng` VALUES (4, 'medical');
INSERT INTO `zhineng` VALUES (5, 'bd&hr');

-- ----------------------------
-- Table structure for zoffer
-- ----------------------------
DROP TABLE IF EXISTS `zoffer`;
CREATE TABLE `zoffer`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `hangye_id` int NULL DEFAULT NULL,
  `zhineng_id` int NULL DEFAULT NULL,
  `bumen_id` int NULL DEFAULT NULL,
  `company` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `title` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `cnd_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `client_offer` int NULL DEFAULT NULL,
  `team_offer` int NULL DEFAULT NULL,
  `offer_time` date NULL DEFAULT NULL,
  `client_owner` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `contact_window` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `offer_owner` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `insert_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_zoffer_hy`(`hangye_id`) USING BTREE,
  INDEX `fk_zoffer_zn`(`zhineng_id`) USING BTREE,
  INDEX `fk_zoffer_bm`(`bumen_id`) USING BTREE,
  CONSTRAINT `fk_zoffer_bm` FOREIGN KEY (`bumen_id`) REFERENCES `bumen` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_zoffer_hy` FOREIGN KEY (`hangye_id`) REFERENCES `hangye` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_zoffer_zn` FOREIGN KEY (`zhineng_id`) REFERENCES `zhineng` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 61 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of zoffer
-- ----------------------------
INSERT INTO `zoffer` VALUES (1, 2, 3, 10, '明济', 'QA经理', '二波', 65000, 65000, '2021-05-01', 'kyle', 'kyle', 'raya', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (2, 1, 2, 7, '九洲', '制剂总监', '钢弹', 80000, 80000, '2021-05-01', 'kyle', 'kyle', 'shelley', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (3, 1, 3, 12, '九洲', '生产经理', '铁柱', 130000, 130000, '2021-06-01', 'kyle', 'kyle', 'kyle', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (4, 1, 2, 1, '信达', 'PD ED', '张三', 320000, 250000, '2021-06-01', 'kerwin', 'Kyle', 'kyle', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (5, 2, 4, 21, '瑞博', '项目经理', '刘儿姐', 90000, 18000, '2021-06-01', 'shelley', 'shelley', 'frank', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (6, 2, 4, 21, '瑞博', '医学经理', '炊鸭', 70000, 14000, '2021-06-01', 'shelley', 'shelley', 'frank', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (7, 3, 2, 5, '嘉晨西海', '下游组长', '周磊磊', 57499, 57499, '2020-02-01', 'kyle', 'kyle', 'Cristina', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (8, 3, 1, 3, '嘉晨西海', '生物学科学家', '单爱东', 69000, 69000, '2020-03-01', 'kyle', 'kyle', 'Skye', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (9, 1, 2, 6, '齐鲁海南', '小分子分析总监', '周金鹏', 276000, 276000, '2020-05-01', 'kyle', 'kyle', 'Kyle', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (10, 1, 1, 2, '益诺思', '眼科副总级', '孟永', 92400, 92400, '2020-05-01', 'shelley', 'shelley', 'Shelley', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (11, 1, 1, 2, '中美冠科', 'Biomaker Scientist', '林洁', 52920, 52920, '2020-05-01', 'kyle', 'kyle', 'Vera', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (12, 1, 2, 5, '华海', 'API技术副总', '朱伟', 310000, 310000, '2020-06-01', 'kyle', 'kyle', 'Kyle', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (13, 1, 5, 17, '信诺维', 'HRVP', '李清', 170400, 170400, '2030-02-06', 'kyle', 'kyle', 'Raya', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (14, 3, 3, 10, '瑞博', '质量经理', '孟小环', 70200, 70200, '2020-07-01', 'shelley', 'shelley', 'Kyle', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (15, 2, 2, 7, '嘉晨西海', '脂质体制剂专家', '张盟', 55200, 55200, '2020-07-01', 'kyle', 'kyle', 'Vera', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (16, 1, 4, 21, '上药', '拆分', NULL, 90000, 27000, '2020-07-01', 'raya', 'raya', 'frank', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (17, 1, 4, 21, '信诺维', '拆分', NULL, 50000, 15000, '2020-07-01', 'kyle', 'kyle', 'anna', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (18, 2, 3, 10, '白帆', '大分子质量高级总监', '吴晓峰', 197916, 158333, '2020-07-01', 'kerwin', 'kyle', 'Amy', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (19, 2, 2, 5, '三叶草', '下游高级主管', '郑荣海', 49280, 39424, '2020-07-01', 'shark', 'shark', 'Cristina', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (20, 1, 3, 1, '常山生化', '子公司总经理', '徐赟', 120000, 120000, '2020-08-01', 'kyle', 'kyle', 'Kyle', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (21, 1, 2, 7, '一品红', '中药制剂经理', '康晓东', 66000, 66000, '2020-08-01', 'shelley', 'shelley', 'Shelley', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (22, 1, 4, 21, '瑞博', 'CMO顾问', 'Que Liu', 40000, 40000, '2020-08-01', 'shelley', 'shelley', 'Raya', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (23, 1, 1, 2, '地奥', '药理经理', '崔魏', 88000, 88000, '2020-08-01', 'kyle', 'kyle', 'Skye', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (24, 1, 2, 5, '信诺维', 'API工艺项目经理', '王严飞', 69600, 69600, '2020-08-01', 'kyle', 'kyle', 'Skye', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (25, 1, 1, 2, '信诺维', 'Biomaker Scientist', '张明明', 72400, 72400, '2020-08-01', 'kyle', 'kyle', 'Skye', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (26, 1, 2, 1, '丽彩', '研发副院长', '陈尧', 139600, 111680, '2020-08-01', 'della', 'kyle', 'Kyle', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (27, 1, 1, 2, '英派', '临床药理', '史卉妍', 117488, 93990, '2020-08-01', 'shark', 'shark', 'Cristina', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (28, 3, 1, 3, '嘉晨西海', '生物学高级科学家', '王莎莎', 55200, 55200, '2020-09-01', 'kyle', 'kyle', 'Vera', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (29, 1, 1, 21, '信诺维', '转化医学经理', '杨晏冬', 55600, 55600, '2020-09-01', 'kyle', 'kyle', 'Vera', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (30, 2, 5, 17, '杏联', '拆分', NULL, 143000, 28600, '2020-09-01', 'raya', 'raya', 'anna', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (31, 1, 4, 21, '上药', '拆分', NULL, 130000, 39000, '2020-09-01', 'raya', 'raya', 'permi', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (32, 2, 3, 10, '仁会', '大分子质量高级总监', '徐海潮', 151800, 106260, '2020-09-01', 'will', 'will', 'Amy', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (33, 1, 2, 1, '远大', '新药院长', '陈少清', 547976, 547976, '2020-10-01', 'shelley', 'shelley', 'Skye', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (34, 1, 3, 10, '亿腾', '小分子质量总监', '刘晓红', 143520, 114816, '2020-10-01', 'kerwin', 'kyle', 'Kyle', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (35, 1, 1, 2, '地奥', '药理经理', '衡晓洁', 55000, 55000, '2020-11-01', 'kyle', 'kyle', 'vera', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (36, 1, 3, 13, '信诺维', '工程副总级', '施云峰', 78000, 78000, '2020-11-01', 'kyle', 'kyle', 'Amy', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (37, 1, 3, 13, '信诺维', '工程总级', '石华平', 126200, 126200, '2020-11-01', 'kyle', 'kyle', 'Cristina', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (38, 1, 1, 2, '瑞博', '临床药理', '卢千峰', 78000, 78000, '2020-11-01', 'shelley', 'shelley', 'Emily', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (39, 2, 3, 10, '依科赛', '大分子质量总监', '杨重斌', 66000, 66000, '2020-11-01', 'kyle', 'kyle', 'Emily', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (40, 1, 4, 21, '信诺维', '拆分', NULL, 142400, 28480, '2020-11-01', 'kyle', 'kyle', 'aimee', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (41, 1, 1, 2, '英派', '药理', '杨新华', 104625, 83700, '2020-11-01', 'shark', 'shark', 'Vera', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (42, 3, 1, 3, '绿叶', '生物学科学家', '刘中天', 66640, 66640, '2020-12-01', 'kyle', 'kyle', 'Vera', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (43, 1, 1, 2, '甫康', '药理毒理总监', '刘小芳', 70600, 70600, '2020-12-01', 'amy', 'amy', 'vera', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (44, 1, 1, 2, '美迪西', '药理VP', '曹保红', 276000, 276000, '2020-12-01', 'shelley', 'shelley', 'Raya', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (45, 3, 1, 2, '嘉晨西海', '药理总监', '陈艳妮', 117600, 117600, '2020-12-01', 'kyle', 'kyle', 'Shelley', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (46, 1, 4, 21, '上药', '拆分', NULL, 184000, 55200, '2020-12-01', 'raya', 'raya', 'aimee', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (49, 1, 4, 21, '信诺维', '拆分', NULL, 198400, 39680, '2021-01-01', 'kyle', 'kyle', 'jessie', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (50, 1, 5, 15, '华海', 'API销售', '许应杰', 120000, 120000, '2021-01-01', 'kyle', 'kyle', 'Raya', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (51, 2, 5, 17, '福贝', '新药运营副总', NULL, 315100, 315100, '2021-01-01', 'raya', 'raya', 'Raya', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (52, 1, 3, 1, '华海', 'API运营副总', '李华军', 240000, 240000, '2021-01-01', 'kyle', 'kyle', 'Kyle', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (53, 1, 2, 7, '拓臻', '新药制剂经理', '许铄', 66240, 66240, '2021-01-01', 'kyle', 'kyle', 'Steven', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (54, 1, 4, 21, '恩华', '分拆', NULL, 64000, 12800, '2021-01-01', 'kyle', 'kyle', 'leo', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (55, 1, 4, 21, '扬子江', '拆分', NULL, 30240, 6048, '2021-01-01', 'raya', 'raya', 'duke', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (56, 1, 1, 3, '盟科', '药化总监', '杨鸿裕', 120000, 84000, '2021-01-01', 'shark', 'shark', 'Vera', '2021-06-04 00:00:00');
INSERT INTO `zoffer` VALUES (57, 1, 1, 1, 'AAA', '药理总监', '王三', 90000, 90000, '2020-05-20', 'amy', 'amy', 'amy', '2021-06-05 12:16:20');
INSERT INTO `zoffer` VALUES (58, 1, 3, 1, 'BBB', '厂长', '球儿', 190000, 0, '2021-05-21', 'Y2', 'Y2', 'K222222222', '2021-06-05 17:45:29');
INSERT INTO `zoffer` VALUES (59, 1, 3, 1, 'BBBccccccccccccc', '厂长', '球儿dddd', 90000, 90000, '2022-05-21', 'Y2', 'Y2233333', 'K333333', '2021-06-05 17:45:57');
INSERT INTO `zoffer` VALUES (60, 1, 1, 1, 'cccc', '猎头2期', 'Lily', 35000, 135000, '2022-05-21', 'kyle', 'kyle', 'kyle', '2021-06-05 18:21:27');

-- ----------------------------
-- View structure for guwen_month_offer
-- ----------------------------
DROP VIEW IF EXISTS `guwen_month_offer`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `guwen_month_offer` AS select `zoffer`.`offer_time` AS `offer_time`,sum(if((`ygoffer`.`yg_name` = 'kyle'),`ygoffer`.`yg_yeji`,0)) AS `kyle`,sum(if((`ygoffer`.`yg_name` = 'shelley'),`ygoffer`.`yg_yeji`,0)) AS `shelley`,sum(if((`ygoffer`.`yg_name` = 'raya'),`ygoffer`.`yg_yeji`,0)) AS `raya`,sum(if((`ygoffer`.`yg_name` = 'vera'),`ygoffer`.`yg_yeji`,0)) AS `vera`,sum(if((`ygoffer`.`yg_name` = 'amy'),`ygoffer`.`yg_yeji`,0)) AS `amy`,sum(if((`ygoffer`.`yg_name` = 'skye'),`ygoffer`.`yg_yeji`,0)) AS `skye`,sum(if((`ygoffer`.`yg_name` = 'cristina'),`ygoffer`.`yg_yeji`,0)) AS `cristina` from (`zoffer` left join `ygoffer` on((`ygoffer`.`offer_id` = `zoffer`.`id`))) group by `zoffer`.`offer_time` order by `zoffer`.`offer_time`;

SET FOREIGN_KEY_CHECKS = 1;
