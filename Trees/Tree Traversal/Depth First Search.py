class Node:
  def __init__(self, value: any) -> None:
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self) -> None:
    self.root = None

  def insert(self, value : any) -> bool:
    new_node : Node = Node(value)
    
    if self.root is None:
      self.root = new_node
      return True
    
    temp = self.root

    while True:
      if new_node.value == temp.value:
        return False
      
      if new_node.value < temp.value:
        if temp.left is None:
          temp.left = new_node
          return True
        
        temp : Node = temp.left
      
      else:
        if temp.right is None:
          temp.right = new_node
          return True
        
        temp = temp.right
  
  def contains(self, value) -> bool:
    temp : Node = self.root

    while temp is not None:
      if value < temp.value:
        temp = temp.left
      elif value > temp.value :
        temp = temp.right
      else:
        return True
    return False
  
  def __r_contains(self, current_node : Node, value : any) -> bool:
    if current_node == None:
      return False
    
    if value == current_node.value:
      return True
    
    if value < current_node.value:
      return self.__r_contains(current_node.left, value)
    
    if value > current_node.value:
      return self.__r_contains(current_node.right, value)
    
  def r_contains(self, value : any) -> bool:
    return self.__r_contains(self.root, value)
  
  def __r_insert(self, current_node : Node, value: any) -> Node | None:
    if current_node == None:
      return Node(value)

    if value < current_node.value:
      current_node.left = self.__r_insert(current_node.left, value)
    
    if value > current_node.value:
      current_node.right = self.__r_insert(current_node.right, value)
    
    return current_node

  def r_insert(self, value : any) -> None:
    if self.root == None:
      self.root = Node(value)
    self.__r_insert(self.root, value)

  def __delete_node(self, current_node : Node, value : any) -> Node | None:
    if current_node == None:
      return None

    if value < current_node.value:
      current_node.left = self.__delete_node(current_node.left, value)

    elif value > current_node.value:
      current_node.right = self.__delete_node(current_node.right, value)
    
    else:
      if current_node.left == None and current_node.right == None:
        return None
      
      elif current_node.left == None:
        current_node = current_node.right
      
      elif current_node.right == None:
        current_node = current_node.left
      
      else:
        sub_tree_min : any = self.min_value(current_node.right)
        current_node.value = sub_tree_min
        current_node.right = self.__delete_node(current_node.right, sub_tree_min)

    return current_node

  def delete_node(self, value : any) -> None:
    self.__delete_node(self.root, value)

  def min_value(self, current_node : Node) -> any:
    while current_node.left is not None:
      current_node = current_node.left
    return current_node.value
  
  def DFS_pre_order(self) -> list[int]:
    result : list[int] = []

    def traverse(current_node : Node):
      result.append(current_node.value)

      if current_node.left is not None:
        traverse(current_node.left)
      
      if current_node.right is not None:
        traverse(current_node.right)
    
    if self.root is not None:
      traverse(self.root)
    
    return result
  
  def DFS_in_order(self) -> list[int]:
    result : list[int] = []

    def traverse(current_node : Node):
      if current_node.left is not None:
        traverse(current_node.left)
      
      result.append(current_node.value)
      
      if current_node.right is not None:
        traverse(current_node.right)

    if self.root is not None:
      traverse(self.root)
    
    return result
  
  def DFS_post_order(self) -> list[int]:
    result : list[int] = []

    def traverse(current_node : Node):
      if current_node.left is not None:
        traverse(current_node.left)
      
      if current_node.right is not None:
        traverse(current_node.right)
      
      result.append(current_node.value)
    
    if self.root is not None:
      traverse(self.root)
    
    return result


def main() -> None:
  
  my_tree = BinarySearchTree()
  my_tree.insert(47)
  my_tree.insert(21)
  my_tree.insert(76)
  my_tree.insert(18)
  my_tree.insert(27)
  my_tree.insert(52)
  my_tree.insert(82)

  print(f"Pre Order  ==> {my_tree.DFS_pre_order()}")
  print(f"In Order   ==> {my_tree.DFS_in_order()}")
  print(f"Post Order ==> {my_tree.DFS_post_order()}")

if __name__ == "__main__":
  main()

"""
  EXPECTED OUTPUT:
  -----------------------------
  Pre Order  ==> [47, 21, 18, 27, 76, 52, 82]
  In Order   ==> [18, 21, 27, 47, 52, 76, 82]
  Post Order ==> [18, 27, 21, 52, 82, 76, 47]
  -----------------------------
 """