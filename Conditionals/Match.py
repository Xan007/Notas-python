comparisonList = []

match comparisonList:
    ###Busca especificamente que haya [cualquiera, "two", "seven"]
    case [first] | [first, "two", "seven"]: # | significa o
        print("this is the first element: {first}")
    case [title, "hello"] | ["hello", title]:
        print("Welcome esteemed guest {title}")
    case [first, *rest]: #* para el resto
        print("This is the first: {first}, and this is the rest: {rest}")
    case _: #El Default
        print("Nothing was matched")