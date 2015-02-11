from django.utils.safestring import mark_safe
from django import forms


class DjangoAdminMultiselect(forms.SelectMultiple):
    class Media:
        extend = False
        css = {
            'all': ('css/django-admin-multiselect.css',)
        }
        js = ('js/django-admin-multiselect.js', )

    def render(self, name, value, attrs=None, choices=()):
        output = super(DjangoAdminMultiselect, self).render(name, value, attrs, choices)
        output += u'''
        	<script type="text/javascript">
				(function($) {
                    $(window).ready(function(){
                        $('#id_%s').multiSelect({});
                    });
                })(grp.jQuery || django.jQuery);
        	</script>
        ''' % name
        return mark_safe(output)