class Solution:

    def encode(self, strs: List[str]) -> str:
        # FOR EACH WORD KEEP TRACK OF HOW MANY CHARACTERS AND ADD A DELIMITTER BEFORE TAKING ADDING THE CHARS INTO THE STRING
        delimitter = "#"
        result = ""
        for word in strs:
            length = str(len(word))
            result = result + length + delimitter + word
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            # find the delimitter and increment until we find the word then set our j index to the beginning of the word 
            while s[j] != "#":
                j += 1
            
            # determine the length of the charaters to read 
            # for example all this is doing is getting the first "5" from our encoded string: 5#Hello5#World
            length  = int(s[i:j])

            # set our starting index value for the word
            start_index = j + 1

            # end index is start_index + length
            end_index = (start_index + length)
    
            word = ""
            word = (s[start_index : end_index]) #read the word from start index and end index 
            
            result.append(word)
            i = end_index
        
        return result
            
