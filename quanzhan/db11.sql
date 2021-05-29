/*
 Navicat MySQL Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80023
 Source Host           : localhost:3306
 Source Schema         : db10

 Target Server Type    : MySQL
 Target Server Version : 80023
 File Encoding         : 65001

 Date: 29/05/2021 22:19:58
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for class
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `class` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

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
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

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
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

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

SET FOREIGN_KEY_CHECKS = 1;
