"""Spcial Word Finder, read files with blank spaces and special symbols."""

from wordfinder import WordFinder


class SpecialWordFinder(WordFinder):
    def __init__(self, filepath):
        """
        Args:
            filepath (str): filepath to read is "special_words.txt"
        """
        super().__init__(filepath)

    def print_words(self, file):
        """
        Read file and prints out the number of words read excluding the special characters

        Attributes:
            file (_type_): _description_
            file (file object): file object used to read from file
        """
        for line in file:
            if not line.strip() or line[0] == "#":
                continue
            self.word_count += 1
            self.word_list.append(line.rstrip("\n"))

        print(f"{self.word_count} words read.")
