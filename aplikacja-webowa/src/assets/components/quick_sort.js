export function QuickSort(array) {
    if (array.length <= 1) return array;

    let pivot = array[0];
    let left = [];
    let right = [];

    for (let i = 1; i < array.length; i++) {
        if (array[i] < pivot) {
            left.push(array[i]);
        } else {
            right.push(array[i]);
        }
    }
    return [...QuickSort(left), pivot, ...QuickSort(right)];
}
