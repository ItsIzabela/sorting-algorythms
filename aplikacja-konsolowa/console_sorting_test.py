import pytest
from io import StringIO
import sys

from console_sorting import Sorting


class TestSorting:
    def setup_method(self):
        self.sorting = Sorting("", [])

    def test_bubble_sort(self):
        self.sorting.array = [5, 3, 8, 1]
        assert self.sorting.bubble_sort() == [1, 3, 5, 8]

    def test_selection_sort(self):
        self.sorting.array = [5, 3, 8, 1]
        assert self.sorting.selection_sort() == [1, 3, 5, 8]

    def test_insertion_sort(self):
        self.sorting.array = [5, 3, 8, 1]
        assert self.sorting.insertion_sort() == [1, 3, 5, 8]

    def test_quick_sort(self):
        self.sorting.array = [5, 3, 8, 1]
        assert self.sorting.quick_sort() == [1, 3, 5, 8]

    def test_heap_sort(self):
        self.sorting.array = [5, 3, 8, 1]
        assert self.sorting.heap_sort() == [1, 3, 5, 8]

    def test_choose_array(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', StringIO('5 3 8 1\n'))
        self.sorting.choose_array()
        assert self.sorting.array == [5, 3, 8, 1]

    def test_choose_sorting_method_prints(self, capsys):
        self.sorting.choose_sorting_method()
        captured = capsys.readouterr()
        assert "Wybierz metode sortowania" in captured.out
        assert "Sortowanie bąbelkowe" in captured.out
        assert "Sortowanie Heap" in captured.out
