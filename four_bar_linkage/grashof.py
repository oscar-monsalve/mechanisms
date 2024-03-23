def is_grashof(a: float, b: float, c: float, d: float) -> bool:
    min_len = min(a, b, c, d)
    max_len = max(a, b, c, d)
    other_links_sum = a + b + c + d - min_len - max_len
    print("Does the linkage satify the Grashof's law?")

    if min_len + max_len < other_links_sum:
        print("""Yes, it is a class I Grashof mechanism. Meaning at least one of the linkages will describe a full rotation.\n""")
        return True
    if min_len + max_len == other_links_sum:
        print("""Yes, it is a class III Grashof mechanism. Meaning at least one of the linkages will describe a full rotation and colineal
        positions will occur.\n""")
        return True
    if min_len + max_len > other_links_sum:
        print("No, is it a class II non-Grashof mechanism. Meaning no linkage will describe a full rotation.\n")
        return False
