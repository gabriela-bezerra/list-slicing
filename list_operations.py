"""Utilities for manipulating lists."""


def head(input_list):
    """Return the first item of the input list.

    For example:

      >>> head(['Jan', 'Feb', 'Mar'])
      'Jan'
    """
    get_head = input_list[0]

    return get_head


def tail(input_list):
    """Return a new list of all items, excluding the first item.

    For example:

    >>> tail(['Jan', 'Feb', 'Mar'])
    ['Feb', 'Mar']

    """

    get_tail = input_list[1:]

    return get_tail


def last(input_list):
    """Return the last item of the input list.

    For example:

    >>> last(['Jan', 'Feb', 'Mar'])
    'Mar'

    """

    get_last = input_list[-1]

    return get_last


def top(input_list):
    """Return all elements of the input list except the last.

    For example:

    >>> top(['Jan', 'Feb', 'Mar'])
    ['Jan', 'Feb']

    """
    get_top = input_list[:-1]

    return get_top


def first_three(input_list):
    """Return the first three elements of the input list.

    For example:

    >>> first_three(['Jan', 'Feb', 'Mar', 'Apr', 'May'])
    ['Jan', 'Feb', 'Mar']

    """

    get_first_three = input_list[:3]

    return get_first_three


def last_five(input_list):
    """Return the last five elements of the input list.

    For example:

    >>> last_five([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [15, 18, 21, 24, 27]

    """
    get_last_five = input_list[-5:]

    return get_last_five


def middle(input_list):
    """Return all elements of input_list except the first two and the last two.

    For example:

    >>> middle([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [6, 9, 12, 15, 18, 21]

    """
    get_middle = input_list[2:-2]

    return get_middle


def inner_four(input_list):
    """Return the third, fourth, fifth, and sixth elements of input_list.

    For example:

    >>> inner_four([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [6, 9, 12, 15]

    """
    get_inner_four = input_list[2:6]

    return get_inner_four


def inner_four_end(input_list):
    """Return the elements that are 6th, 5th, 4th, and 3rd from the end of input_list.

    This function should return those elements in a list, in the exact order
    described above.

    For example:

    >>> inner_four_end([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [12, 15, 18, 21]

    """

    inner_four_mid = input_list[-6:-2]

    return inner_four_mid


def replace_head(input_list):
    """Replace the head of input_list with the value 42 and return nothing.

    Input list must be modified in-place, not merely reassigned to a new value.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_head(multiples)
    >>> multiples
    [42, 3, 6, 9, 12, 15, 18, 21, 24, 27]

    """

    input_list[0] = 42


def replace_third_and_last(input_list):
    """Replace third and last elements of input_list with 37 and return nothing.

    Input list must be modified in-place, not merely reassigned to a new value.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_third_and_last(multiples)
    >>> multiples
    [0, 3, 37, 9, 12, 15, 18, 21, 24, 37]

    """

    input_list[2] = 37
    input_list[-1] = 37


def replace_middle(input_list):
    """Replace all elements of a list but the first two and last two with 42 and 37.

    After the replacement, 42 and 37 should appear in that order in input_list.
    Input list must be modified in-place, not merely reassigned to a new value.

    Return nothing.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_middle(multiples)
    >>> multiples
    [0, 3, 42, 37, 24, 27]

    """

    input_list[2:-2] = [42, 37]


def delete_third_and_seventh(input_list):
    """Remove third and seventh elements of input_list and return nothing.

    Input list must be modified in-place, not merely reassigned to a new value.

    For example:

    >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    >>> delete_third_and_seventh(notes)
    >>> notes
    ['Do', 'Re', 'Fa', 'So', 'La', 'Do']

    """

    input_list[2:3] = []
    input_list[5:6] = []


def delete_middle(input_list):
    """Remove all elements from input_list except the first two and last two.

    Input list must be modified in-place, not merely reassigned to a new value.

    Return nothing.

    For example:

    >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    >>> delete_middle(notes)
    >>> notes
    ['Do', 'Re', 'Ti', 'Do']

    """

    input_list[2:-2] = []
