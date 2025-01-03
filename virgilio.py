"""Define Virgilio class."""

# imported for handle fily system.
import os

# imported for handle math operations.
import math

# imported for handling json files.
import json

# get the current work directory.
CWD = os.getcwd()
# change work directory.
CANTOS_FOLDER_DIRECTORY = os.chdir("canti")
# get the current path after we moved on the canti folder.
CANTOS_DIRECTORY = os.getcwd()


class Virgilio:
    """A Class rapresenting Virgilio with a directory.

    Attributes:
        directory (str): The path of the folder which conatins the Cantos.

    """

    class CantoNotFoundError(FileNotFoundError):
        """Class for manage errors realtives to File not found error.

        Args:
            FileNotfoundError (cls): Catch all excpetions that are FileNotFound

        """

        def __init__(self) -> None:
            """ Passing the error msg wich is going to be associated\
            to the excpetion istance.

            """
            super().__init__("canto_number must be between 1 and 34.")

    def __init__(self, directory: str) -> None:
        """Initialize a new Virgilio object with a directory.

        Args:
            directory (str): The path of the folder which conatins the Cantos.

        """
        self.directory = directory

    def read_canto_lines(
            self,
            canto_number: int,
            strip_lines: bool = False,
            num_lines: int = None
    ) -> list[str]:
        """Read the specified Canto file .txt.
        Return a list of the verses.

        Args:
            canto_number (int): The number of the Canto.
            strip_lines (bool): If True split() each verse.
            num_lines (int):

        """

        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")

        try:

            """ if canto_number is not valid we raise
            the personalized error class.

            """
            if not 1 <= canto_number <= 34:
                raise self.CantoNotFoundError

            # check if canto_number,num_lines are set and == INT
            if canto_number and not isinstance(canto_number, int):
                raise TypeError("canto_number must be an integere")
            if num_lines and not isinstance(num_lines, int):
                raise TypeError("num_lines must be an integere")

            final_list = []

            with open(file_path, "r", encoding="utf-8") as file:
                canto_verses = file.readlines()

                """ check the value of strip_lines
                before split() verses.

                """
                if strip_lines:

                    """check the value of num_lines before
                    returning just the range of verses of the Canto.

                    """
                    if num_lines:
                        canto_verses = canto_verses[0:num_lines]

                    for verse in canto_verses:
                        cleared_verse = verse.strip()
                        final_list.append(cleared_verse)
                else:

                    """check the value of num_lines before returning
                    just the range of verses of the Canto.

                    """
                    if num_lines:
                        canto_verses = canto_verses[0:num_lines]

                    final_list.extend(canto_verses)

            return final_list

        except self.CantoNotFoundError as canto_file_error:
            return canto_file_error
        except TypeError as type_error:
            return type_error
        except Exception:
            return f"Error while opening {file_path}"

    def count_verses(self, canto_number: int) -> int:
        """Count the number of verses in the specified Canto.

        Arg:
            canto_number (int): The number of the Canto.

        """
        # calculate the list lenght returned by the method read_canto_lines.
        canto_verses = self.read_canto_lines(canto_number)

        total_canto_verses = len(canto_verses)

        return total_canto_verses

    def count_tercets(self, canto_number: int) -> int:
        """Count the number of tercets in a Canto.

        Args:
            canto_number (int): used for get the number of verses
            in a specific Canto.

        """

        # num of verses in a Canto.
        total_canto_verses = self.count_verses(canto_number)

        # math.floor() used for round the number to the nearest int.
        canto_tercets = math.floor(total_canto_verses / 3)

        return canto_tercets

    def count_word(self, canto_number: int, word: str) -> int:
        """Count how many times a word appear in the Canto.

        Args:
            canto_number (int): The number of the Canto.
            word (str): The word to search inside the canto.

        """

        #  List and join verses of a Canto.
        canto_verses = self.read_canto_lines(canto_number)
        separator = ""
        joined_canto = separator.join(canto_verses)

        # print(joined_canto)
        word_count = joined_canto.count(word)

        return word_count

    def get_verse_with_word(self, canto_number: int, word: str) -> str:
        """Get the first verse which contains the indicated word.

        Args:
            canto_number (int): The number of the Canto.
            word (str): the world we are looking for inside each verse.

        """

        canto_verses = self.read_canto_lines(canto_number)

        # cicling on every verse for searching the word.
        for verse in canto_verses:

            # if word in verse we return it.
            if word in verse:
                return verse

    def get_verses_with_word(self, canto_number: int, word: str) -> list[str]:
        """Return a list of every verse which contains the indicated word.

        Args:
            canto_number (int): The number of the Canto.
            word (str): the world we are looking for inside each verse.

        """

        canto_verses = self.read_canto_lines(canto_number)

        canto_verses_with_word = []

        # cicling on every verse for searching the word.
        for verse in canto_verses:

            # if found we append the verse in the new empty list.
            if word in verse:
                canto_verses_with_word.append(verse)

        return canto_verses_with_word

    def get_longest_verse(self, canto_number: int) -> str:
        """Get the longest verse of a specific Canto.

        Args:
            canto_number (int): The number of the Canto.

        """

        canto_verses = self.read_canto_lines(canto_number)

        # for i,verse in enumerate(canto_verses):
        #     print(i, len(verse), sep="-")

        """
        max_len = 0
        for verse in canto_verses:
            if len(verse) > max_len:
                max_len = len(verse)
                longest_verse = verse
        return longest_verse

        """

        # The max function return the longest verse.
        longest_verse = max(
            canto_verses,
            key=len  # key=len checks each verse lenght
            )

        return longest_verse

    def get_longest_canto(self) -> dict[str, int]:
        """Get the Canto with the most verses and the num of those."""

        # counter for save the highest number of verses.
        canto_verses_counter = 0

        # declared an empty dictionary to populate
        longest_canto = {}

        for canto in range(1, 35):
            # counting the verse of cantos from 1 to 34.
            canto_total_verses = self.count_verses(canto)
            if canto_total_verses > canto_verses_counter:
                # updating the counter for the comparison of the verses num
                canto_verses_counter = canto_total_verses

                # 2 variables: the canto num and it's total num of verser
                longest_canto_num = canto
                longest_cardio_total_verses = canto_total_verses
                # adding the 2 keys/values to the previusly created dictionary
                longest_canto["canto_number"] = longest_canto_num
                longest_canto["canto_len"] = longest_cardio_total_verses

        return longest_canto

    def count_words(
            self,
            canto_number: int,
            words: list[str]
            ) -> dict[str, int]:
        """Return a dictionary which has x elements,
        where x is the number of words passed, using
        as key the word and as value the number of times
        it happears in the Canto.

        Args:
            canto_number (int): The number of the Canto.
            words (list[str]): The list of words to count inside the Canto.

        """
        words_in_canto = {}
        #  list of verses in the canto.
        canto_verses = self.read_canto_lines(canto_number)
        separator = ""
        joined_canto = separator.join(canto_verses)

        for word in words:
            if word in joined_canto:
                word_count = joined_canto.count(word)
                words_in_canto[word] = word_count

        with open(
            f"{CANTOS_DIRECTORY}/word_counts.json",
            "w",
            encoding="utf-8"
            ) as json_file:
            json.dump(words_in_canto, json_file, indent=4, ensure_ascii=False)

        return words_in_canto

    def get_hell_verses(self) -> list[str]:
        """Return a list with all the Cantos
        of Inferno (34) verses; from the first to the last.

        """

        # declration of an empty list
        hell_verses = []

        # cicle Cantos and concatenate the verses in a list
        for canto in range(1, 35):
            canto_verses = self.read_canto_lines(canto)
            hell_verses += canto_verses

        # debug: for handling the possible excessive lenght of the print
        with open("../hell_verses.txt", "w", encoding="utf-8") as file:
            for verse in hell_verses:
                file.write(verse.strip() + "\n")

        return hell_verses

    def count_hell_verses(self) -> int:
        """Get the count INT representing total num
        of verses in the Inferno Canto.

        """
        total_hell_verses = self.get_hell_verses()
        len_hell_verses = len(total_hell_verses)

        return len_hell_verses

    def get_hell_verse_mean_len(self) -> float:
        """Get the mean lenght of the verses inside
        the Inferno canto.

        """

        hell_verses_list = self.get_hell_verses()
        total_num_verses = self.count_hell_verses()

        total_len_verses = 0

        # sum the len of each verse inside the variable total_len_verses
        for hell_verse in hell_verses_list:
            total_len_verses += len(hell_verse.strip())

        mean_len_verses = total_len_verses / total_num_verses

        return mean_len_verses


