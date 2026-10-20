# -*- coding: utf-8 -*-
"""Kiem 22 — chung minh hanh vi auditor/rules/m07_adverse_action_review.py
   KHONG doi giua b-freeze va HEAD, du AST (bao gom docstring) co doi.

   Boi canh: dong 1 commit vao auditor/ SAU b-freeze (don ten nguoi thuc
   trong docstring, dong 13). ast.parse() thuan tuy chi chung minh file
   con hop le ve CU PHAP, khong chung minh HANH VI khong doi, vi docstring
   nam trong AST (Module/FunctionDef/ClassDef body[0] la ast.Expr(Constant
   str)). pm phat hien thieu sot nay (xem docs/TASKS.md).

   Phep kiem dung: bo node docstring roi so sanh ast.dump() cua ban cu
   (tai b-freeze, qua `git show`) va ban moi (tren dia). Giong het = hanh
   vi (moi lenh, moi bieu thuc ngoai docstring) khong doi."""
import ast, subprocess, sys

FILE = 'auditor/rules/m07_adverse_action_review.py'

def strip_docstrings(tree):
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if (node.body and isinstance(node.body[0], ast.Expr)
                and isinstance(node.body[0].value, ast.Constant)
                and isinstance(node.body[0].value.value, str)):
                node.body.pop(0)
    return tree

old_src = subprocess.run(['git', 'show', f'b-freeze:{FILE}'],
                          capture_output=True, text=True, encoding='utf-8', check=True).stdout
new_src = open(FILE, encoding='utf-8').read()

t_old, t_new = ast.parse(old_src), ast.parse(new_src)
same_with_doc = ast.dump(t_old) == ast.dump(t_new)
same_without_doc = ast.dump(strip_docstrings(ast.parse(old_src))) == ast.dump(strip_docstrings(ast.parse(new_src)))

print('=== KIEM 22 — %s: hanh vi khong doi sau b-freeze ===' % FILE)
print('  AST giong het (CO docstring) : %s  (ky vong False — docstring da sua)' % same_with_doc)
print('  AST giong het (BO docstring) : %s  (ky vong True  — day la bang chung hanh vi)' % same_without_doc)

ok = (same_with_doc is False) and (same_without_doc is True)
print('\n' + '=' * 70)
print('KET QUA: %s' % ('PASS' if ok else 'FAIL'))
sys.exit(0 if ok else 1)
