#include <pybind11/pybind11.h>

int add(int a, int b)
{
    return a + b;
}

PYBIND11_MODULE(powerplant, m)
{
    m.doc() = "Casablanca metal video analysis engine";
    m.def("add", &add, "A function which adds two numbers");
}