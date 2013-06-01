from jingo import register


@register.filter
def yesno(val):
    if val:
        return 'Yes'
    return 'No'


@register.filter
def orNA(val):
    if val:
        return val
    return 'N/A'
