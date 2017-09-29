from menu.models import MenuItem


class MenuContextMixin(object):

    def get_context_data(self, **kwargs):
        context = super(MenuContextMixin, self).get_context_data(**kwargs)
        context['menu'] = MenuItem.objects.all()

        return context
