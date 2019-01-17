# https://leetcode.com/problems/add-two-numbers/
# Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.sumList(l1, l2)

    def sumList(self, lhs, rhs):
        current_node_lhs = lhs
        current_node_rhs = rhs
        step_in = False
        while(current_node_lhs.next != None and current_node_rhs.next != None):
            sum_val = current_node_lhs.val + current_node_rhs.val
            if step_in:
                sum_val += 1
                step_in = False
            current_node_lhs.val = sum_val % 10
            step_in = sum_val >= 10

            current_node_lhs = current_node_lhs.next
            current_node_rhs = current_node_rhs.next

        if current_node_lhs.next == None and current_node_rhs.next != None:
            sum_val = current_node_lhs.val + current_node_rhs.val
            if step_in:
                sum_val += 1
                step_in = False
            current_node_lhs.val = sum_val % 10
            step_in = sum_val >= 10
            pre = current_node_lhs
            current_node_lhs.next = current_node_rhs = current_node_rhs.next
            current_node_lhs = current_node_lhs.next
            while(current_node_lhs != None):
                sum_val = current_node_lhs.val
                if step_in:
                    sum_val += 1
                    step_in = False
                current_node_lhs.val = sum_val % 10
                step_in = sum_val >= 10

                pre = current_node_lhs
                current_node_lhs = current_node_lhs.next
        elif current_node_lhs.next != None and current_node_rhs.next == None:
            sum_val = current_node_lhs.val + current_node_rhs.val
            if step_in:
                sum_val += 1
                step_in = False
            current_node_lhs.val = sum_val % 10
            step_in = sum_val >= 10
            pre = current_node_lhs
            current_node_lhs = current_node_lhs.next
            while(current_node_lhs != None):
                sum_val = current_node_lhs.val
                if step_in:
                    sum_val += 1
                    step_in = False
                current_node_lhs.val = sum_val % 10
                step_in = sum_val >= 10

                pre = current_node_lhs
                current_node_lhs = current_node_lhs.next
        elif current_node_lhs.next == None and current_node_rhs.next == None:
            sum_val = current_node_lhs.val + current_node_rhs.val
            if step_in:
                sum_val += 1
                step_in = False
            current_node_lhs.val = sum_val % 10
            step_in = sum_val >= 10
            pre = current_node_lhs

        if step_in:
            pre.next = ListNode(1)

        result = []
        while(lhs != None):
            result.append(lhs.val)
            lhs = lhs.next
        return result

    def printList(self, link_list):
        i = 0
        current_node = link_list
        while(current_node != None):
            if current_node.next == None:
                next = 'null'
                print(f"index: {i}, value: {current_node.val}, next: {next}")
            else:
                next = 'not null'
                print(f"index: {i}, value: {current_node.val}, next: {next}")
            current_node = current_node.next
            i += 1

    def buildList(self, numbers):
        for index, number in enumerate(numbers):
            if index == 0:
                pre = link_list = ListNode(number)
            else:
                linkNode = ListNode(number)
                pre.next = linkNode
                pre = linkNode

        return link_list


if __name__ == '__main__':
    solution = Solution()
    l1_numbers = [9,9]
    l2_numbers = [9]
    l1_numbers = [2,4,5]
    l2_numbers = [5,6,4]
    l1_numbers = [0]
    l2_numbers = [9,9]
    l1_list = solution.buildList(l1_numbers)
    l2_list = solution.buildList(l2_numbers)

    solution.addTwoNumbers(l1_list, l2_list)
