load("@pybind11_bazel//:build_defs.bzl", "pybind_extension")

pybind_extension(
    name = "powerplant",
    srcs = ["powerplant.cpp"],
    visibility = ["//visibility:public"],
    deps = ["//src/powerplant/utilities"],
)

py_library(
    name = "powerplant",
    data = [":powerplant.so"],
    imports = ["."],
    visibility = ["//visibility:public"],
)
