class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "[]"
        encoded_string = ""
        for string in strs:
            encoded_string += string
            encoded_string += "XXX"
        return encoded_string[:-3]
    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []
        return s.split("XXX")
