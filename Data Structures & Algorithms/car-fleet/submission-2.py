class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sp = sorted(zip(position, speed), reverse=True)
        stack = []

        for c_pos, c_speed in sp:
            time = (target - c_pos) / c_speed
            if not stack or time > stack[-1]:
                stack.append(time)  
            

        return len(stack)