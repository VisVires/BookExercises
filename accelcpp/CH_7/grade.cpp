#include <stdexcept>
#include <vector>
#include "grade.h"
#include "median.h"
#include "Student_info.h"

using std::domain_error;    using std::vector;

double grade(double midterm, double final, double homework)
{
    return .2 * midterm + .4 * final + .4 * homework;
}

double grade(double midterm, double final, const std::vector<double>& hw)
{
    if(hw.size() == 0)
        throw domain_error("student has done no homework");
    return grade(midterm, final, median(hw));
}

double grade(const Student_info& s)
{
    return grade(s.midterm, s.final, s.homework);
}