virgilio = Virgilio(CANTOS_DIRECTORY)


print(type(virgilio.read_canto_lines(1)))
print(virgilio.read_canto_lines(1))
print(type(virgilio.read_canto_lines(1, True)))
print(virgilio.read_canto_lines(1, True))
print(type(virgilio.read_canto_lines(1.2, True, 5)))
print(virgilio.read_canto_lines(1.2, True, 5))
print(type(virgilio.read_canto_lines(1, True, 5.2)))
print(virgilio.read_canto_lines(1, True, 5.2))
print(type(virgilio.read_canto_lines(36, True, 2)))
print(virgilio.read_canto_lines(36, True, 2))
print(type(virgilio.read_canto_lines(1, True, 2)))
print(virgilio.read_canto_lines(1, True, 2))
print(virgilio.read_canto_lines("test"))

print(type(virgilio.count_verses(1)))
print(virgilio.count_verses(1))

print(type(virgilio.count_tercets(1)))
print(virgilio.count_tercets(1))

print(type(virgilio.count_word(1, "i")))
print(virgilio.count_word(1, "a"))

print(type(virgilio.get_verse_with_word(1, "natura")))
print(virgilio.get_verse_with_word(1, "che"))

print(type(virgilio.get_verses_with_word(1, "e")))
print(virgilio.get_verses_with_word(1, "e"))
print(len(virgilio.get_verses_with_word(1, "e")))

print(type(virgilio.get_longest_verse(1)))
print(virgilio.get_longest_verse(1))

print(type(virgilio.get_longest_canto()))
print(virgilio.get_longest_canto())

print(type(virgilio.count_words(1, ["a", "b", "c", "d"])))
print(virgilio.count_words(1, ["a", "b", "c", "d", "e"]))

print(type(virgilio.get_hell_verses()))
# too long for the terminal, check hell_verses.txt.
# print(virgilio.get_hell_verses())

print(type(virgilio.count_hell_verses()))
print(virgilio.count_hell_verses())

print(type(virgilio.get_hell_verse_mean_len()))
print(virgilio.get_hell_verse_mean_len())
