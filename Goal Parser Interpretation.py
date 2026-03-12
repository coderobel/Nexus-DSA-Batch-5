class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        output = ""
        length = len(command) - 1
        index = 0
        while index <= length:
            if command[index] == "G":
                output += "G"
            elif command[index] == "(" and command[index + 1] == ")":
                output += "o"
            elif command[index] == "(" and command[index + 1] == "a":
                output += "al"
            index += 1
        return output        
