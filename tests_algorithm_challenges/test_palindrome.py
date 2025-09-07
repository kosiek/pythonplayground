
def get_palindrome_substrings(text: str) -> int:
    anagrams = 0
    for window_size in range(1, len(text)):
        print(f"\tAnagrams of length {window_size}")
        for text_start in range(len(text) - window_size + 1):
            text_end = text_start + window_size
            substring = text[text_start:text_end]
            substring_palindrome = substring[::-1]
            print(f"\t\tSubstring of size {window_size}: {substring}")
            for match_start in range(text_start + 1, len(text) - window_size + 1):
                match_end = match_start + window_size
                match = text[match_start:match_end]
                print(f"\t\t\tCompare {substring} vs {match}")
                if substring_palindrome == match:
                    print(f"\t\t\t\\Palindrome pair:  {substring} & {match}")
                    anagrams += 1
    print(f"TOTAL: {anagrams}")
    return anagrams
