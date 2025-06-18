def find_the_redheads(family_dict):

    redheads_iter = filter(lambda name: family_dict[name] == "red", family_dict)

    return list(redheads_iter)

if __name__ == "__main__":
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    print(find_the_redheads(dupont_family))
