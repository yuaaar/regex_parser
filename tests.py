from parser import *

#check_answers checks parser on test_dict (key = test case, value = manually composed answer)
def check_answers(test_dict):
    for test in test_dict:
        solution = str(parse(test))
        if solution == test_dict[test]:
            print("CORRECT parse of " + test)
        else:
            print("\n")
            print("INCORRECT parse of " + test)
            print("parser produced  " + solution)
            print("should have been " + test_dict[test])
            print("\n")

print("tests for primitives")
print("\n")
cases = {"a": "prim(\"a\")",
        "ab ": "prim(\"ab \")",
        "(a)": "prim(\"a\")",
        "(a b)": "prim(\"a b\")"}
check_answers(cases)

print("********************")

print("tests for repetition modifiers")
print("\n")
cases = {"a+": "plus(prim(\"a\"))", 
        "ab?": "seq(prim(\"a\"), ques(prim(\"b\")))",
        "(a)*": "kleene(prim(\"a\"))",
        "(ab)+": "plus(prim(\"ab\"))",
        "(a?)": "ques(prim(\"a\"))",
        "(ab*)": "seq(prim(\"a\"), kleene(prim(\"b\")))"}
check_answers(cases)

print("********************")

print("tests for sequences")
print("\n")
cases = {"(a)(bc)": "seq(prim(\"a\"), prim(\"bc\"))",
        "a(bc)": "seq(prim(\"a\"), prim(\"bc\"))",
        "(ab)c": "seq(prim(\"ab\"), prim(\"c\"))",
        "(a)bc": "seq(prim(\"a\"), prim(\"bc\"))",
        "(a*)+b?": "seq(plus(kleene(prim(\"a\"))), ques(prim(\"b\")))",
        "((ab*)(cd(e))?fg+h)": "seq(seq(seq(seq(seq(prim(\"a\"), kleene(prim(\"b\"))), ques(seq(prim(\"cd\"), prim(\"e\")))), prim(\"f\")), plus(prim(\"g\"))), prim(\"h\"))"}
check_answers(cases)

print("********************")

print("tests for alternations")
print("\n")
cases = {"a|b": "alt(prim(\"a\"), prim(\"b\"))",
        "(ab)|(cd)": "alt(prim(\"ab\"), prim(\"cd\"))",
        "(ab)?|c*|(de)+": "alt(alt(ques(prim(\"ab\")), kleene(prim(\"c\"))), plus(prim(\"de\")))",
        "a|bc*|(d|(ef)g)": "seq(alt(prim(\"a\"), prim(\"b\")), alt(kleene(prim(\"c\")), seq(alt(prim(\"d\"), prim(\"ef\")), prim(\"g\"))))"}
check_answers(cases)

print("********************")
