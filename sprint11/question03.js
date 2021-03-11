const maxInterv = (...args) => {
    let max = 0;
    for (let i = 0; i < args.length - 1; i++) {
        let difference = Math.abs(args[i] - args[i + 1]);
        max = difference > max ? difference : max;
    }
    return max;
}
