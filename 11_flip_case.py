def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # This line does not work but is here for questions
    # return [ltr.upper() if ltr == ltr.lower() else ltr.lower() for ltr in phrase if ltr.upper() == to_swap.upper()]

    result_phrase = []

    for ltr in phrase:
        if ltr.upper() == to_swap.upper():
            if ltr == ltr.upper():
                result_phrase.append(ltr.lower())
            else:
                result_phrase.append(ltr.upper())
        else:
            result_phrase.append(ltr)

    return ''.join(result_phrase)
