class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # count = 0
        # for index, value in enumerate(input):
        #     count += 1
        #     print('index', index, 'value ', value)

        #     ind = 0
        #     for i in input:
        #         ind += 1
        #         sum = value + i
        #         if sum == target:
        #             return index, count + ind - 2

        """My solve """
        count = 0
        index = 0
        for j in nums:
            count += 1

            ind = 0
            for i in nums[count:]:
                ind += 1
                sum = i + j
                if sum == target:
                    return index, count + ind - 1
        index += 1
            
        """ Best practise """

        # class Solution(object):
        #     def twoSum(self, nums, target):
        #         HashMap = {}
        #         for i, num in enumerate(nums):
        #             diff = target - num
        #             if diff in HashMap:
        #                 return [HashMap[diff], i]
        #             HashMap[num] = i
        #         return
        
input = [3,2,4]
target = 6

# result 0,3
sol = Solution()
print(sol.twoSum(input, target))

