def my_context_processor(req):
    return {
        'domain_name': 'https://hogehoge.com',
        'site_name': 'Hogehoge Site',
    }