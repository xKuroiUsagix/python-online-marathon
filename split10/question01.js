function modifyArray(array) {
    let newArr = array.slice();
    newArr[0] = 'Start';
    newArr[newArr.length-1] = 'End';
    return newArr;
}