class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if list(moves).count("R") == list(moves).count("L") and list(moves).count("U") == list(moves).count("D"):
            return True
        else:
            return False