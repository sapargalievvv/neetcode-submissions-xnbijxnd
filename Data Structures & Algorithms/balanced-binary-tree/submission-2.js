/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {boolean}
     */
    isBalanced(root) {
        let isOk = true;

        const getLevels = (root) => {
            if (!root) {
                return 0;
            }

            const left = getLevels(root.left);
            const right = getLevels(root.right);

            if (left - right > 1 || right - left > 1) {
                isOk = false;
            }

            return 1 + Math.max(left, right);
        };

        getLevels(root);

        return isOk;
    }
}
