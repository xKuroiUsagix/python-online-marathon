const howMuchSec = (...params) => {
    let seconds = params[0] || 0;
    for (let i = 1; i < params.length; i++) {
        if (i === 1) {
            seconds += params[i] * 60;
        }
        else if (i === 2) {
            seconds += params[i] * 60 * 60;
        }
        else if (i === 3) {
            seconds += params[i] * 60 * 60 * 24;
        }
        else if (i == 4) {
            seconds += params[i] * 60 * 60 * 24 * 7;
        }
        else if (i === 4) {
            seconds += params[i] * 60 * 60 * 24 * 7 * 30;
        }
        else if (i == 5) {
            seconds += params[i] * 60 * 60 * 24 * 7 * 30 * 12;
        }
    }
    return seconds;
}
