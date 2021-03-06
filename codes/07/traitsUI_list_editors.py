# -*- coding: utf-8 -*-
"""
TraitsUI的各种编辑List的编辑器
"""

from enthought.traits.api import HasTraits, Unicode, Int, List, Instance
from enthought.traits.ui.api import View, Item, TableEditor, ListEditor, HGroup
from enthought.traits.ui.table_column import ObjectColumn   

class Employee(HasTraits):
    name = Unicode(label="姓名") 
    department = Unicode(label="部门")
    salary = Int(label="薪水")
    bonus = Int(label="奖金")
    view = View("name", "department", "salary", "bonus") 
 
table_editor = TableEditor(  
    columns = [
        ObjectColumn(name="name", label="姓名"), 
        ObjectColumn(name="department", label="部门"),
        ObjectColumn(name="salary", label="薪水"),
        ObjectColumn(name="bonus", label="奖金")
    ],
    row_factory = Employee,
    deletable = True,
    show_toolbar = True)

list_editor = ListEditor(style="custom") 
tab_editor = ListEditor(use_notebook=True, deletable=True, page_name=".name") 
 
class EmployeeList(HasTraits):
    employees = List(Instance(Employee, factory=Employee)) 
    view = View(
        HGroup(
            Item("employees", editor=table_editor), 
            Item("employees", editor=list_editor),
            Item("employees", style="custom", editor=tab_editor),
            show_labels=False
        ),
        resizable=True,
        width = 600,
        title="列表编辑器演示"
    )

    
demo = EmployeeList()
demo.employees = [
    Employee(name="张三", department="开发", salary=6000, bonus=0),
    Employee(name="李四", department="管理", salary=10000, bonus=5000),   
]
demo.configure_traits()