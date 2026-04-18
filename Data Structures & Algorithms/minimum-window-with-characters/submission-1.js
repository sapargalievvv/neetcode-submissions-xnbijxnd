class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
    minWindow(s, t) {
        let left = 0;

        const windowCounts = {};
        const tCounts = {};

        for (let letter of t) {
            if (letter in tCounts) {
                tCounts[letter]++;
            } else {
                tCounts[letter] = 1;
            }
        }

        const need = Object.keys(tCounts).length;
        let have = 0;

        let res = [];
        let minWindow = Infinity;

        for (let i = 0; i < s.length; i++) {
            const right = s[i];

            if (right in tCounts) {
                windowCounts[right] = (windowCounts[right] || 0) + 1;

                if (windowCounts[right] === tCounts[right]) {
                    have++;
                }
            }

            while (have === need) {
                const windowSize = i - left + 1;

                if (windowSize < minWindow) {
                    minWindow = windowSize;
                    res = [left, i];
                }

                if (s[left] in tCounts) {
                    windowCounts[s[left]]--;

                    if (windowCounts[s[left]] < tCounts[s[left]]) {
                        have--;
                    }
                }

                left++;
            }
        }

        const [l, r] = res;

        return minWindow === Infinity ? "" : s.slice(l, r+1);
    }
}
