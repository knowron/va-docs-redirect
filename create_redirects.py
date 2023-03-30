import glob, os

redirect = """
<!DOCTYPE html>
<meta charset="utf-8">
<title>Redirecting to https://docs.virtualassist.smt.asmpt.com/replace_me/</title>
<meta http-equiv="refresh" content="0; URL=https://docs.virtualassist.smt.asmpt.com/replace_me/">
<link rel="canonical" href="https://docs.virtualassist.smt.asmpt.com/replace_me/">
"""
redirect_german = """
<!DOCTYPE html>
<meta charset="utf-8">
<title>Redirecting to https://docs.virtualassist.smt.asmpt.com/de/replace_me/</title>
<meta http-equiv="refresh" content="0; URL=https://docs.virtualassist.smt.asmpt.com/de/replace_me/">
<link rel="canonical" href="https://docs.virtualassist.smt.asmpt.com/de/replace_me/">
"""

if __name__ == "__main__":
    # Get all .md files from a specirfic directory
    files = glob.glob("../docs/**/*.md", recursive=True)    
    # Loop through all files
    for file in files:
        # Trim the path to the file
        file = file.replace("../docs/docs/", "")
        # get rid of the extension for all files
        file = file.replace(".en.", ".")
        file = file.replace(".de.", ".")
        file = file.replace(".md", "")
        # Create directory with the name of the file
        folder_path = os.path.join(".", file)
        # recursively create the directory
        os.makedirs(folder_path, exist_ok=True)
        # Create index.html file in the directory
        f = open(os.path.join(file, "index.html"), "w")
        # Write the redirect code to the file
        f.write(redirect.replace("replace_me", file))
        f.close()

        # now create the german version
        german_path = os.path.join(".", "de", file)
        print(german_path)
        # recursively create the directory
        os.makedirs(german_path, exist_ok=True)
        # Create index.html file in the directory
        print(redirect_german.replace("replace_me", german_path))

        f = open(os.path.join(german_path, "index.html"), "w")
        # Write the redirect code to the file
        f.write(redirect_german.replace("replace_me", file))
        f.close()

        