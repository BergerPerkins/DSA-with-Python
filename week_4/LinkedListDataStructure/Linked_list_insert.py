class Node:
    def __init__(self, data):
        self.data = data
        self.nextPtr = None
class Linkedlist:
    #Linked list initialization
    def __init__(self):
        self.head = None

    # function to insert new data at the begining of the linked list
    # Time complexity : O(1)
    def insertAtBegining(self, new_data):
        new_node = Node(new_data)
        new_node.nextPtr = self.head
        self.head = new_node
    
    # print of all he node data values in a linked list
    def printLL(self):
        temp = self.head
        while temp:
            print(str(temp.data)+" ", end=" ")
            temp = temp.nextPtr

    # Function to insert new data at the end of the linked list
    # Time complexity : O(n)
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        # insertion at the very end of the linked list
        temp = self.head
        #reach towards the very last node of the linked list
        while temp.nextPtr:
            temp = temp.nextPtr
        temp.nextPtr = new_node

    # function to insert new data after a particular node
    # Time complexity : O(1)
    def insertAfterNode(self, prev_node, new_data):
        if prev_node is None:
            print("given node must be available inside linked list")
            return
        
        new_node = Node(new_data)
        new_node.nextPtr = prev_node.nextPtr
        prev_node.nextPtr = new_node

    # function to count the total number of nodes in a give linked list
    # Time complexity : O(n)
    def countNodes(self):
        count = 0
        temp = self.head
        while temp:
            count+=1
            temp = temp.nextPtr
        return count
    
    # function to search for a given data in a linked list, iff the data is available return true otherwise false
    # Time complexity : O(n)
    def searchNode(self, nodeData):
        if self.head is None:
            return False
        temp = self.head
        while temp:
            if temp.data == nodeData:
                return True
            temp = temp.nextPtr
        return False
    
    ## function to delete a node in a given Linked List
    def deleteNode(self, pos):



#Driver code
llist = Linkedlist()
#function calling
llist.insertAtBegining(10)
llist.insertAtBegining(20)
llist.insertAtBegining(40)
llist.insertAtBegining(70)
llist.insertAtBegining(90)
llist.insertAtEnd(100)
llist.insertAtEnd(120)
llist.insertAtEnd(150)
llist.insertAfterNode(llist.head.nextPtr.nextPtr, 30)

llist.printLL()

result = llist.countNodes()
print("The count of the number of nodes in a given linked list:", result)

nodeData = 130
if llist.searchNode(nodeData):
    print("Data is available in the given linked list")
else:
    print("Data is not available in the given linked list")