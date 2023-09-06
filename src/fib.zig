const std = @import("std");
const py = @import("pydust");

pub fn get_fibonacci(args: *const extern struct { n: py.PyLong }) !u64 {
    return f(try args.n.as(u64));
}

fn f(n: u64) u64 {
    return if (n < 2) n else f(n - 1) + f(n - 2);
}

comptime {
    py.module(@This());
}

const testing = std.testing;

// "poetry run pytest" will run zig tests along with python tests.
// "zig build test" still works and runs just zig tests.
test "fibonacci test" {
    py.initialize();
    defer py.finalize();

    const pl = try py.PyLong.from(u64, 9);
    defer pl.decref();

    try testing.expectEqual(
        @as(u64, 34),
        try get_fibonacci(&.{ .n = pl }),
    );
}
