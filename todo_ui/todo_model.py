# -*- coding: utf-8 -*-
from openerp import models, fields, api

class Tag(models.Model):
    _name = 'todo.task.tag'
    name = fields.Char('Name', translate=True)

class Stage(models.Model):
    _name = 'todo.task.stage'
    _order = 'sequence,name'
    _rec_name = 'name'  # default
    _table = 'todo_task_stage'  # default
    name = fields.Char('Name', translate=True)
    sequence = fields.Integer('Sequence')
