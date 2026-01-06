from collections import deque

def find_max_sum_level(root):
    if not root:
        return -1 # Or 0, depending on your preference

    queue = deque([root])
    
    max_sum = float('-inf') # Initialize with a very small number
    max_level = 0
    current_level = 0

    while queue:
        level_size = len(queue)
        current_level_sum = 0
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level_sum += node.val
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Check if this level's sum is the best we've seen
        if current_level_sum > max_sum:
            max_sum = current_level_sum
            max_level = current_level
            
        current_level += 1 # Move to the next floor
    
    return max_level