class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const groupsMap = {} 

        strs.forEach((str) => {
            const sorted = [...str.split("")].sort().join("");

            if (groupsMap[sorted]) {
                groupsMap[sorted].push(str);
            } else {
                groupsMap[sorted] = [str];
            }
        });

        console.log("groupsMap", groupsMap);
        return Object.values(groupsMap)
    }
}
