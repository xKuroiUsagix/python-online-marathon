function factorial(n) {
    if (n === 1 || n === 0) {
        return 1;
    }
    else {
        return n * factorial(n - 1);
    }
}

function processArray(arr, factorial) {
    let newArr = arr.slice();
    newArr.forEach((element, index) => {
        newArr[index] = factorial(element);
    });
    return newArr;
}