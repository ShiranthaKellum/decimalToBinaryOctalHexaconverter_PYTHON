
def converter (n):
    for i in range (1, n+1):
        print (
        str(i).rjust (len (str (bin (n)))-2, " "),                                      # decimal
        str (oct (i).replace ("0o", "")).rjust (len (str (bin (n)))-1, " "),            # octal convertion : replace method cut the 1st argumented value and replace it with the 2nd agrument
        str (hex(i).upper().replace("0X", "")).rjust(len(str(bin(n)))-1, " "),          # hexadeci convertion : rjust aligns the text to right with the distance of 1st argument fill it with second argument
        str(bin(i).replace("0b", "")).rjust(len(str(bin(n)))-1, " "),                   # binary convertion
        sep=""

        )

if __name__ == "__main__":
    x = int (input ())
    converter (x)
