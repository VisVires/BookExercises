#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <stdexcept>
#include <algorithm>

#include "student_info.h"

using std::vector;      using std::string;
using std::cout;        using std::setprecision;
using std::endl;        using std::domain_error;
using std::cin;         using std::max;
using std::streamsize;

int main()
{
    vector<Student_info> students;
    Student_info record;
    string::size_type maxlen = 0;

    //read and store the data
    while(record.read(cin))
    {
        maxlen = max(maxlen, record.name().size());
        students.push_back(record);
    }

    sort(students.begin(), students.end(), compare);

    for(vector<Student_info>::size_type i = 0; i != students.size(); ++i)
    {
        cout << students[i].name() << string(maxlen + 1 - students[i].name().size(), ' ');
        try{
            double final_grade = students[i].grade();
            streamsize prec = cout.precision();
            cout << setprecision(3) << final_grade << setprecision(prec) << endl;
        }
        catch (domain_error e){
            cout << e.what() << endl;
        }
    }
    return 0;
}
