from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        unable = len(students)
        queue = deque(students)

        for sandwich in sandwiches:
            rotations = 0
            while rotations < len(queue) and queue[0] != sandwich:
                queue.append(queue.popleft())
                rotations += 1
            
            if queue and queue[0] == sandwich:
                queue.popleft()
                unable -= 1
            else:
                break
        return unable