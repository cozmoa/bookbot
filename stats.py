def word_count(x):
    words = x.split()
    return len(words)
def count_chars(text):
    count_char = {}
    lower_text = text.lower()
    
    for char in lower_text:
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1
            
    return count_char

def order(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        char_info = {"char": char, "num": count}
        chars_list.append(char_info)
    
    def sort_on(dict):
        return dict["num"]
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list
    
