var groupmates = [
    {
        "name": "Арсен",
        "surname": "Джабраилов",
        "group": "БСТ2351",
        "marks": [4, 3, 5]
    },
    {
        "name": "Владислав",
        "surname": "Авдеев",
        "group": "БСТ2351",
        "marks": [4, 4, 3]
    },
    {
        "name": "Анастасия",
        "surname": "Аксенова",
        "group": "БСТ2351",
        "marks": [4, 4, 4]
    },
    {
        "name": "Филипп",
        "surname": "Бардин",
        "group": "БСТ2352",
        "marks": [5, 5, 5]
    },
    {
        "name": "Михаил",
        "surname": "Виноградов",
        "group": "БСТ2353",
        "marks": [4, 3, 5]
    },
    {
        "name": "Алексей",
        "surname": "Гавриков",
        "group": "БСТ2351",
        "marks": [3, 3, 5]
    }
]

var rpad = function(str, length) {
    // js не поддерживает добавление нужного количества символов
    // справа от строки, т.е. аналога ljust из Python здесь нет 
    str = str.toString(); // преобразование в строку
    while (str.length < length)
        str = str + ' '; // добавление пробела в конец строки 
    return str; // когда все пробелы добавлены, возвратить строку
};

var printStudents = function(students) { 
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
    );
    // был выведен заголовок таблицы
    for (var i = 0; i<=students.length-1; i++) {
    // в цикле выводится каждый экземпляр студента 
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['surname'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['marks'], 20)
        );
    }
    console.log('\n'); // добавляется пустая строка в конце вывода
};
printStudents(groupmates); 

var filterGroup = function(students, group) {
    return students.filter(function(student) {
        return student['group'] ==group;
    });
};
function searchGroup(group) {
    printStudents(filterGroup(groupmates, group));
};

var filterAvg = function(students, minAvg) {
    return students.filter(function(student) {
        var sum = student['marks'].reduce(function(a, b) { return a + b; }, 0);
        var avg = sum / student['marks'].length;
        return avg > minAvg;
    });
};

function searchAvg(mark) {
    printStudents(filterAvg(groupmates, mark));
};