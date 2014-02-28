# Gets the last line from e.g. an IRC log. Relies on e.g. irssi logging IRC.


def get_text(mode):
	if mode == "IRC":
                file = open("oxhack.log")
                lines = file.readlines()
                file.close()

                last_line = lines[-1]
                if (last_line[0:2] == ' <'):
                        last_line = last_line.split('> ', 1)[1] # Remove the first word, i.e. the nick, from the line
                else:
                        last_line = "SOS"

                return last_line
