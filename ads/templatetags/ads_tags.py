from django import template

from ads.models import DealType, HousingType, ProperType, Finishing

register = template.Library()


@register.inclusion_tag('base/tags/base_tag.html')
def get_filters():
    deal_type = DealType.objects.all()
    housing_type = HousingType.objects.all()
    proper_type = ProperType.objects.all()
    finishing = Finishing.objects.all()
    return {
        'deal_type': deal_type,
        'housing_type': housing_type,
        'proper_type': proper_type,
        'finishing': finishing
    }
