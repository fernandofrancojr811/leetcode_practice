from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        buckets = [0] * (n+1) # this is saying we have buckets like this is we had array [1,2,3 ] we would have 4 buckets => [0,0,0,0], so n + 1
        #they are all initialized to 0, meaning how many items show up [0, 0, 0, 0 ]....
        #                                                               0x 1x 2x 3x ....
        for num, freq in counter.items(): #for each number and freq in side the counter array we created
            if buckets[freq] == 0:      # if the bucket at that freq is empty
                buckets[freq] = [num]  # then fill it with that num
            else:
                buckets[freq].append(num) #if its already full then add the num to the list

            #next we want to iterate the array backwards and add the items backwards into a new list

        ret = []

        for i in range(n, -1, -1): #starting at n because we have n + 1 things in the array, down to -1 exclusive so we end at zero, decrimenting by 1
            if buckets[i] != 0:
                ret.extend(buckets[i])  #if the bucket is not zero we extend the ret array
            if len(ret) == k: #once we have the ret aray be the size of k ret break and return ret
                break

        return ret
