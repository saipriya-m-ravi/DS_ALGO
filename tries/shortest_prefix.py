class TrieNode:
    def __init__(self):
        self.children = {}
        self.freq = 0


class Solution:
    def prefix(self, A):
        
        root = TrieNode()

        # Insert words
        for word in A:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                node.freq += 1

        result = []

        # Find unique prefix
        for word in A:
            node = root
            prefix = ""
            
            for ch in word:
                node = node.children[ch]
                prefix += ch
                
                if node.freq == 1:
                    break
            
            result.append(prefix)

        return result