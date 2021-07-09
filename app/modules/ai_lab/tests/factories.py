import wagtail_factories
import factory
import pytest
import json

from modules.ai_lab.models.home_page import AiLabHomePage
from modules.ai_lab.models.resource_listings import (
    AiLabResourceIndexPage,
    AiLabUnderstandIndexPage,
    AiLabDevelopIndexPage,
    AiLabAdoptIndexPage,
    AiLabResourceCollection,
)
from modules.ai_lab.models.resources import (
    AiLabCaseStudy,
    AiLabExternalResource,
    AiLabInternalResource,
    AiLabGuidance,
    AiLabReport,
    AiLabTopic,
)

from modules.core.tests.factories import CorePageFactory
from wagtail.core.models import Site


class AiLabHomePageFactory(CorePageFactory):
    title = "Ai Lab Home"

    @factory.lazy_attribute
    def parent(self):
        return Site.objects.all()[0].root_page

    class Meta:
        model = AiLabHomePage


class AiLabTopicFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("word")

    class Meta:
        model = AiLabTopic


class ResourceFactory(CorePageFactory):
    summary = factory.Faker("sentence")

    @factory.post_generation
    def topics(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            topics = extracted
        else:
            topics = AiLabTopicFactory.create_batch(3)

        for topic in topics:
            self.topics.add(topic)

    class Meta:
        abstract = True


class AiLabCaseStudyFactory(ResourceFactory):
    title = factory.Sequence(lambda n: "Case Study %d" % n)

    class Meta:
        model = AiLabCaseStudy


class AiLabGuidanceFactory(ResourceFactory):
    title = factory.Sequence(lambda n: "Guidance %d" % n)

    class Meta:
        model = AiLabGuidance


class AiLabReportFactory(ResourceFactory):
    title = factory.Sequence(lambda n: "Report %d" % n)

    class Meta:
        model = AiLabReport


class AiLabExternalResourceFactory(ResourceFactory):
    title = factory.Sequence(lambda n: "External Resource %d" % n)
    external_url = factory.Faker("url")

    class Meta:
        model = AiLabExternalResource


class AiLabInternalResourceFactory(ResourceFactory):
    title = factory.Sequence(lambda n: "Internal Resource %d" % n)

    class Meta:
        model = AiLabInternalResource


class AiLabResourceCollectionFactory(ResourceFactory):
    title = factory.Sequence(lambda n: "Resource Collection %d" % n)

    @factory.lazy_attribute
    def resource_list(self):
        return [AiLabCaseStudyFactory.create()]

    @factory.lazy_attribute
    def resources(self):
        r = []
        for resource in self.resource_list:
            r.append({"type": "link", "value": resource.id})
        return json.dumps(r)

    class Meta:
        model = AiLabResourceCollection
        exclude = ("resource_list",)


class AiLabResourceIndexPageFactory(CorePageFactory):
    title = factory.Sequence(lambda n: "Case Study %d" % n)

    @factory.lazy_attribute
    def parent(self):
        return AiLabHomePageFactory.create()

    class Meta:
        model = AiLabResourceIndexPage


class AiLabCategoryIndexPageFactory(CorePageFactory):
    summary_title = "This is the summary title"
    summary_body = "This is the summary body"

    @factory.lazy_attribute
    def parent(self):
        return AiLabResourceIndexPageFactory.create()


class AiLabUnderstandIndexPageFactory(AiLabCategoryIndexPageFactory):
    title = "Resources to Understand AI"

    class Meta:
        model = AiLabUnderstandIndexPage


class AiLabDevelopIndexPageFactory(AiLabCategoryIndexPageFactory):
    title = "Resources to Develop AI"

    class Meta:
        model = AiLabDevelopIndexPage


class AiLabAdoptIndexPageFactory(AiLabCategoryIndexPageFactory):
    title = "Resources to Adopt AI"

    class Meta:
        model = AiLabAdoptIndexPage
