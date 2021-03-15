function mapCreator(keys, values) {
    if (keys.length != values.length) {
        throw Error("Lists are not same length");
    }

    const map = new Map();
    for (let i = 0; i < keys.length; i++) {
        if (typeof(values[i]) === "string") {
            map.set(keys[i], values[i]);
        }
    }
    return map;
}
