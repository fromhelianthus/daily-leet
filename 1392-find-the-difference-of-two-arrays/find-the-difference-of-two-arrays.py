class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # 배열 nums1과 nums2가 주어질 때,
        # 각 배열의 요소 중 다른 배열의 요소와 중복되지 않는 요소만 남기고
        # 두 결과를 하나의 배열에 담아 리턴하기
        
        # 공통 요소를 제거하기
        set1 = set(nums1)
        set2 = set(nums2)

        distinct_set1 = set1 - set2
        distinct_set2 = set2 - set1

        # 공통요소가 제거된 각 배열을 result에 담기
        # set은 객체를 반환하므로 배열(list)로 변환해야 함

        # result = [[], []] 위에서 초기화를 한 후 값을 대입하지 않고,
        # result를 초기화하면서 동시에 리스트로 변환하여 할당하기
        result = [list(distinct_set1), list(distinct_set2)]

        return result
        
