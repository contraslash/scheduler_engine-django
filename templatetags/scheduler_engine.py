from django import template

register = template.Library()


@register.inclusion_tag("scheduler_engine/template_includes/scheduler_css.html", )
def scheduler_css():
    """
    Render the CSS link tags for views where the scheduler will be showed
    :return:
    """
    return {}


@register.inclusion_tag("scheduler_engine/template_includes/scheduler_js.html", )
def scheduler_js(events, locale):
    """
    Render the JS Script tags for views where the scheduler will be showed
    :param events: EventModel Objects array
    :param locale: String whit locale, recomended options: 'es', ''en
    :return:
    """
    return {
        'events': events,
        'locale': locale
    }

@register.inclusion_tag("scheduler_engine/template_includes/scheduler_html.html", )
def scheduler_html():
    """
    Render the HTML tag to load the scheduler
    :return:
    """
    return {}