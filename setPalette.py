import re

#colors [label 1, label 2 ...]
#colors = ['2b231a', '0b0e0f', '1a252b', '0b0a08', '515e64', '6b635a', 'ffb355', '68c4f2', 'ebb26c', '74b5d6', 'cba577', '79a4b9', 'ab9679', '78909d', '8b8174', '717b80']
colors = ['F6B32D', 'ec6717', 'a12019', 'ffdc3a', 'fff9f2', '101010', '5a6b65', '231813', '9d754e', 'c37671', '7e2315', 'ffcda3', '490813', '614704', '000000', 'ffffff']
i3Path = "/home/nicholas/.config/i3/config"
testPath = "/home/nicholas/.config/i3/scriptTests/testConfig"

def modifyI3(file_path):
	try:
		# Read the contents of the file
		with open(file_path, 'r') as file:
			file_contents = file.read()


		# Modify the hex code in the target string
		for i in range(16):
			file_contents = re.sub(r'set \$gp' + str(i+1) + r' #[0-9A-Fa-f]+', "set $gp" + str(i+1) + " #" + colors[i], file_contents)
	
		# Write the modified contents back to the file
		with open(file_path, 'w') as file:
			file.write(file_contents)

		print("Hex code modified successfully.")
	except FileNotFoundError:
		print("File not found:", file_path)
	except Exception as e:
		print("An error occurred:", str(e))

modifyI3(i3Path)
