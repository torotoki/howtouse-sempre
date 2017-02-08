with open("raw_ClassDependency.md", "r") as raw:
    for line in raw:
        if (line.startswith(" ")): print line.strip()
