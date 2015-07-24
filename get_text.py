# Gets the last line from e.g. an IRC log. Relies on e.g. irssi logging IRC.
import urllib

def get_text(mode):
	if mode == "IRC":
		urllib.urlretrieve("http://users.ox.ac.uk/~kebl3927/oxspace.log", "/home/pi/moarse/oxhack.log")
                file = open("/home/pi/moarse/oxhack.log")
                lines = file.readlines()
                file.close()

		filtered_lines = []
		for line in lines:
			if line[5:7] == ' <':
				filtered_lines.append(line)


                if (len(filtered_lines) != 0):
                        last_line = filtered_lines[-1].split('> ', 1)[1] # Remove the first word, i.e. the nick, from the line
                else:
                        last_line = "SOS"

                return last_line
