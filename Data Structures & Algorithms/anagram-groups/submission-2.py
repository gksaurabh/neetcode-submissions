def sort_word(s: str) -> str:
        sorted_list = sorted(s)
        result = ""
        for char in sorted_list:
            result += char
        
        return result

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        expanded_list = {} #sorted_word : word_list

        for word in strs:
            if expanded_list:
                sorted_word = sort_word(word)
                if sorted_word in expanded_list.keys():
                    expanded_list[sorted_word].append(word)
                else:
                    expanded_list[sorted_word] = [word]
            else:
                sorted_word = sort_word(word)
                expanded_list[sorted_word] = [word]

        return list(expanded_list.values())