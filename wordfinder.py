"""Word Finder: finds random words from a dictionary."""


import random


class WordFinder:
    def __init__(self, filepath):
        """
        Initailizes word count and list and opens the file

        Args:
            filepath (str): filepath of file to read "words.txt"

        Attributes:
            word_count (int): Number of words read from file
            word_list (list): List containing all the words from file
        """
        self.filepath = filepath
        self.word_count = 0
        self.word_list = []

        file = open(filepath, "r")
        self.print_words(file)
        file.close()

    def print_words(self, file):
        """
        Read file and prints out the number of words read

        Attributes:
            file (_type_): _description_
            file (file object): file object used to read from file
        """
        for line in file:
            self.word_count += 1
            self.word_list.append(line.rstrip("\n"))

        print(f"{self.word_count} words read.")

    def random(self):
        """
        Returns a random word from the list of words of the file

        Attributes:
            ran_idx (int): Random index to draw from the word list
            word_len (int): Length of the word list, used to find a random index
        """
        word_len = len(self.word_list)
        ran_idx = random.randint(0, word_len - 1)
        return self.word_list[ran_idx]
