# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = [] #Создание списка
        while head: #пока есть элементы
            list.append(head.val) #Добавить к списку
            head = head.next #Перейти к следующему элементу
        return l == l[::-1]    #Если изначальный список равен перевернутому