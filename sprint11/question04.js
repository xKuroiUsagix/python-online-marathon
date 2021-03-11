const sumOfLen = (...strings) => {
    let sum = 0;
    for (let i = 0; i < strings.length; i++) {
        sum += strings[i].length;
    }
    return sum;
}
