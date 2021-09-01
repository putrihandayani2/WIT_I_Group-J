"""
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")


#minimize the number of print() function invocations by inserting the \n sequence into the strings
print("    *", "\n   * *", "\n  *   *", "\n *     *", "\n***   ***", "\n  *   *", "\n  *   *", "\n  *****")

"""
#make the arrow twice as large (but keep the proportions)
print(" " * 7 + "*" + " " * 0 +"\n"
    + " " * 6 + "*" + " " * 1 + "*\n"
    + " " * 5 + "*" + " " * 3 + "*\n"
    + " " * 4 + "*" + " " * 5 + "*\n"
    + " " * 3 + "*" + " " * 7 + "*\n"
    + " " * 2 + "*" + " " * 9 + "*\n"
    + " " * 1 + "*" + " " * 11 + "*\n"
    + "*" * 5 + " " * 5 + "*" * 5 + "\n"
    + (" " * 4 + "*" + " " * 5 + "*\n") * 4
    + (" " * 4 + "*" * 6 + "*\n"))
