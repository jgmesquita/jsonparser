from JSON.ObjectJSON import ObjectJSON

def main():
    json_file = ObjectJSON("test.json")  # Create object 
    json_file.print()                    # Print to the terminal
    json_file.get("skills")              # Print to the terminal the value from a field
    json_file.set("age", 24)             # Field exists
    json_file.set("Test", 1)             # Field doesn't exist
    json_file.serialize("output.json")   # Output to another file

if __name__ == "__main__":
    main()