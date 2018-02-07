# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
"""

__author__ = "Hans Bering"
__copyright__ = "Copyright 2017"
__credits__ = ["Hans Bering"]
__license__ = "MIT License"
__maintainer__ = "Hans Bering"
__email__ = "hansi.b.github@mgail.moc"
__status__ = "Development"

from reWrapped.modders import SingleValueField, TupleValueField


class _Group(SingleValueField):

    def __init__(self, index, defaultValue=None):
        super(_Group, self).__init__()
        assert index >= 0, "Group requires non-negative index argument (got {})".format(index)
        self._index = index
        self._defVal = defaultValue

    def check(self, pattern):
        assert pattern.groups >= self._index, \
            "Pattern {} has {} group(s) (got group index {})".format(pattern,
                                                                     pattern.groups,
                                                                     self._index)

    def fill(self, _string, matchObject):
        v = matchObject.group(self._index)
        return v if v is not None else self._defVal

    def __eq__(self, other):
        if not isinstance(other, _Group): return False
        return self._index == other._index and self._defVal == other._defVal

    def __hash__(self):
        return hash((self._index, self._defVal))


def g(idx: int):
    """
    The basic match group as a field on a ReWrap class. In match instances
    of that class, the field is the content of the respective single capturing
    `match group <https://docs.python.org/3/library/re.html#re.match.group>`_ content.
    For multiple groups, use :func:`gTuple`

    For the whole match, you can use the abbreviation :data:`g0`. Likewise, the first
    nine groups have the abbrevations :data:`g1` to :data:`g9`.

    :param idx: the non-negative index of the desired match group, where zero is the whole match
    :return:
        a match field for the group of the argument index
    :see: https://docs.python.org/3/library/re.html#re.match.group

    Example::

        >>> from reWrapped import ReWrap, matched
        >>> class TwoWords(ReWrap):
        ...     matchOn = "(\w+)\s+(\w+)"
        ...     firstWord = matched.g(1)
        ...     secondWord = matched.g(2)
        ...     allOfIt = matched.g(0)
        ...
        >>> w = TwoWords.search("hello world")
        >>> w.firstWord
        'hello'
        >>> w.secondWord
        'world'
        >>> w.allOfIt
        'hello world'
    """
    return _Group(idx)


def gOr(idx: int, defaultValue):
    """
    A match group like :func:`g`, but with a default value in case the group is not matched. Only
    makes sense for optional matches.

    :param idx: the non-negative index of the desired match group
    :param defaultValue: the value to return in case the group is not matched
    :return: a matcher for the group of the argument index

    Example:

    .. doctest::

        >>> from reWrapped import ReWrap, matched
        >>> class OptionalYear(ReWrap):
        ...     matchOn = "([0-9]{2})\.([0-9]{2})\.([0-9]{4})?"
        ...     day = matched.g1.asInt
        ...     month = matched.g2.asInt
        ...     year = matched.gOr(3, 2018).asInt
        ...
        >>> m = OptionalYear.search("02.03.")
        >>> m.day, m.month, m.year
        (2, 3, 2018)
        >>> m = OptionalYear.search("02.03.1999")
        >>> m.day, m.month, m.year
        (2, 3, 1999)

    Note that the default only applies to unmatched groups (i.e., which have a value of `None`),
    not to zero-length groups, which are matched to the empty string. In the following example,
    the default value will apply on a missing `numbers` group:

    .. doctest::

        >>> from reWrapped import ReWrap, matched
        >>> class OptNumbers(ReWrap):
        ...     matchOn = "([0-9])? ([a-z]+)"
        ...     numbers = matched.gOr(1, -1)
        ...     letters = matched.g2
        ...
        >>> m = OptNumbers.search(" abc")
        >>> m.numbers, m.letters
        (-1, 'abc')

    But if the number group can have a zero length, Python matches it as such, and consequently
    you get the empty string, not the default value:

    .. doctest::

        >>> from reWrapped import ReWrap, matched
        >>> class SomeNumbers(ReWrap):
        ...     matchOn = "([0-9]*) ([a-z]+)"
        ...     numbers = matched.gOr(1, -1)
        ...     letters = matched.g2
        ...
        >>> m = SomeNumbers.search(" xyz")
        >>> m.numbers, m.letters
        ('', 'xyz')

    """
    return _Group(idx, defaultValue)


g0 = _Group(0)
"""
An abbreviation for :func:`g(0) <g>` - the whole match,
like `matchobject.group() or matchobject.group(0) <https://docs.python.org/3/library/re.html#re.match.group>`_:

