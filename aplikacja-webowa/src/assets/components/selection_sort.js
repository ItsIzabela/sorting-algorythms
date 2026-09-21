export function SelectionSort(array) {
    let n = array.length;
    for(let i = 0; i < n - 1; i++) {
        let min_index = i;
        for(let j = i + 1; j < n; j++) {
            if(array[j] < array[min_index]) {
                min_index = j;
            }
        }
        if(min_index !== i) {
            [array[i], array[min_index]] = [array[min_index], array[i]];
        }
    }
    return array;
}
