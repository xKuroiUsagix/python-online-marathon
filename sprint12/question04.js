const Checker = require('./Checker.js');

class Student {
    
    constructor(fullName, direction) {
      this._fullName = fullName;
      this._direction = direction;
    }

    showFullName() {
        return this._fullName;
    }

    nameIncludes(data) {
        return this.showFullName().search(data) != -1;
    }

    static studentBuilder() {
        return new Student("Ihor Kohut", "qc");
    }

    get direction() {
        return this._direction;
    }

    set direction(direction) {
        if (direction instanceof String) {
            this._direction = direction;
        }
        else {
            throw Error("Wrong direction type.");
        }
    }
}

const stud1 = new Student("Ivan Petrenko", "web");
const stud2 = new Student("Sergiy Koval", "python");
const stud3 = Student.studentBuilder();
