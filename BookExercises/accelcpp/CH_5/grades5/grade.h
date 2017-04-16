#ifndef GRADE_H_INCLUDED
#define GRADE_H_INCLUDED

#include <list>
#include <vector>
#include "Student_info.h"

double grade(double, double, double);
double grade(double, double, const std::vector<double>&);
double grade(const Student_info&);


#endif // GRADE_H_INCLUDED
