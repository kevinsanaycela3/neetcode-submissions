class Solution:
    def isValid(self, s: str) -> bool:
        compare = []
        n = len(s)
        my_dict = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        if len(s) % 2 != 0:
            return False
        else:
            for char in s:
                if char in my_dict.values():
                    compare.append(char)
                if char in my_dict.keys():
                    if compare == []:
                        return False
                    else:
                        if compare[-1] == my_dict[char]:
                            compare.pop()
                        else:
                            return False
            
            if compare == []:
                return True
            else:
                return False

        
        
        

                

            

            

        

        




            
        