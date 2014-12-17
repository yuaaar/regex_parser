regex_parser
============

convert regex into ast, originally written for https://github.com/rickbhardwaj/regex-language

designed to work in conjunction with a lua-style backtracking matching algorithm, the current parser returns left associative seq and alt nodes, and supports "*", "+", and "?", as well as parens denoting groupings. Currently cannot parse spaces between groupings. Future work will probably center around ignoring special characters and dealing with spaces.