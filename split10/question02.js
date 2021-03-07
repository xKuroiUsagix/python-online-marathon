function combineArray(arr1, arr2) {
    function numbersOnly(value) {
        return typeof value == typeof Number();
    }
    return arr1.filter(numbersOnly).concat(arr2.filter(numbersOnly));
}