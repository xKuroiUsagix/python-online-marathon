const filterNums = (arr, number=0, param='greater') => {
    let is_greater = param === 'greater' ? true : false;
    return arr.filter(item => {
        return (is_greater && item > number) || (!is_greater && item < number);
    });
};
