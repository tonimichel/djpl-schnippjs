

def refine_STATICS(original):

    original['GENERAL']['css']['files'] += [
        'schnippjs/styles/schnipp.ui.dialog.css',
        'schnippjs/styles/dynforms.css',
        'schnippjs/styles/dynforms/fields.css',
        'schnippjs/styles/dynforms/fields/dropdownselect.css',
        'schnippjs/styles/dynforms/fields/datepicker.css',
        'schnippjs/styles/dynforms/fields/inlines.css',
        'schnippjs/styles/dynforms/helptext_visitor.css',
        'schnippjs/styles/dynforms/fields/xorform.css',
        'schnippjs/styles/dynforms/fields/checkbox2.css',
        'schnippjs/styles/dynforms/fields/intslider.css',
    ]

    original['GENERAL']['js']['files'] += [
        'schnippjs/src/schnipp.js',
        'schnippjs/src/schnipp/events.js',
        'schnippjs/src/schnipp/net.js',
        #<!-- schnipp dynforms -->
        'schnippjs/src/schnipp/dynforms.js',
        'schnippjs/src/schnipp/dynforms/visitors.js',
        'schnippjs/src/schnipp/dynforms/fields.js',
        'schnippjs/src/schnipp/dynforms/abstract_field.js',
        'schnippjs/src/schnipp/dynforms/abstractselect.js',
        'schnippjs/src/schnipp/dynforms/primitive_field.js',
        'schnippjs/src/schnipp/dynforms/fields/dropdownselect.js',
        'schnippjs/src/schnipp/dynforms/fields/text.js',
        'schnippjs/src/schnipp/dynforms/fields/textarea.js',
        'schnippjs/src/schnipp/dynforms/fields/integer.js',
        'schnippjs/src/schnipp/dynforms/fields/floatingpoint.js',
        'schnippjs/src/schnipp/dynforms/fields/checkbox.js',
        'schnippjs/src/schnipp/dynforms/fields/checkbox2.js',
        'schnippjs/src/schnipp/dynforms/fields/select.js',
        'schnippjs/src/schnipp/dynforms/fields/datepicker.js',
        'schnippjs/src/schnipp/dynforms/fields/hiddeninput.js',
        'schnippjs/src/schnipp/dynforms/fields/optionalform.js',
        'schnippjs/src/schnipp/dynforms/fields/form.js',
        'schnippjs/src/schnipp/dynforms/fields/inlines.js',
        'schnippjs/src/schnipp/dynforms/fields/xorform.js',
        'schnippjs/src/schnipp/dynforms/fields/password.js',
        'schnippjs/src/schnipp/dynforms/fields/radioselect.js',
        'schnippjs/src/schnipp/dynforms/fields/intslider.js',
        'schnippjs/src/schnipp/dynforms/fields/multiselect.js',

        #<!-- schnipp tree -->
        'schnippjs/src/schnipp/tree.js',
        'schnippjs/src/schnipp/tree/ui.js',
        'schnippjs/src/schnipp/tree/model.js',
        'schnippjs/src/schnipp/tree/ui/jquery.mjs.nestedSortable.js',
        'schnippjs/src/schnipp/tree/ui/nestedsortable.js',
        'schnippjs/src/schnipp/tree/ui/treeview.js',
        'schnippjs/src/schnipp/tree/model/treenode.js',

        #<!-- schnipp models -->
        'schnippjs/src/schnipp/models.js',
        'schnippjs/src/schnipp/models/exceptions.js',
        'schnippjs/src/schnipp/models/observable.js',
        'schnippjs/src/schnipp/models/entity.js',

        #<!-- schnipp ui -->
        'schnippjs/src/schnipp/ui.js',
        'schnippjs/src/schnipp/ui/dialog.js',
        'schnippjs/src/schnipp/ui/list.js',
    ]
    return original
