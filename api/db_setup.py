from search_characters import models


def db_setup():
    print('STARTING DB_SETUP')

    # Create SearchIndexes
    index_list = ['foo_index', 'bar_index', 'baz_index', 'buzz_index']
    for index_name in index_list:
        models.SearchIndex.objects.get_or_create(name=index_name)
    print(f"CREATED SEARCH INDEXES {index_list}")

    # Create User Foo
    user_foo, was_user_created = models.User.objects.get_or_create(
        email="testfoo@testfooabc.com", name="foo", password="passw0rd")
    print('CREATED USER "foo"')

    # Add Indexes to Foo
    foo_index = models.SearchIndex.objects.get_or_create(name="foo_index")[0]
    bar_index = models.SearchIndex.objects.get_or_create(name="bar_index")[0]
    user_foo.index_list.add(foo_index)
    user_foo.index_list.add(bar_index)
    user_foo.save()
    print('Added ["foo_index", "bar_index"] to User "foo"')
    print('DB_SETUP COMPLETE')