const std = @import("std");
const py = @import("pydust");

pub fn hello() void {
    std.debug.print("HELLO WORLD\n", .{});
}

comptime {
    py.module(@This());
}

test "lib tests" {
    py.ffi.Py_Initialize();

    const pf = py.PyFloat.from(f64, 1.0);
    _ = pf;
}
