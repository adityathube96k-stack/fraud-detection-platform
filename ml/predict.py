


        result = ""

        for value, symbol in values:
            while num >= value:
                result += symbol
                num -= value
        return result



if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            if close_count < open_co
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(a, b):
            dummy = ListNode()
            tail = dummy

            while a and b:
                if a.val <= b.val:
                    tail.next = a
                    a = a.next
                else:
                    tail.next = b
                    b = b.next
                tail = tail.next

            tail.next = a if a else b
            return dummy.next

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                first = lists[i]
                second = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(merge(first, second))

            lists = merged

        return lists[0] if lists else None
