# Gets the last line from e.g. an IRC log. Relies on e.g. irssi logging IRC.


def get_text():
        file = open("example.log")
        lines = file.readlines()
        file.close()

        last_line = lines[-1]

        return last_line
