from ajax_datatable.views import AjaxDatatableView
# from django.contrib.auth.models import Permission
from .models import Contacts


class PermissionAjaxDatatableView(AjaxDatatableView):

    model = Contacts
    title = 'Permissions'
    initial_order = [["id", "name"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': False, },
        {'name': 'name', 'visible': True, },
        {'name': 'title', 'visible': True, },
        # {'name': 'app_label', 'foreign_field': 'content_type__app_label', 'visible': True, },
        # {'name': 'model', 'foreign_field': 'content_type__model', 'visible': True, },
    ]
