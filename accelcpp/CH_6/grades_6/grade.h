#ifndef GRADE_H_INCLUDED
#define GRADE_H_INCLUDED

#include <vector>
#include "Student_info.h"

double grade(double, double, double);
double grade(double, double, const std::vector<double>&);
double grade(const struct Student_info&);


#endif // GRADE_H_INCLUDED
