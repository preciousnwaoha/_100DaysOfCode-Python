from tkinter import X
from unittest.util import _MAX_LENGTH


birds = ["hen", "parrot", "eagle", "chicken", "falcon"]
mammals = ["goat", "dog", "cat", "ram"]
reptiles = ["snake", "turtle", "crocodile", "dinasour"]


# def longest_len(arr):
#     num = 0
#     for bird in arr:
#         if len(bird) > num:
#             num = len(bird)
#     return num

# def joiner(*arrs):
#     new_list = []
#     for item in list(arrs):
#         for i in item:
#             new_list.append(i)
#     return longest_len(new_list)

# def configure(arr, num):
#     new_arr = []
#     for word in arr:
#         word_len = len(word)
#         adder = num - word_len
#         space = ""
#         for i in range(adder):
#             space = space + " "
#         addee = space + word
#         new_arr.append(addee)
#     return new_arr

# def grouper(*arrs):
#     data = ""
#     data_arrs = []
#     data_arrs_lens = []
#     maxer = joiner(*arrs)
#     for arr in arrs:
#         data_arrs.append(configure(arr, maxer))
#     for arr in data_arrs:
#         data_arrs_lens.append(len(arr))
#     idx = 0
#     # num_check = max(data_arrs_lens)
#     # print(data_arrs_lens)
#     for num in data_arrs_lens:
#         for arr in data_arrs:
#             if arr[idx]:
#                 data = data + "\t" +  arr[idx]
#             else:
#                 temp = ""
#                 for l in range(maxer):
#                     temp = temp + "\t"
#                 data = data + "\t" + temp 
#         idx = idx + 1
#         data = data + "\n\n"
        
#     return data

# print(grouper(birds, mammals, reptiles))

# print('madshfdiod'.rjust(20, '.'))




def longest_lengths(*arrs):
    word_lens_max = []
    new_word_arrs = []
    for word_arr in arrs:
        x = []
        for word in word_arr:
            x.append(len(word))
        word_lens_max.append(max(x))
        for word in word_arr:
            x.append(len(word))
        
        # for num in range(len(word_arr)):
        #     print(f"\n{word_arr[num]} +")
    print(word_lens_max)
    
        
longest_lengths(birds, mammals, reptiles)