.. doctest::

    >>> from reWrapped import ReWrap, matched
    >>> class Word(ReWrap):
    ...     matchOn = "(\w)+"
    ...     txt = matched.g0
    ...
    >>> m = Word.search("... coconut! ")
    >>> m.txt
    'coconut'

"""  # pylint: disable=W0105

g1 = _Group(1)
"""
An abbreviation for :func:`g(1) <g>` - the content of the first capturing group,
like `matchobject.group(1) <https://docs.python.org/3/library/re.html#re.match.group>`_
"""  # pylint: disable=W0105

g2 = _Group(2)
"""
An abbreviation for :func:`g(2) <g>` - the content of the second capturing group,
like `matchobject.group(2) <https://docs.python.org/3/library/re.html#re.match.group>`_
"""  # pylint: disable=W0105
g3 = _Group(3)
"""
An abbreviation for :func:`g(3) <g>` - the content of the third capturing group,
like `matchobject.group(3) <https://docs.python.org/3/library/re.html#re.match.group>`_
"""  # pylint: disable=W0105
g4 = _Group(4)
"""
An abbreviation for :func:`g(4) <g>` - the content of the fourth capturing group,
like `matchobject.group(4) <https://docs.python.org/3/library/re.html#re.match.group>`_
"""  # pylint: disable=W0105
g5 = _Group(5)
"""
An abbreviation for :func:`g(5) <g>` - the content of the fifth capturing group,
like `matchobject.group(5) <https://docs.python.org/3/library/re.html#re.match.group>`_
"""  # pylint: disable=W0105
g6 = _Group(6)
"""
An abbreviation for :func:`g(6) <g>` - the content of the sixth capturing group,
like `matchobject.group(6) <https://docs.python.org/3/library/re.html#re.match.group>`_
"""  # pylint: disable=W0105
g7 = _Group(7)
"""
An abbreviation for :func:`g(7) <g>` - the content of the seventh capturing group,
like `matchobject.group(7) <https://docs.python.org/3/library/re.html#re.match.group>`_
"""  # pylint: disable=W0105
g8 = _Group(8)
"""
An abbreviation for :func:`g(8) <g>` - the content of the eigth capturing group,
like `matchobject.group(8) <https://docs.python.org/3/library/re.html#re.match.group>`_
"""  # pylint: disable=W0105
g9 = _Group(9)
"""
An abbreviation for :func:`g(9) <g>` - the content of the ninth capturing group,
like `matchobject.group(9) <https://docs.python.org/3/library/re.html#re.match.group>`_
"""  # pylint: disable=W0105


class _After(SingleValueField):

    def __init__(self):
        super(_After, self).__init__()

    def check(self, pattern):
        pass

    def fill(self, string, matchObject):
        return string[matchObject.end():]


class _Before(SingleValueField):

    def __init__(self):
        super(_Before, self).__init__()

    def check(self, pattern):
        pass

    def fill(self, string, matchObject):
        return string[:matchObject.start()]


after = _After()
"""
The part behind the match of a searched string.

Example:

.. doctest::

    >>> from reWrapped import ReWrap, matched
    >>> class Word(ReWrap):
    ...     matchOn = "(\w)+"
    ...     rest = matched.after
    ...
    >>> m = Word.search("... coconuts! and more!")
    >>> m.rest
    '! and more!'

""" # pylint: disable=W0105

before = _Before()
"""
The part in front of the match of a searched string.

Example:

.. doctest::

    >>> from reWrapped import ReWrap, matched
    >>> class Word(ReWrap):
    ...     matchOn = "(\w)+"
    ...     inFront = matched.before
    ...
    >>> m = Word.search("... coconut! and more!")
    >>> m.inFront
    '... '

""" # pylint: disable=W0105

class _GroupTuple(TupleValueField):

    def __init__(self, *indices):
        super(_GroupTuple, self).__init__()
        assert len(indices) == 0 or min(indices) >= 0, \
            "GroupTuple requires non-negative index arguments (got {})".format(indices)

        self._indices = tuple(indices)

    def check(self, pattern):
        if len(self._indices) > 0:
            assert pattern.groups >= max(self._indices), \
                "Pattern {} has {} group(s) (got group indices {})".format(pattern,
                                                                           pattern.groups,
                                                                           self._indices)
        else:
            assert pattern.groups > 1, \
                "Pattern {} has {} group(s) (got empty group indices)".format(pattern,
                                                                              pattern.groups,
                                                                              self._indices)

    def fill(self, _string, matchObject):
        if len(self._indices) == 0: return matchObject.groups()
        return tuple(matchObject.group(i) for i in self._indices)


def gTuple(*indices):
    """
    Blahblah
    """
    return _GroupTuple(*indices)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
