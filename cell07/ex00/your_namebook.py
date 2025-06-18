def array_of_names(person_dict):
    full_names = []
    for first, last in person_dict.items():
        
        full_name = first.capitalize() + " " + last.capitalize()
        full_names.append(full_name)
    return full_names


if __name__ == "__main__":
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    print(array_of_names(persons))
