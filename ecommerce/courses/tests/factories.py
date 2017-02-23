

import factory
from factory.fuzzy import FuzzyText

from ecommerce.courses.models import Course


class CourseFactory(factory.DjangoModelFactory):
    class Meta(object):
        model = Course

    id = FuzzyText(prefix='course-v1:test-org+course+')
    name = FuzzyText(prefix='course-name-')
