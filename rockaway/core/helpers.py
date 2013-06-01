from jingo import register


@register.filter
def yesno(val):
    if val:
        return 'Yes'
    return 'No'
