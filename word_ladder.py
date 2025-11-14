#!/usr/bin/python3
# Word Ladder.
# You are given two words: begin_word and end_word,
# and a dictionary of words called word_list.
# Your task is to determine the length of the shortest
# transformation sequence from beginWord to endWord, such that:
# 1. Only one letter can be changed at a time.
# 2. Each transformed word must exist in the wordList.
# If no such transformation sequence exists, return 0.
# Constraints:
# * 1 <= begin_word.length <= 10
# * end_word.length == begin_word.length
# * 1 <= word_list.length <= 5000
# * All words consist of lowercase English letters.
# * begin_word and end_word are non-empty and may not be the same.

# Example:
begin_word = "hit"
end_word = "cog"
word_list = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# The shortest transformation sequence is:
# "hit" → "hot" → "dot" → "dog" → "cog"
# which has a length of 5.

# Solution:
# We need to find the shortest transformation from beginWord to endWord.
# That means we can treat this as a shortest path problem in a graph:
# Each word is a node.
# There’s an edge between two words if they differ by exactly one letter.
# We can then use Breadth-First Search (BFS) — it naturally finds
# the shortest path in an unweighted graph. Step-by-step logic:
# 1. Put all words in a set for fast lookup.
# 2. Use a queue for BFS, starting from begin_word.
# 3. For each word, try changing every letter (a–z) to see
#    if that new word is in the list.
# 4. If we find the end_word, return the number of steps.
# 5. Otherwise, keep going until the queue is empty (no path).

# Time O(N x L): 1. Visit each word N. 2. For each word, generate neighbors
# Space O(N): Generate word set O(N) and create the queue max O(N)
def ladder_length(begin_word, end_word, word_list):
    word_set = set(word_list)
    if end_word not in word_set:
        return 0

    queue = [(begin_word, 1)]  # (current_word, steps)

    while queue:
        word, steps = queue[0]  # Get the first element
        # Remove it (deque package would work
        # better for larger queues)
        queue = queue[1:]
        if word == end_word:
            # We've reached the target word
            return steps

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                if new_word in word_set:
                    word_set.remove(new_word)  # Avoid revisiting
                    queue.append((new_word, steps + 1))

    return 0


print(ladder_length(begin_word, end_word, word_list))
