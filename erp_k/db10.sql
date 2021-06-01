/*
 Navicat MySQL Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 80023
 Source Host           : localhost:3306
 Source Schema         : db10

 Target Server Type    : MySQL
 Target Server Version : 80023
 File Encoding         : 65001

 Date: 01/06/2021 22:36:24
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
) ENGINE = InnoDB AUTO_INCREMENT = 24 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

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
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of test01
-- ----------------------------

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

SET FOREIGN_KEY_CHECKS = 1;
