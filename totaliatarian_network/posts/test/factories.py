import factory

from totaliatarian_network.users.test.factories import UserFactory


class PostFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'posts.Post'

    text = factory.Faker("sentence")
    user = factory.SubFactory(UserFactory)
    # default is always False, included here explicitly
    private = False