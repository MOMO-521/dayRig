
'''
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1：

输入：nums = [3,2,3]
输出：3
示例 2：

输入：nums = [2,2,1,1,1,2,2]
输出：2

求数组中的众数
摩尔投票法——抵消思想，第一：vote == 0 中立状态，那么选择当前的候选人
第二：当前票是候选人的，则票数加一
第三：不是当前候选人，则抵消一张候选人的票，即票数减一
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0            # 候选人票数
        candiate = nums[0]  # 候选人
        for item in nums:      # 遍历所有票
            if vote == 0:       # 如果候选人一张票没有就是中立，就选当前人为候选人
                candiate = item  
            if item == candiate:    # 当前票是候选人的，则票数加一
                vote+=1
            else:                   # 不是当前候选人，则抵消一张候选人的票，即票数减一
                vote-=1
        return candiate
        
