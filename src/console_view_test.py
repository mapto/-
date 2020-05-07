#!/usr/bin/env python3
# coding: utf-8


def test_draw_board():
    """ Test drawing of ASCII board. """

    from console_view import draw_board

    board = [
        [
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
        ],
        [
            "\x1b[35m . ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[35m . ",
        ],
        [
            "\x1b[35m . ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[0m   ",
            "\x1b[31m[ ]",
            "\x1b[31m[ ]",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[35m . ",
        ],
        [
            "\x1b[35m . ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[37m( )",
            "\x1b[31m + ",
            "\x1b[37m( )",
            "\x1b[0m   ",
            "\x1b[31m[ ]",
            "\x1b[31m[ ]",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[35m . ",
        ],
        [
            "\x1b[35m . ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[37m( )",
            "\x1b[31m + ",
            "\x1b[37m( )",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[35m . ",
        ],
        [
            "\x1b[35m . ",
            "\x1b[0m   ",
            "\x1b[34m[ ]",
            "\x1b[34m[ ]",
            "\x1b[0m   ",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[31m + ",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[35m . ",
        ],
        [
            "\x1b[35m . ",
            "\x1b[0m   ",
            "\x1b[34m[ ]",
            "\x1b[34m[ ]",
            "\x1b[0m   ",
            "\x1b[37m( )",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[31m + ",
            "\x1b[31m{ }",
            "\x1b[31m{ }",
            "\x1b[0m   ",
            "\x1b[37m( )",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[35m . ",
        ],
        [
            "\x1b[35m . ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[37m( )",
            "\x1b[34m{ }",
            "\x1b[34m{ }",
            "\x1b[0m   ",
            "\x1b[31m + ",
            "\x1b[31m{ }",
            "\x1b[31m{ }",
            "\x1b[0m   ",
            "\x1b[37m( )",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[35m . ",
        ],
        [
            "\x1b[35m . ",
            "\x1b[0m   ",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[34m{ }",
            "\x1b[34m{ }",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[0m   ",
            "\x1b[35m . ",
        ],
        [
            "\x1b[35m . ",
            "\x1b[0m   ",
            "\x1b[37m( )",
            "\x1b[34m + ",
            "\x1b[34m + ",
            "\x1b[34m + ",
            "\x1b[34m + ",
            "\x1b[34m + ",
            "\x1b[0m   ",
            ">|<",
            "\x1b[0m   ",
            "\x1b[32m + ",
            "\x1b[32m + ",
            "\x1b[32m + ",
            "\x1b[32m + ",
            "\x1b[32m + ",
            "\x1b[37m( )",
            "\x1b[0m   ",
            "\x1b[35m . ",
        ],
        [
            "\x1b[35m . ",
            "\x1b[0m   ",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[32m{ }",
            "\x1b[32m{ }",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[0m   ",
            "\x1b[35m . ",
        ],
        [
            "\x1b[35m . ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[37m( )",
            "\x1b[0m   ",
            "\x1b[33m{ }",
            "\x1b[33m{ }",
            "\x1b[33m + ",
            "\x1b[0m   ",
            "\x1b[32m{ }",
            "\x1b[32m{ }",
            "\x1b[37m( )",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[35m . ",
        ],
        [
            "\x1b[35m . ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[37m( )",
            "\x1b[0m   ",
            "\x1b[33m{ }",
            "\x1b[33m{ }",
            "\x1b[33m + ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[37m( )",
            "\x1b[0m   ",
            "\x1b[32m[ ]",
            "\x1b[32m[ ]",
            "\x1b[0m   ",
            "\x1b[35m . ",
        ],
        [
            "\x1b[35m . ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[33m + ",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[0m   ",
            "\x1b[32m[ ]",
            "\x1b[32m[ ]",
            "\x1b[0m   ",
            "\x1b[35m . ",
        ],
        [
            "\x1b[35m . ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[37m( )",
            "\x1b[33m + ",
            "\x1b[37m( )",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[35m . ",
        ],
        [
            "\x1b[35m . ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[33m[ ]",
            "\x1b[33m[ ]",
            "\x1b[0m   ",
            "\x1b[37m( )",
            "\x1b[33m + ",
            "\x1b[37m( )",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[35m . ",
        ],
        [
            "\x1b[35m . ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[33m[ ]",
            "\x1b[33m[ ]",
            "\x1b[0m   ",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[37m( )",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[35m . ",
        ],
        [
            "\x1b[35m . ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[0m   ",
            "\x1b[35m . ",
        ],
        [
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            " ",
            "\x1b",
            "[",
            "3",
            "6",
            "m",
            " ",
            ".",
            "\x1b[0m🏳️\u200d🌈",
        ],
    ]

    assert draw_board() == board
