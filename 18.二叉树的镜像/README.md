## 二叉树的镜像
### 题目描述
操作给定的二叉树，将其变换为源二叉树的镜像。
### 解法
递归思想。
* 如果当前节点不为None，就交换它的子节点的位置。
* 再对当前节点的左右子节点进行上一步的操作。
