from collections import Counter, defaultdict


def checking_anagram(keywords):
    agrms = defaultdict(list)
    for i in keywords:
        hist = tuple(Counter(i).items())
        agrms[hist].append(i)
    return list(agrms.values())


keywords = ("python", "yphotn")

print(checking_anagram(keywords))


# Another Function

def anagram_2(str1, str2):
    # convert both the strings into lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # check if length is same
    if (len(str1) == len(str2)):

        # sort the strings
        sorted_str1 = sorted(str1)
        sorted_str2 = sorted(str2)

        # if sorted char arrays are same
        if (sorted_str1 == sorted_str2):
            print(str1 + " and " + str2 + " are anagram.")
        else:
            print(str1 + " and " + str2 + " are not anagram.")

    else:
        print(str1 + " and " + str2 + " are not anagram.")


# function to check if two strings are
# anagram or not
def check(s1, s2):
    # the sorted strings are checked
    if (sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

    # driver code


s1 = "listen"
s2 = "silent"
check(s1, s2)


# Another method

