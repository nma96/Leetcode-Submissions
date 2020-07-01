class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = sum(nums[:3])

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                currSum = nums[i] + nums[left] + nums[right]

                # check if new sum is smaller than previous
                # if it is, update result
                if abs(currSum - target) < abs(result - target):
                    result = currSum

                # To find the other number sums, iterate through
                if currSum < target:
                    left += 1
                else:
                    right -= 1
        return result
