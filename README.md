regex_parser
============

convert regex into ast, originally written for https://github.com/rickbhardwaj/regex-language

designed to work in conjunction with a lua-style backtracking matching algorithm, the current parser returns left associative seq and alt nodes, and supports "*", "+", and "?", as well as parens denoting groupings. 

Currently cannot parse spaces between groupings, but have decided that spaces between groupings complicates syntax, rather than making it more approachable. The parser should either ignore all spaces, or accept spaces as valid tokens, disallowing random spaces between groupings, and I've decided the second option to be more convenient.

Future work will probably center around ignoring special characters.
