function longestLogin(loginList) {
    function reducer(previous, current) {
        if (previous.length <= current.length) {
            return current;
        }
        return previous
    }
    return loginList.reduce(reducer);
}