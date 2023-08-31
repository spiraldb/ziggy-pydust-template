const pyconf = @import("pyconf");
const std = @import("std");
const py = @import("pydust");

comptime {
    _ = py.module("_lib", struct {
        pub fn hello() void {
            std.debug.print("HELLO WORLD\n", .{});
        }
    });

    py.exportInitFunctions();
}

test "lib tests" {
    py.ffi.Py_Initialize();

    const pf = py.PyFloat.from(f64, 1.0);
    _ = pf;
}
