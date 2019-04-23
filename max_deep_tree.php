/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($value) { $this->val = $value; }
 * }
 */
// 递归的调用
class Solution {

    /**
     * @param TreeNode $root
     * @return Integer
     */
    static function maxDepth($root) {
        // 1 2 4 8 16 32 68...
        if ($root == null) return 0;
        return max([static::maxDepth($root->left),static::maxDepth($root->right)])+1;
        
    }
}
