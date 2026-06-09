class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        r=[]
        for i in range(len(sentences)):
            s=len(sentences[i].split())
            r.append(s)
        return max(r)        